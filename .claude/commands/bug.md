You are initiating a bug fix workflow.

---

# INPUT REQUIRED

User must provide:

* bug description
* expected behaviour
* actual behaviour
* reproduction steps (if available)

---

# STEP 1 — UPDATE STATE

Update /ai/MASTER_STATE.md:

* Current Task → Fix bug: <description>
* Current Stage → PLANNING
* Continue → YES

---

# STEP 2 — ENFORCE TEST-FIRST

Ensure:

* a failing test MUST be created to reproduce the bug
* no fix is allowed without this test

---

# STEP 3 — EXECUTE WORKFLOW

Run:

/auto

---

# RULES

* Do not fix without failing test
* Do not skip regression tests
* Do not assume root cause without validation
