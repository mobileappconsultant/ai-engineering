# AI Engineering System Template

Portable AI-governed engineering workflow for VS Code + Claude.

## Purpose

This template installs a disciplined AI SDLC system into any repository.

Supported project types:
- backend
- frontend
- mobile
- fullstack

Primary workflow:
Planner → Architect → Builder → Verifier → DevOps → Critic

## Install into a target repo

From the template repo root:

```bash
bash bootstrap.sh
```

Or copy the `/ai`, `/.claude`, `/.githooks`, and `/scripts` folders into a target project.

Then in the target project:

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
chmod +x .githooks/post-commit
chmod +x scripts/*.sh
```

## Use in Claude VS Code

Run:

```text
/auto
```

The system reads `/ai`, decides the current stage from `/ai/MASTER_STATE.md`, executes the correct agent, writes outputs to `/ai/runtime`, and updates state.

## Notes

- This is semi-autonomous, not magic.
- Human review is still required.
- For real enforcement, pair this with tests, git hooks, and CI.
