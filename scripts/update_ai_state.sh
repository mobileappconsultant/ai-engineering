#!/usr/bin/env bash
set -euo pipefail

if [ ! -f ai/MASTER_STATE.md ]; then
  exit 0
fi

echo "MASTER_STATE exists. Update manually or via Claude after significant changes."
