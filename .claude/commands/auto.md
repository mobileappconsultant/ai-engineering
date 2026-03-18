You are executing a state-driven AI engineering workflow.

---

# STEP 1 — LOAD CONTEXT (MANDATORY)

Read:

* /ai/master.md
* /ai/MASTER_STATE.md
* /ai/ENGINEERING_STANDARDS.md
* /ai/TEST_STRATEGY.md
* /ai/DESIGN_PATTERNS.md
* /ai/STATE_MACHINE.md
* /ai/docs/* (if exists)
* /ai/runtime/* (if exists)

---

# STEP 2 — VALIDATE SYSTEM

## Validate master.md

Must contain:

* Architecture section
* Design principles
* Testing rules

## Validate MASTER_STATE.md

Must contain:

* Current Stage
* Mode
* Continue flag

If validation fails:
STOP and repair.

---

# STEP 3 — EXECUTE CURRENT STAGE

---

## STAGE: PLANNING

Act as Product Manager.

Output:

* problem
* user story
* acceptance criteria
* constraints
* edge cases

Save to:
`/ai/runtime/planner.md`

Update state → ARCHITECTURE

---

## STAGE: ARCHITECTURE

Act as Architect.

Include:

* modules affected
* design patterns
* dependency injection plan
* test strategy
* devops requirement

Save to:
`/ai/runtime/architect.md`

If backend or infra change:
Requires DevOps → YES

Update state → IMPLEMENTATION

---

## STAGE: IMPLEMENTATION

Act as Builder.

## STRICT TDD

1. Write failing tests
2. Show failure
3. Implement minimal code
4. Refactor

Save to:
`/ai/runtime/builder.md`

---

## TDD VALIDATION

If failing tests are NOT shown first:
STOP.

If tests do not pass after implementation:
STOP.

---

Update state → VERIFICATION

---

## STAGE: VERIFICATION

Act as Tester.

Check:

* unit tests
* integration tests
* regression coverage

Save to:
`/ai/runtime/verifier.md`

If gaps found:
STOP.

Update state → DEVOPS_REVIEW

---

## STAGE: DEVOPS_REVIEW

Act as DevOps Engineer.

Check:

* Docker stability
* health checks
* restart policies
* resource limits
* circuit breakers
* retries/timeouts

Save to:
`/ai/runtime/devops.md`

If unsafe:
STOP.

Update state → CRITICAL_REVIEW

---

## STAGE: CRITICAL_REVIEW

Act as Critic.

Challenge:

* hidden bugs
* bad assumptions
* missing tests
* simpler alternatives

Save to:
`/ai/runtime/critic.md`

Update state → COMPLETE

---

## STAGE: COMPLETE

Summarise outcome.

Save to:
`/ai/runtime/final.md`

---

# STEP 4 — LOOP CONTROL

If Mode = AUTO and Continue = YES:
Proceed to next stage automatically.

If Mode = STEP:
STOP.

---

# RULES

* Do not skip stages
* Do not write code outside IMPLEMENTATION
* Do not proceed if tests fail
* Always update MASTER_STATE.md
* Always persist outputs
