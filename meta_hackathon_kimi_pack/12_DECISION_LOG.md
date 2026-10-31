# Vordenk Decision Log

Keep this file short. Each important decision should include context, alternatives, consequences, and a status. A decision is not final until the founder approves it.

## Status values

- `PROPOSED` — suggested by Kimi/founder, not yet agreed.
- `ACCEPTED` — founder approved and implementation should follow it.
- `REJECTED` — considered and rejected; record why to avoid repeating debate.
- `SUPERSEDED` — once accepted but replaced; link to replacement.

## Entry template

```markdown
## D-XXX — [Short title]
- Status: PROPOSED / ACCEPTED / REJECTED / SUPERSEDED
- Date:
- Context/problem:
- Options considered:
- Decision:
- Rationale and trade-offs:
- Consequences/risks:
- How we will validate it:
- Revisit trigger:
```

## Seed decisions to validate

### D-001 — Product wedge
- Status: PROPOSED
- Context: Full Vordenk covers enterprise transformation end to end, but the hackathon build window is short.
- Decision: Build Vordenk Discovery Intelligence as one slice of the wider Transformation OS.
- Rationale: A complete discover → reason → visualise → validate → persist loop is more credible than a fragmented platform.
- Validate: Can the demo show evidence-backed cross-session improvement in under three minutes?

### D-002 — Meta-model path
- Status: PROPOSED
- Context: Meta model integration is a baseline competition requirement.
- Decision: Use Meta Model API for Muse Spark as the core reasoning model; use Muse Voice Transcribe if audio input can be delivered safely in time.
- Rationale: Direct and visible Meta model use; avoids depending on unconfirmed partner credits.
- Validate: Complete a minimal real call and show model output in the app.

### D-003 — Canonical process visual
- Status: PROPOSED
- Context: Generated images alone are difficult to edit, validate, and trace.
- Decision: Store a structured process model and render it through a diagram library; generated imagery is optional and illustrative only.
- Validate: A human edit changes the diagram from structured data and survives reload.

### D-004 — Hackathon scope
- Status: PROPOSED
- Context: The long-term product extends through design, delivery, and value realisation.
- Decision: Keep those as architecture-compatible future phases; do not attempt to build all of them during this hackathon.
- Validate: The MVP output should be reusable for later requirements and delivery workflows.

Add accepted decisions only after founder approval. Kimi should suggest updates, not silently rewrite these statuses.
