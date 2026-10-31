# Beginner-Friendly Architecture

## Architecture goal

Build the smallest coherent system that can demonstrate the complete hackathon loop. Prefer a **modular monolith** over microservices: one app, clear modules, one system of record, and a small number of reliable AI calls.

## Suggested system shape

```text
Browser UI
  ├─ Engagement + session workspace
  ├─ Transcript/artifact input
  ├─ Evidence and review panel
  └─ Editable process diagram
          │
          ▼
Server-side application API
  ├─ Session ingestion and validation
  ├─ Meta Model client (server-side only)
  ├─ Structured output schema validation
  ├─ Discovery synthesis and question ranking
  └─ Human review/status-change endpoints
          │
          ├── Meta Muse Voice Transcribe (audio, if implemented)
          ├── Meta Muse Spark (structured reasoning/synthesis)
          ▼
Database / storage
  ├─ Engagements
  ├─ Sessions and transcript chunks
  ├─ Evidence-linked knowledge objects
  ├─ Decisions and user corrections
  └─ Versioned process models and checkpoint runs
```

## Stack decision rule

Do not pick technologies because they sound impressive. First ask Kimi to check what you already know, your current machine/repository, deployment target, and how quickly each option can deliver the MVP. Then choose and record one stack for the hackathon.

Reasonable default to evaluate for a solo hackathon builder:
- A full-stack web framework (for example, Next.js + TypeScript) to avoid running many services.
- A relational database such as PostgreSQL, optionally hosted by a managed service if the setup is faster and privacy requirements fit.
- A validated schema library for AI output and API inputs.
- A diagram renderer such as Mermaid or a graph library. Generate diagram source from validated structured process data.
- Server-side Meta API calls only.
- Simple styling and a polished interface; don't overinvest in design systems.

If your skills or current repo make Python + FastAPI and a small React frontend materially easier, compare it explicitly before committing. Do not build two stacks or restart the repo repeatedly.

## Suggested modules (names are conceptual, not existing paths)

- `sessions`: engagement/session creation, transcript ingestion, timeline.
- `model_gateway`: one server-side interface for Meta model calls.
- `extraction`: schema, structured object validation, evidence references.
- `transformation_memory`: store/retrieve facts, processes, questions, decisions and versions.
- `discovery`: contradiction checks and question prioritisation.
- `visualisation`: structured process model to editable diagram.
- `review`: validate/edit/reject/defer and audit the action.
- `evaluation`: seeded examples and quality measurements.

Do not create all modules upfront just to match this list. Create modules when the implementation benefits from them.

## Data flow for one checkpoint

1. Receive transcript chunk(s) and optional approved artifact(s).
2. Store raw input metadata and stable source IDs.
3. Fetch only relevant prior project objects and unresolved questions.
4. Send the bounded context plus explicit output schema to Muse Spark.
5. Validate output fields, references, types, and constraints.
6. Store proposed extracted/inferred objects and a checkpoint version.
7. Detect known contradictions where possible using deterministic checks plus model proposals.
8. Render diagram and discovery summary.
9. Consultant validates/edits/rejects items.
10. Persist review status and history so the next session can use it.

## Avoid premature complexity

Do not add a vector database, LangGraph, message broker, Redis, Kubernetes, multi-agent framework, or custom graph DB until an observable requirement justifies it. Semantic search may become useful later, but the MVP needs reliable structured memory and source linkage more than a complex retrieval stack.

## Error handling

- API unavailable: show a useful message, preserve input, and offer retry.
- Model returns malformed output: validate, log redacted diagnostics, and retry at most a bounded number of times.
- Citation/source ID missing: mark the item unsupported or reject it, not silently accept it.
- User edits an item: create a new version/audit entry; do not overwrite its past without history.
- Partial session: store checkpoints and recover after refresh or network failure.
- Never display a fabricated successful result when inference failed.
