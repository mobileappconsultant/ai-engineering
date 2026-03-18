# TEST_STRATEGY

Testing is mandatory.

## Test Pyramid

1. Unit tests
2. Integration tests
3. Regression tests
4. End-to-end tests where justified

## Unit Tests
Required for:
- business rules
- scoring logic
- validation
- utility functions
- policy decisions
- state transitions

Rules:
- fast
- isolated
- deterministic
- no network
- no real DB unless explicitly intended

## Integration Tests
Required for:
- API endpoints
- DB persistence flows
- queue interactions
- auth/RBAC
- repository behavior
- DI wiring

## Bug Fix Rule (MANDATORY)

Every bug fix must:

1. Create a failing test that reproduces the bug
2. Implement fix
3. Pass test
4. Add regression coverage

If step 1 is missing:
STOP immediately.

## Regression Tests
Required when:
- fixing a bug
- changing existing logic
- refactoring critical code
- changing API behavior
- modifying security, concurrency, or async workflows

Rule:
Every bug fix must add a regression test.

## TDD Workflow

Red → Green → Refactor

The Builder must:
1. write failing tests first
2. confirm failure
3. implement minimal change
4. refactor safely

## Regression Enforcement

Every bug fix MUST include:
- a failing test that reproduces the issue
- a passing test after fix

If missing:
STOP the workflow.

## Coverage
Target:
- 90% for core modules
- lower for non-critical edges only with justification
