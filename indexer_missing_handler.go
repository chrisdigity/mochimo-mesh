package main

import (
	"encoding/json"
	"net/http"
)

type IndexerMissingRequest struct {
	NetworkIdentifier NetworkIdentifier `json:"network_identifier"`
}

type IndexerMissingResponse struct {
	TotalCount    int            `json:"total_count"`
	MissingBlocks []MissingBlock `json:"missing_blocks"`
}

func indexerMissingHandler(w http.ResponseWriter, r *http.Request) {
	var req IndexerMissingRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		mlog(3, "§bindexerMissingHandler(): §4Error decoding request: §c%s", err)
		giveError(w, ErrInvalidRequest)
		return
	}

	if req.NetworkIdentifier.Blockchain != Constants.NetworkIdentifier.Blockchain ||
		req.NetworkIdentifier.Network != Constants.NetworkIdentifier.Network {
		mlog(3, "§bindexerMissingHandler(): §4Wrong network identifier")
		giveError(w, ErrWrongNetwork)
		return
	}

	missingBlocks := snapshotBlockAuditMissingBlocks()
	response := IndexerMissingResponse{
		TotalCount:    len(missingBlocks),
		MissingBlocks: missingBlocks,
	}
	json.NewEncoder(w).Encode(response)
}