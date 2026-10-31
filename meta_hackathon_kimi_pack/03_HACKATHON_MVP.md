# Vordenk Discovery Intelligence — Hackathon MVP

## Name for the demo

**Vordenk Discovery Intelligence: From Workshop Evidence to a Living Transformation Blueprint**

This is one newly built capability inside the long-term Vordenk Enterprise Transformation OS. It is more than an AI co-consultant: it creates reusable, source-linked business understanding and a structured artifact that later phases can use.

## Target demo scenario

Use a wholly synthetic enterprise engineering-change workshop. For example, stakeholders describe how an engineering change request moves through impact assessment, approvals, and BOM updates. Provide a second synthetic session or artifact that contradicts or clarifies a detail (e.g. who approves a production-impacting change). This lets the demo show memory and contradiction handling instead of just summarisation.

Do not use confidential real Accenture or client material.

## Must-have end-to-end flow

1. **Create an engagement** with a name, goal, and scope.
2. **Ingest workshop evidence:** paste/upload transcript text. If feasible, also transcribe a consented synthetic/demo audio clip with Meta Muse Voice Transcribe. If time allows, accept an authorised workshop photo/slide/document and analyse it with Meta's multimodal model path.
3. **Extract structured knowledge using Muse Spark:** process steps, actors, systems, business rules, issues, metrics, decisions, questions, and source spans. Validate the response against a schema.
4. **Create evidence-linked objects:** every important claim stores its source session and excerpt or timestamp when available, plus its current status.
5. **Build a Discovery Intelligence checkpoint:** current understanding, prioritised unanswered questions, assumptions, conflicts/contradictions, risks/dependencies, and proposed next steps.
6. **Render a real editable diagram** from structured process data (for example Mermaid or a graph renderer). Do not use a generated picture as the canonical process model.
7. **Human review:** user can validate, edit, reject, or defer a material item. Store who/when/status and retain history.
8. **Cross-session memory:** add a second transcript with conflicting information. The application flags the disagreement and updates the proposed blueprint only after user review.
9. **Show the Meta path:** visibly and honestly indicate which Meta models powered transcription/reasoning. Include model name and latency/usage only if measured in the actual run.

## If time is limited: scope order

**P0 — mandatory**
- Functional web UI and persistent engagement/session structure.
- Transcript paste/upload.
- Real Meta Model API inference using a Meta model.
- Structured extraction with evidence/source snippets.
- Questions plus at least one non-trivial gap or conflict.
- Editable process diagram or equivalent structured visual.
- Human correction/status change.
- Persist and demonstrate a second session changing the understanding.
- Public GitHub repo, setup instructions, and three-minute video.

**P1 — high value if P0 works**
- Audio-file transcription with Meta Muse Voice Transcribe.
- Browser mic/streaming transcription if the official real-time API and browser/server flow work reliably.
- Upload a synthetic process image or slide and cross-reference it with transcript context via Muse Spark multimodal input.
- A small evaluation panel showing evidence coverage, unresolved conflicts, and generation latency.

**P2 — optional stretch only**
- Muse Image for a clearly labelled illustrative TO-BE concept visual, not as source of truth.
- SAM 3.1 only if a real segmentation need arises and its output is relevant to the user's workflow.
- Hosted Muse Spark Open through Baseten, Modal, or Fireworks if access/credits are available and integration is faster than or adds value beyond direct Model API.
- Login, multi-tenant production features, Azure DevOps write integration, full backlog generation, complex multi-agent orchestration.

## Do not build during the hackathon

- The full seven-stage transformation OS.
- Long-running, eight-hour live workshop orchestration.
- Many loosely coordinated agents.
- A custom graph database before Postgres/structured records prove insufficient.
- Automatic writes to customer work systems.
- Unverified claims that the product saves money or improves consulting outcomes.
- A generic chat screen that merely answers questions over documents.

## What makes the MVP distinct

Its core unit is not a note or answer. It is an **evidence-linked transformation object** that survives across sessions, has explicit validation status, can create a process model, and can trigger a decision-relevant follow-up question. The product demonstrates a loop: new evidence changes understanding; human correction changes the canonical project model; the next synthesis respects that history.

## Hackathon-specific success measures

Set targets before evaluating and report actual values, never invented results. Candidate measurements:
- Material claims with valid source links.
- Correctness/completeness of process steps against a human-reviewed reference.
- Number of seeded contradictions correctly surfaced.
- Fraction of generated questions rated useful by a reviewer.
- Whether edits survive a reload and influence the next session's synthesis.
- End-to-end latency and actual model/provider usage.
