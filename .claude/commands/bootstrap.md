You are bootstrapping and initialising the AI engineering system.

This step prepares the environment AND loads system context.

---

# STEP 1 — VALIDATE STRUCTURE

Ensure the following directories exist:

* /ai
* /ai/docs
* /ai/runtime

If missing:
Create them.

---

# STEP 2 — VALIDATE CORE FILES

Ensure the following files exist:

* /ai/master.md
* /ai/MASTER_STATE.md

If missing:
Create default versions with valid structure.

---

# STEP 3 — LOAD GOVERNANCE LAYER (MANDATORY)

Read and internalise ALL of the following:

* /ai/AI_SYSTEM.md
* /ai/PROJECT_TYPE.md
* /ai/STATE_MACHINE.md
* /ai/master.md
* /ai/MASTER_STATE.md
* /ai/ENGINEERING_STANDARDS.md
* /ai/CHANGE_CONTROL.md
* /ai/TEST_STRATEGY.md
* /ai/DESIGN_PATTERNS.md
* project-type-specific standards (if defined)
* /ai/docs/* (if exists)

---

# STEP 4 — VALIDATE SYSTEM STATE

Extract from MASTER_STATE.md:

* current stage
* mode
* continue flag

Ensure:

* current stage is valid
* mode is AUTO or STEP
* continue flag exists

If invalid:
Repair before proceeding.

---

# STEP 5 — GENERATE DOCUMENTATION

If Python is available:

Run:
python ai/generate_docs.py

Ensure the following files exist:

* /ai/docs/SYSTEM_ARCHITECTURE.md
* /ai/docs/API_MAP.md
* /ai/docs/DATA_MODEL.md
* /ai/docs/MODULE_GRAPH.md

If generation fails:
STOP and report error.

---

# STEP 6 — SYSTEM SUMMARY OUTPUT

Output the following:

1. Current Stage
2. Current Project Type
3. Active Constraints (from master.md + standards)
4. Next Required Agent (based on stage)
5. Summary of System Architecture (from docs)

---

# STEP 7 — FINAL VALIDATION

Confirm:

* required directories exist
* required files exist
* system state is valid
* documentation is present

---

# RULES

* Do not write code
* Do not skip validation steps
* Do not assume missing files
* Prefer stopping over guessing

---

# OUTPUT FORMAT

## System Initialisation Report

* Structure Status
* Core Files Status
* Documentation Status
* Current Stage
* Project Type
* Next Agent
* Constraints Summary
* Architecture Summary

---

STOP after output.
