# DESIGN_PATTERNS

Use patterns deliberately, not decoratively.

## Approved Patterns

### Strategy
Use when multiple algorithms or providers can be swapped.

### Factory
Use when object construction varies by type, environment, or provider.

### Dependency Injection
Use for:
- service wiring
- repositories
- external clients
- policy engines

Prefer constructor injection or framework-native DI.

### Repository
Use to isolate persistence concerns from business logic.

### Adapter
Use to wrap external systems behind stable internal interfaces.

### Builder
Use when constructing complex objects with optional configuration.

### Observer / Event-Driven
Use for domain events, notifications, async workflows.

### Circuit Breaker
Required for backend services that call unstable or rate-limited external systems.

## Anti-Patterns

- God services
- Fat controllers
- business logic in route handlers
- hardcoded dependencies
- direct external API calls from UI layers
- shared mutable global state
- hidden retry loops

## Rules
- Prefer the simplest pattern that solves the problem.
- Do not introduce patterns without explaining why.
- The Architect must justify pattern selection before implementation.
