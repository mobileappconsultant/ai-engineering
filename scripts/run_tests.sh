#!/usr/bin/env bash
set -euo pipefail

if [ -d tests/unit ]; then
  echo "Running unit tests..."
  pytest tests/unit
fi

if [ -d tests/integration ]; then
  echo "Running integration tests..."
  pytest tests/integration
fi

if [ -d tests/regression ]; then
  echo "Running regression tests..."
  pytest tests/regression
fi
