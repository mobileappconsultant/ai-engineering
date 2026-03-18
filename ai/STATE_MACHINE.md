# STATE_MACHINE

Allowed workflow states:

1. PLANNING
2. ARCHITECTURE
3. IMPLEMENTATION
4. VERIFICATION
5. DEVOPS_REVIEW
6. CRITICAL_REVIEW
7. COMPLETE

## Valid Transitions

PLANNING → ARCHITECTURE
ARCHITECTURE → IMPLEMENTATION
IMPLEMENTATION → VERIFICATION
VERIFICATION → DEVOPS_REVIEW
VERIFICATION → CRITICAL_REVIEW
DEVOPS_REVIEW → CRITICAL_REVIEW
CRITICAL_REVIEW → COMPLETE

## Rules

- Builder cannot run before Architect output exists.
- Implementation cannot start before tests are defined.
- DevOps review is required for backend, deployment, infrastructure, queue, cache, DB, Docker, reverse proxy, or CI/CD changes.
- Critic performs the final adversarial pass.
