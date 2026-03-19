# BACKEND_STANDARDS

Backend code must be production-safe, secure, observable, and resilient.

---

## Architecture

Use:

* API/controller layer
* service layer
* repository/data access layer
* infrastructure adapters

Do not put business logic in route handlers.

---

## FastAPI Rules

* Use Pydantic models for all request and response contracts
* Use dependency injection for auth, config, repositories, and clients
* Keep route handlers thin
* Centralise exception handling
* Validate and sanitise request inputs
* Return safe error responses only

---

## Dependency Injection

Use DI for:

* repositories
* service classes
* external clients
* config providers
* caches
* message brokers
* policy engines

Prefer explicit injection over hidden globals or implicit singletons.

---

## Authentication and Authorisation

* Enforce auth in backend dependencies
* Enforce RBAC at route or service layer
* Test permission boundaries explicitly
* Never rely on frontend enforcement

---

## Circuit Breakers

Required when calling:

* third-party APIs
* rate-limited APIs
* flaky internal services
* slow network dependencies
* AI, OCR, geocoding, or enrichment providers

Must define:

* failure threshold
* reset timeout
* fallback behaviour
* logging behaviour

---

## Retries and Timeouts

Retries must be:

* bounded
* backoff-based
* idempotent-aware

External calls must have:

* connect timeout
* read timeout
* total timeout where practical

Do not retry blindly.

---

## Queue and Worker Safety

For async workers:

* task time limits required
* retries bounded
* poison-message behaviour defined
* concurrency chosen based on memory reality
* prefetch tuned deliberately
* late ack only when appropriate

---

## Healthchecks

Backend services should expose:

* liveness
* readiness
* dependency health where appropriate

Health endpoints must not claim healthy if critical dependencies are unavailable.

---

## Data Safety

* Migrations must be reversible where possible
* Destructive migrations require explicit approval
* Schema changes must consider zero-downtime rollout
* Use parameterised queries only

---

## Observability

* structured logs
* actionable errors
* correlation IDs where relevant
* clear startup failure messages
* dependency failure visibility

---

## Security Expectations

* strict schema validation
* no hardcoded secrets
* no sensitive data leakage
* auth bypass tests mandatory for protected routes
* file uploads validated and constrained
