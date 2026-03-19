# SECURITY_STANDARDS

This document defines mandatory security practices for any AI agent or developer working on this repository.

Security is a blocking requirement, not an optional improvement.

---

## Threat Model

Assume:

* hostile clients
* malicious users
* leaked credentials
* replay attempts
* brute-force attempts
* compromised upstream services
* prompt injection where AI features exist

Never assume trust.

---

## Input Validation

* Validate all inputs at system boundaries
* Reject unexpected fields
* Reject malformed data
* Enforce strict schemas
* Apply length, type, range, and format checks

Never trust:

* request bodies
* query parameters
* headers
* cookies
* uploaded files
* webhook payloads

---

## Authentication

* All protected endpoints must require authentication
* Tokens must be validated for signature, expiry, issuer, and audience where applicable
* Refresh token flows must be explicit and controlled
* Token scopes or roles must be enforced server-side

Never trust client-side role checks.

---

## Authorisation

* Enforce RBAC or permission checks at the backend
* Every sensitive route must explicitly verify role/permission
* Object-level access must be checked, not assumed

Examples:

* users can only access their own records unless elevated role permits otherwise
* admin routes must never be inferred from UI state

---

## Secrets Management

* No secrets in source code
* No secrets in Docker images
* No secrets in logs
* No secrets in client-visible responses
* Use environment variables or secret managers only

---

## Injection Protection

Prevent and test for:

* SQL injection
* command injection
* path traversal
* prompt injection
* template injection
* unsafe deserialisation

Use parameterised queries and safe APIs only.

---

## File Upload Safety

* Validate MIME type and extension
* Enforce file size limits
* Reject executable or dangerous formats unless explicitly required
* Store uploads outside executable paths
* Never trust original filenames
* Scan or quarantine sensitive uploads where appropriate

---

## External Service Safety

All external calls must include:

* connection timeout
* read timeout
* bounded retries
* circuit breaker where failure risk is meaningful
* fallback behaviour where appropriate

No unbounded waits.

---

## Rate Limiting and Abuse Protection

Apply rate limiting to:

* login
* registration
* password reset
* public APIs
* expensive endpoints
* AI or OCR endpoints
* upload endpoints

Protect against brute force, scraping, and queue abuse.

---

## Logging and Monitoring

* Log security-relevant failures
* Log auth failures
* Log suspicious patterns
* Never log secrets, tokens, passwords, or full sensitive payloads

Security logs must be useful without leaking private data.

---

## Error Handling

* Return safe error messages to clients
* Do not expose stack traces, SQL details, internal URLs, or secret values
* Detailed errors belong in logs, not responses

---

## Security Testing

All relevant changes must include:

* invalid input tests
* auth bypass tests
* permission tests
* injection-resistance tests
* rate-limit or abuse-path consideration
* regression tests for previous vulnerabilities

---

## Failure Policy

If security requirements are unclear:
STOP.

If an insecure implementation is detected:
STOP and fix security before proceeding.

Security issues override convenience and speed.
