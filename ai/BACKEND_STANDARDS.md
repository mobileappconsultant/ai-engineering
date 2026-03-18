# BACKEND_STANDARDS

Backend code must be production-safe.

## Architecture
Use:
- API/controller layer
- service layer
- repository/data access layer
- infrastructure adapters

Do not put business logic in route handlers.

## Dependency Injection
Use DI for:
- repositories
- service classes
- external clients
- config providers
- caches
- message brokers

Prefer explicit injection over hidden singletons.

## Circuit Breakers
Required when calling:
- third-party APIs
- rate-limited APIs
- flaky internal services
- slow network dependencies

Must support:
- closed / open / half-open states
- failure threshold
- reset timeout
- fallback behavior
- structured logging

## Retries
Retries must be:
- bounded
- backoff-based
- idempotent-aware

Do not retry blindly.

## Healthchecks
Backend services should expose:
- liveness
- readiness
- dependency health where appropriate

## Queue Safety
For async workers:
- ack policy must be explicit
- task time limits required
- prefetch tuned
- retries bounded
- poison message strategy defined

## Data Safety
- migrations must be reversible where possible
- destructive migrations require explicit approval
- schema changes must consider zero-downtime rollout

## Observability
- structured logs
- correlation IDs where relevant
- actionable error messages
- metrics where feasible

## Circuit Breaker Requirement
Mandatory when:
- calling external APIs
- handling OCR / NLP / AI calls
- using queues or async workers

Must define:
- failure threshold
- retry strategy
- timeout
- fallback
