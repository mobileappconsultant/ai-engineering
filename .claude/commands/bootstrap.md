You are bootstrapping and initialising the AI engineering system.

## STEP 1 — VALIDATE STRUCTURE

Ensure directories exist:

* /ai
* /ai/docs
* /ai/runtime

Create missing directories.

---

## STEP 2 — VALIDATE CORE FILES

Ensure files exist:

* /ai/master.md
* /ai/MASTER_STATE.md
* /ai/AI_SYSTEM.md
* /ai/ENGINEERING_STANDARDS.md
* /ai/CHANGE_CONTROL.md
* /ai/TEST_STRATEGY.md
* /ai/DESIGN_PATTERNS.md
* /ai/SECURITY_STANDARDS.md

If missing:
create or restore sensible defaults.

---

## STEP 3 — LOAD GOVERNANCE LAYER

Read and internalise:

* /ai/AI_SYSTEM.md
* /ai/PROJECT_TYPE.md
* /ai/STATE_MACHINE.md
* /ai/master.md
* /ai/MASTER_STATE.md
* /ai/ENGINEERING_STANDARDS.md
* /ai/CHANGE_CONTROL.md
* /ai/TEST_STRATEGY.md
* /ai/DESIGN_PATTERNS.md
* /ai/SECURITY_STANDARDS.md
* project-type-specific standards
* /ai/docs/*

---

## STEP 4 — VALIDATE SYSTEM STATE

Extract from MASTER_STATE.md:

* current stage
* mode
* continue flag

Ensure:

* current stage valid
* mode is AUTO or STEP
* continue flag exists

If invalid:
repair before proceeding.

---

## STEP 5 — GENERATE DOCS

If Python available:

Run:
python ai/generate_docs.py

Ensure generated:

* /ai/docs/SYSTEM_ARCHITECTURE.md
* /ai/docs/API_MAP.md
* /ai/docs/DATA_MODEL.md
* /ai/docs/MODULE_GRAPH.md

If generation fails:
STOP and report.

---

## STEP 6 — OUTPUT SYSTEM SUMMARY

Output:

1. Current Stage
2. Current Project Type
3. Active Constraints
4. Next Required Agent
5. Summary of System Architecture
6. Security Readiness Notes

---

## RULES

* Do not write code
* Do not skip validation
* Prefer stopping over guessing

STOP after output.
