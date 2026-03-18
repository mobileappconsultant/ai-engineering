#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(pwd)"

mkdir -p "$ROOT_DIR/ai/AGENTS"
mkdir -p "$ROOT_DIR/ai/docs"
mkdir -p "$ROOT_DIR/ai/runtime"
mkdir -p "$ROOT_DIR/.claude/commands"
mkdir -p "$ROOT_DIR/.githooks"
mkdir -p "$ROOT_DIR/scripts"

echo "AI Engineering System files are present in this repository."
echo "If copying into another project, copy:"
echo "  ai/ .claude/ .githooks/ scripts/"
echo
echo "Then run:"
echo "  git config core.hooksPath .githooks"
echo "  chmod +x .githooks/pre-commit .githooks/post-commit scripts/*.sh"
