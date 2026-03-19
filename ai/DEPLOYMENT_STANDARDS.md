# DEPLOYMENT_STANDARDS

All deployments must be safe, observable, recoverable, and resistant to trivial failure.

---

## Containers

Every production container must define:

* restart policy
* healthcheck
* explicit image tag
* resource limits where supported
* non-root user where possible
* stdout/stderr logging
* graceful shutdown handling

Do not use `latest` in production.

---

## Docker

Rules:

* multi-stage builds preferred
* slim base images preferred
* dependencies pinned
* no secrets baked into images
* writable paths must be explicit
* unnecessary packages must not be installed

---

## Runtime Safety

Services must include:

* health endpoints
* readiness logic for critical dependencies
* bounded startup assumptions
* retry or wait strategy for dependency readiness
* timeouts for external calls

---

## Caddy / Reverse Proxy

Use Caddy with:

* HTTPS termination
* sane timeouts
* security headers where appropriate
* upstream routing clarity
* minimal exposed surface area

---

## Safe Deployments

Prefer:

* rolling deployments
* blue-green deployments
* staged rollout where feasible

Minimum requirement:

* rollback command documented
* previous working image available
* migration compatibility considered before deploy

---

## Rollbacks

Every deploy must have:

* previous image tag
* rollback procedure
* data migration rollback or compatibility strategy
* clear decision point for rollback

---

## Database Migrations

* backwards-compatible first
* destructive later
* do not require instant simultaneous cutover unless explicitly approved

---

## Resource Protection

For constrained hosts:

* define realistic worker concurrency
* cap Redis memory where relevant
* prevent unbounded queue behaviour
* use logging rotation
* avoid memory-amplifying defaults

---

## Monitoring

Minimum:

* healthchecks
* logs
* restart visibility
* disk usage awareness
* memory and CPU visibility

---

## Security Requirements

* no public admin surfaces without protection
* no debug mode in production
* no exposed internal ports without reason
* no plaintext secrets in compose files committed to repo
