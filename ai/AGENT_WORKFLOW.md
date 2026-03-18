# AGENT_WORKFLOW

All development follows this mandatory sequence:

1. Planner
2. Architect
3. Builder
4. Verifier
5. DevOps
6. Critic

## Planner
Responsible for:
- problem statement
- user story
- acceptance criteria
- constraints
- edge cases
- success metrics
- non-goals

No technical design.

## Architect
Responsible for:
- technical design
- module boundaries
- API and data changes
- design pattern selection
- dependency flow
- dependency injection plan
- test strategy
- rollout impact
- risks and alternatives

No code.

## Builder
Responsible for:
- TDD implementation
- failing tests first
- minimal implementation
- safe refactor
- patch output only

No architecture changes.

## Verifier
Responsible for:
- unit test sufficiency
- integration test sufficiency
- regression coverage
- contract correctness
- logical correctness

No new features.

## DevOps
Responsible for:
- Docker and runtime safety
- healthchecks
- restart policy
- resource limits
- rollback safety
- migration safety
- reverse proxy safety
- queue, worker, timeout, retry, and circuit-breaker suitability where relevant

## Critic
Responsible for:
- adversarial review
- identifying blind spots
- hidden coupling
- overengineering
- untested assumptions
- production failure modes

## Rules
- Each stage consumes the artifact from the previous stage.
- No role may override another role’s responsibility.
- Architecture decisions must not be made during coding.
- Tests must be written before implementation.
