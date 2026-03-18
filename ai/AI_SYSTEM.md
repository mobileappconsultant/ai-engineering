# AI_SYSTEM

This repository uses a governed AI engineering workflow.

All work must follow the defined workflow and role boundaries.

## Workflow

Planner → Architect → Builder → Verifier → DevOps → Critic

## Operating Rules

1. Read all files in `/ai` before doing any work.
2. Determine the project type from `/ai/PROJECT_TYPE.md`.
3. Determine the current lifecycle state from `/ai/MASTER_STATE.md`.
4. Declare:
   - Current Stage
   - Responsible Agent
   - Next Stage
5. Follow the responsibilities of the current agent only.
6. Do not mix roles.
7. Engineering rules in `ENGINEERING_STANDARDS.md` are mandatory.
8. Change control rules in `CHANGE_CONTROL.md` are mandatory.
9. Deployment safety rules in `DEPLOYMENT_STANDARDS.md` are mandatory for infrastructure or backend changes.
10. If instructions conflict, precedence is:
   - ENGINEERING_STANDARDS.md
   - CHANGE_CONTROL.md
   - PROJECT_TYPE.md
   - agent role file

## Autonomous Execution Rules

- Never execute more than one stage without validating outputs.
- Stop immediately if uncertainty is detected.
- Prefer stopping over guessing.
- Do not fabricate tests, results, metrics, or runtime status.
- Do not write code outside the IMPLEMENTATION stage.
- Do not skip stages.

## Required Session Bootstrap

Before performing any work, read:

- /ai/AI_SYSTEM.md
- /ai/PROJECT_TYPE.md
- /ai/STATE_MACHINE.md
- /ai/MASTER_STATE.md
- /ai/ENGINEERING_STANDARDS.md
- /ai/CHANGE_CONTROL.md
- /ai/TEST_STRATEGY.md
- /ai/DESIGN_PATTERNS.md
- project-type-specific standards file
- /ai/docs/*

Then summarise:
- system purpose
- current project state
- active work
- constraints
- current agent stage

Do not write code until the correct stage is reached.
