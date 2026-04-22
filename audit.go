package main

import (
	"encoding/binary"
	"encoding/hex"
	"sync"
	"time"

	"mochimo-mesh/indexer"

	"github.com/NickP005/go_mcminterface"
)

type BlockAuditStatus struct {
	Enabled            bool   `json:"enabled"`
	RepairEnabled      bool   `json:"repair_enabled"`
	Stage              string `json:"stage"`
	StartedAt          int64  `json:"started_at,omitempty"`
	FinishedAt         int64  `json:"finished_at,omitempty"`
	CurrentHeight      uint64 `json:"current_height"`
	FirstOverlapHeight uint64 `json:"first_overlap_height,omitempty"`
	InitialDBHeight    uint64 `json:"initial_db_height,omitempty"`
	ScannedCount       uint64 `json:"scanned_count"`
	MissingCount       uint64 `json:"missing_count"`
	RepairedCount      uint64 `json:"repaired_count"`
}

type MissingBlock struct {
	Height uint64 `json:"height"`
	Hash   string `json:"hash"`
}

var blockAuditMu sync.RWMutex
var blockAuditStatus = BlockAuditStatus{}
var blockAuditMissingBlocks []MissingBlock

func updateBlockAuditStatus(update func(*BlockAuditStatus)) {
	blockAuditMu.Lock()
	defer blockAuditMu.Unlock()
	update(&blockAuditStatus)
}

func snapshotBlockAuditStatus() BlockAuditStatus {
	blockAuditMu.RLock()
	defer blockAuditMu.RUnlock()
	return blockAuditStatus
}

func resetBlockAuditMissingBlocks() {
	blockAuditMu.Lock()
	defer blockAuditMu.Unlock()
	blockAuditMissingBlocks = nil
}

func snapshotBlockAuditMissingBlocks() []MissingBlock {
	blockAuditMu.RLock()
	defer blockAuditMu.RUnlock()
	missingBlocks := make([]MissingBlock, len(blockAuditMissingBlocks))
	copy(missingBlocks, blockAuditMissingBlocks)
	return missingBlocks
}

func addBlockAuditMissingBlock(height uint64, hash string) {
	blockAuditMu.Lock()
	defer blockAuditMu.Unlock()
	blockAuditMissingBlocks = append(blockAuditMissingBlocks, MissingBlock{
		Height: height,
		Hash:   hash,
	})
}

func removeBlockAuditMissingBlock(height uint64, hash string) {
	blockAuditMu.Lock()
	defer blockAuditMu.Unlock()
	for index := range blockAuditMissingBlocks {
		if blockAuditMissingBlocks[index].Height == height && blockAuditMissingBlocks[index].Hash == hash {
			blockAuditMissingBlocks = append(blockAuditMissingBlocks[:index], blockAuditMissingBlocks[index+1:]...)
			return
		}
	}
}

func StartBlockAudit(db *indexer.Database) {
	if !Globals.EnableAudit {
		resetBlockAuditMissingBlocks()
		updateBlockAuditStatus(func(status *BlockAuditStatus) {
			status.Enabled = false
			status.RepairEnabled = Globals.AuditRepair
			status.Stage = "disabled"
			status.StartedAt = 0
			status.FinishedAt = 0
			status.CurrentHeight = 0
			status.FirstOverlapHeight = 0
			status.InitialDBHeight = 0
			status.ScannedCount = 0
			status.MissingCount = 0
			status.RepairedCount = 0
		})
		return
	}

	go runBlockAudit(db)
}

func runBlockAudit(db *indexer.Database) {
	resetBlockAuditMissingBlocks()
	now := time.Now().UnixMilli()
	updateBlockAuditStatus(func(status *BlockAuditStatus) {
		status.Enabled = Globals.EnableAudit
		status.RepairEnabled = Globals.AuditRepair
		status.Stage = "initializing"
		status.StartedAt = now
		status.FinishedAt = 0
		status.CurrentHeight = 0
		status.FirstOverlapHeight = 0
		status.InitialDBHeight = 0
		status.ScannedCount = 0
		status.MissingCount = 0
		status.RepairedCount = 0
	})

	finish := func(stage string) {
		updateBlockAuditStatus(func(status *BlockAuditStatus) {
			status.Stage = stage
			status.FinishedAt = time.Now().UnixMilli()
		})
	}

	if db == nil {
		finish("failed")
		return
	}

	lowestHeight, err := db.GetLowestBlockHeight()
	if err != nil {
		mlog(3, "§bBlockAudit(): §4Error getting lowest indexed block height: §c%s", err)
		finish("failed")
		return
	}
	if lowestHeight == nil {
		mlog(4, "§bBlockAudit(): §7Skipping block audit because the indexer has no indexed blocks yet")
		finish("idle")
		return
	}

	updateBlockAuditStatus(func(status *BlockAuditStatus) {
		status.InitialDBHeight = *lowestHeight
		status.Stage = "seeking_overlap"
	})

	overlapFound := false
	err = iterateBlockTrailers(TFILE_PATH, func(trailer go_mcminterface.BTRAILER) error {
		height := uint64(binary.LittleEndian.Uint32(trailer.Bnum[:]))
		if !overlapFound && height < *lowestHeight {
			return nil
		}

		hash := hex.EncodeToString(trailer.Bhash[:])
		updateBlockAuditStatus(func(status *BlockAuditStatus) {
			status.CurrentHeight = height
		})

		existing, err := db.GetBlockByHeightAndHash(height, hash)
		if err != nil {
			return err
		}

		if !overlapFound {
			if existing == nil {
				return nil
			}

			overlapFound = true
			updateBlockAuditStatus(func(status *BlockAuditStatus) {
				status.Stage = "auditing"
				status.FirstOverlapHeight = height
				status.ScannedCount = 1
			})
			mlog(4, "§bBlockAudit(): §7Found first overlapping indexed block at height §9%d", height)
			return nil
		}

		updateBlockAuditStatus(func(status *BlockAuditStatus) {
			status.ScannedCount++
		})

		if existing != nil {
			return nil
		}

		updateBlockAuditStatus(func(status *BlockAuditStatus) {
			status.MissingCount++
		})
		addBlockAuditMissingBlock(height, hash)
		mlog(4, "§bBlockAudit(): §7Missing canonical block at height §9%d §7hash §60x%s", height, hash)

		if !Globals.AuditRepair {
			return nil
		}

		block, err := GetBlockByHexHash("0x" + hash)
		if err != nil {
			mlog(3, "§bBlockAudit(): §4Error retrieving missing canonical block §60x%s§4: §c%s", hash, err)
			return nil
		}

		db.PushBlock(block)
		repairedBlock, err := db.GetBlockByHeightAndHash(height, hash)
		if err != nil {
			mlog(3, "§bBlockAudit(): §4Error verifying repaired block §60x%s§4: §c%s", hash, err)
			return nil
		}
		if repairedBlock == nil {
			mlog(3, "§bBlockAudit(): §4Repair did not index missing canonical block §60x%s", hash)
			return nil
		}
		removeBlockAuditMissingBlock(height, hash)
		updateBlockAuditStatus(func(status *BlockAuditStatus) {
			status.RepairedCount++
		})
		return nil
	})
	if err != nil {
		mlog(3, "§bBlockAudit(): §4Audit failed: §c%s", err)
		finish("failed")
		return
	}

	if !overlapFound {
		mlog(4, "§bBlockAudit(): §7No overlapping block hashes found between tfile history and the indexer database")
		finish("no_overlap")
		return
	}

	finish("completed")
}
