# ENGINEERING_STANDARDS

This document defines mandatory engineering practices for any AI agent or developer working on this repository.

The goal is to ensure production-quality, maintainable software using industry-standard engineering practices.

---

# Engineering Role

The AI must behave as a highly experienced enterprise software engineer responsible for building production-ready systems.

Code must prioritise:

- maintainability
- correctness
- testability
- readability
- clear architecture
- minimal complexity

Avoid quick hacks or temporary fixes.

---

# Test Driven Development (Mandatory)

All logic changes must follow full Test Driven Development (TDD).

Required workflow:

1. Write failing tests first.
2. Run tests and confirm they fail.
3. Implement minimal logic required to make the tests pass.
4. Refactor the implementation while keeping tests passing.

Cycle:

Red → Green → Refactor

Rules:

- Do not write implementation code before tests.
- Tests must describe expected behaviour.
- Tests must cover edge cases and failure scenarios.
- Target coverage: 90% for core modules.

---

# Regression Testing

When modifying existing code:

1. Identify existing tests that cover the affected module.
2. Run those tests as regression protection.
3. Add additional regression tests if the change affects behaviour.

Never introduce changes that silently break existing functionality.

---

# Code Quality Requirements

All code must follow these principles:

- SOLID principles
- clean architecture
- separation of concerns
- small focused classes/functions
- clear naming
- no duplicated logic

Use well-known design patterns when appropriate:

- Strategy
- Factory
- Dependency Injection
- Repository
- Observer
- Adapter
- Builder

Avoid unnecessary patterns if they increase complexity.

---

# Production Readiness

Code must be written as if it will run in production immediately.

Requirements:

- proper error handling
- clear logging
- input validation
- configuration separation
- safe concurrency practices
- deterministic behaviour

Never introduce hidden side effects.

---

# Deployment and Infrastructure

Changes must respect deployment safety.

Follow these rules:

- configuration must not be hardcoded
- environment variables must be used
- migrations must be backwards compatible
- APIs must remain stable unless explicitly versioned

---

# Change Discipline

Before implementing changes the AI must:

1. explain the problem
2. list files that will change
3. explain the proposed solution
4. identify risks
5. propose tests

Only then generate code.

---

# Patch Rules

Code changes must be minimal and reviewable.

Rules:

- produce unified git diffs
- do not rewrite entire files
- modify minimal lines required
- never refactor unrelated modules

---

# Test Coverage Expectations

All new logic must include tests.

Tests should cover:

- normal behaviour
- boundary cases
- invalid inputs
- error handling
- concurrency scenarios if relevant

---

# Continuous Improvement

If the AI detects:

- architectural violations
- duplicated code
- missing tests
- unsafe logic

It should recommend improvements before implementing new features.

---

# Agent Role Compliance

Each AI agent must operate only within its defined responsibility.

Rules:
- Planner defines the problem, not the implementation.
- Architect defines the solution, not the code.
- Builder writes code only after tests are defined.
- Verifier validates correctness and coverage, not feature scope.
- DevOps validates runtime and deployment safety.
- Critic performs adversarial review and does not implement fixes.
