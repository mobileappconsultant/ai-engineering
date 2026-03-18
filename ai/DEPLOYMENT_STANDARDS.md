# DEPLOYMENT_STANDARDS

All deployments must be safe, observable, and recoverable.

## Containers
Every production container should define:
- restart policy
- healthcheck
- resource limits
- non-root user where possible
- stdout/stderr logging
- explicit image version tags

Do not use `latest` in production.

## Docker
- slim base images preferred
- multi-stage builds preferred
- dependencies pinned
- secrets never baked into images

## Caddy
Use Caddy as reverse proxy with:
- HTTPS termination
- sensible timeouts
- upstream health awareness where applicable

## Safe Deployments
Prefer:
- rolling deployments
- blue-green deployments
- canary where justified

Minimum requirement:
- rollback plan documented
- previous working image available
- migrations applied safely

## Rollbacks
Every deploy must have:
- rollback command
- previous image/tag
- migration rollback plan or compatibility strategy

## DB Migrations
- backwards-compatible first
- destructive later
- no coupled deploy that requires instant cutover unless approved

## Environment Management
- environment variables only
- no secrets in repo
- separate dev/staging/prod configs

## Monitoring
Minimum:
- healthchecks
- logs
- restart visibility
- resource visibility

## Failure Handling
If health fails:
- traffic should stop reaching bad instances where possible
- rollback should be preferred over heroic debugging in prod
