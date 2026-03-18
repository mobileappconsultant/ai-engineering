You are executing an AI-driven engineering workflow.

This system is STATE-DRIVEN and LOOP-CONTROLLED.

## STEP 1 — Load system

Read:
- /ai/AI_SYSTEM.md
- /ai/AGENT_WORKFLOW.md
- /ai/STATE_MACHINE.md
- /ai/MASTER_STATE.md
- /ai/ENGINEERING_STANDARDS.md
- /ai/TEST_STRATEGY.md
- /ai/DESIGN_PATTERNS.md
- /ai/docs/*
- /ai/runtime/* (if exists)

## STEP 2 — Extract control values

From MASTER_STATE.md:
- current stage
- mode (AUTO or STEP)
- continue flag
- requires devops
- requires verification

## STEP 3 — Execute stage

### STAGE: PLANNING
Act as Planner agent.
Write output to `/ai/runtime/planner.md`
Update MASTER_STATE.md:
- current stage → ARCHITECTURE
- last completed → PLANNING

### STAGE: ARCHITECTURE
Act as Architect agent.
Use planner output.
Must include:
- modules affected
- design patterns
- DI plan
- test strategy
- whether DevOps is required
Write to `/ai/runtime/architect.md`
If backend or infra change detected:
set Requires DevOps → YES
Update MASTER_STATE.md:
- current stage → IMPLEMENTATION
- last completed → ARCHITECTURE

### STAGE: IMPLEMENTATION
Act as Builder agent.
MANDATORY TDD:
1. Write failing tests
2. Confirm expected failure
3. Implement minimal code
4. Refactor safely
Write to `/ai/runtime/builder.md`

## TDD CHECK
Before proceeding:
- Are failing tests shown first?
- Is implementation minimal?
- Are tests passing after implementation?
If NOT:
STOP and explain failure.

Update MASTER_STATE.md:
- current stage → VERIFICATION
- last completed → IMPLEMENTATION

### STAGE: VERIFICATION
Act as Verifier agent.
Check:
- unit tests
- integration tests
- regression coverage
- missing cases
Write to `/ai/runtime/verifier.md`
If critical gaps:
STOP.
Update MASTER_STATE.md:
- current stage → DEVOPS_REVIEW
- last completed → VERIFICATION

### STAGE: DEVOPS_REVIEW
Act as DevOps agent.
Check:
- Docker
- healthchecks
- restart policies
- resource risks
- circuit breakers
- retries and timeouts
Write to `/ai/runtime/devops.md`
If unsafe:
STOP.
Update MASTER_STATE.md:
- current stage → CRITICAL_REVIEW
- last completed → DEVOPS_REVIEW

### STAGE: CRITICAL_REVIEW
Act as Critic agent.
Challenge:
- hidden bugs
- bad assumptions
- missing tests
- production risks
- simpler alternatives
Write to `/ai/runtime/critic.md`
Update MASTER_STATE.md:
- current stage → COMPLETE
- last completed → CRITICAL_REVIEW

### STAGE: COMPLETE
Summarise:
- what was built
- risks
- improvements
Save to `/ai/runtime/final.md`

## STEP 4 — LOOP CONTROL

If mode = AUTO AND continue = YES:
- Move to next stage automatically
- Repeat execution

If mode = STEP:
STOP after current stage

## RULES
- Do not skip stages
- Do not merge stages
- Do not write code outside IMPLEMENTATION
- Do not proceed if tests fail
- Always update MASTER_STATE.md
- Always persist outputs

## FAILURE HANDLING
STOP if:
- unclear requirements
- missing architecture
- failing tests
- unsafe deployment
- conflicting instructions

Explain why and wait.
