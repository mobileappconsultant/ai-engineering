# CHANGE_CONTROL

This document defines the mandatory process for introducing changes to the system.
It prevents uncontrolled architectural drift and ensures that all modifications remain deliberate, reviewable, and production-safe.

## Scope

Change control applies to:
- architecture changes
- database schema changes
- API contract changes
- infrastructure configuration
- security mechanisms
- core domain logic

Routine internal refactoring or small bug fixes may bypass full change control, but must still follow coding standards and testing rules.

## Change Categories

### Minor Change
Small modifications that do not alter architecture or public behaviour.

Examples:
- bug fixes
- small performance improvements
- additional validation logic
- internal refactoring with no behaviour change

Minor changes require:
- failing tests first (TDD)
- passing regression tests
- minimal patch output

### Major Change
Changes that affect system behaviour, architecture, or public interfaces.

Examples:
- new modules or services
- database schema updates
- API contract modifications
- cross-module refactors
- infrastructure or deployment changes

Major changes require a formal proposal.

## Change Proposal Process

Before implementing a major change, the AI must produce a proposal containing:
1. Change Summary
2. Motivation
3. Impact Analysis
4. Risks
5. Alternatives Considered
6. Implementation Plan
7. Test Strategy

Implementation must not begin until the proposal is reviewed and accepted.

## Architectural Protection

The following areas must not be modified without explicit approval:
- authentication logic
- database schema migrations
- infrastructure configuration
- deployment workflows
- security mechanisms

## Backwards Compatibility

Changes must preserve backwards compatibility whenever possible.

Rules:
- existing APIs must not break without versioning
- database migrations must be reversible
- configuration changes must be deployable safely

## Testing Requirements

All changes must include tests.

Requirements:
- new tests for new functionality
- regression tests for affected modules
- full test suite must pass before merging

## Documentation Updates

When a change affects architecture or behaviour, update:
- /ai/MASTER_STATE.md
- /ai/docs/SYSTEM_ARCHITECTURE.md
- /ai/docs/API_MAP.md
- /ai/docs/DATA_MODEL.md

## Patch Discipline

- produce unified git diffs
- modify only necessary files
- avoid unrelated refactoring

## Mandatory Workflow Enforcement

All changes must pass through:

Planner → Architect → Builder → Verifier → DevOps → Critic

Exceptions require explicit human approval.

Skipping stages is prohibited for:
- backend changes
- infra changes
- auth/security changes
- data model changes
- deployment changes
