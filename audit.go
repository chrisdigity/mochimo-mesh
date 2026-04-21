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
	Running            bool   `json:"running"`
	Stage              string `json:"stage"`
	StartedAt          int64  `json:"started_at,omitempty"`
	FinishedAt         int64  `json:"finished_at,omitempty"`
	CurrentHeight      uint64 `json:"current_height"`
	FirstOverlapHeight uint64 `json:"first_overlap_height,omitempty"`
	InitialDBHeight    uint64 `json:"initial_db_height,omitempty"`
	OverlapFound       bool   `json:"overlap_found"`
	ScannedCount       uint64 `json:"scanned_count"`
	MissingCount       uint64 `json:"missing_count"`
	RepairedCount      uint64 `json:"repaired_count"`
	FailedCount        uint64 `json:"failed_count"`
	LastError          string `json:"last_error,omitempty"`
}

var blockAuditMu sync.RWMutex
var blockAuditStatus = BlockAuditStatus{}

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

func StartStartupBlockAudit(db *indexer.Database) {
	if !Globals.EnableStartupAudit {
		return
	}

	go runStartupBlockAudit(db)
}

func runStartupBlockAudit(db *indexer.Database) {
	now := time.Now().UnixMilli()
	updateBlockAuditStatus(func(status *BlockAuditStatus) {
		status.Enabled = Globals.EnableStartupAudit
		status.RepairEnabled = Globals.StartupAuditRepair
		status.Running = true
		status.Stage = "initializing"
		status.StartedAt = now
		status.FinishedAt = 0
		status.CurrentHeight = 0
		status.FirstOverlapHeight = 0
		status.InitialDBHeight = 0
		status.OverlapFound = false
		status.ScannedCount = 0
		status.MissingCount = 0
		status.RepairedCount = 0
		status.FailedCount = 0
		status.LastError = ""
	})

	finish := func(stage, lastError string) {
		updateBlockAuditStatus(func(status *BlockAuditStatus) {
			status.Running = false
			status.Stage = stage
			status.FinishedAt = time.Now().UnixMilli()
			status.LastError = lastError
		})
	}

	if db == nil {
		finish("failed", "indexer database not initialized")
		return
	}

	lowestHeight, err := db.GetLowestBlockHeight()
	if err != nil {
		mlog(3, "§bStartupBlockAudit(): §4Error getting lowest indexed block height: §c%s", err)
		finish("failed", err.Error())
		return
	}
	if lowestHeight == nil {
		mlog(4, "§bStartupBlockAudit(): §7Skipping startup audit because the indexer has no indexed blocks yet")
		finish("idle", "")
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
				status.OverlapFound = true
				status.FirstOverlapHeight = height
				status.ScannedCount = 1
			})
			mlog(4, "§bStartupBlockAudit(): §7Found first overlapping indexed block at height §9%d", height)
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
		mlog(4, "§bStartupBlockAudit(): §7Missing canonical block at height §9%d §7hash §60x%s", height, hash)

		if !Globals.StartupAuditRepair {
			return nil
		}

		block, err := GetBlockByHexHash("0x" + hash)
		if err != nil {
			updateBlockAuditStatus(func(status *BlockAuditStatus) {
				status.FailedCount++
				status.LastError = err.Error()
			})
			mlog(3, "§bStartupBlockAudit(): §4Error retrieving missing canonical block §60x%s§4: §c%s", hash, err)
			return nil
		}

		db.PushBlock(block)
		updateBlockAuditStatus(func(status *BlockAuditStatus) {
			status.RepairedCount++
		})
		return nil
	})
	if err != nil {
		mlog(3, "§bStartupBlockAudit(): §4Audit failed: §c%s", err)
		finish("failed", err.Error())
		return
	}

	if !overlapFound {
		mlog(4, "§bStartupBlockAudit(): §7No overlapping block hashes found between tfile history and the indexer database")
		finish("no_overlap", "")
		return
	}

	finish("completed", "")
}
