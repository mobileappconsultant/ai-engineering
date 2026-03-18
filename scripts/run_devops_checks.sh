#!/usr/bin/env bash
set -euo pipefail

if [ -f docker/docker-compose.yml ]; then
  echo "Checking docker compose config..."
  docker compose -f docker/docker-compose.yml config >/dev/null
fi

if [ -f docker/Dockerfile ]; then
  echo "Checking Dockerfile build..."
  docker build -f docker/Dockerfile -t ai-check-temp . >/dev/null
fi

echo "DevOps checks completed."
