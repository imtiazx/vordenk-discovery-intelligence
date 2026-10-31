# Evaluation, Privacy, Security, and Reliability

## Why this file matters

Vordenk handles potentially sensitive client conversations. For the hackathon, use only synthetic, public, or explicitly authorised data. The demo scenario should be synthetic. Never upload confidential employer/client material or record people without proper permission.

## Hackathon evaluation set

Create several short, synthetic workshop scenarios with a human-authored reference answer. Include:
- clear process steps and roles;
- a missing approval rule;
- a process exception;
- two statements that conflict across sessions;
- a stakeholder correction that should override an unvalidated inference;
- one irrelevant statement to test over-extraction;
- one unsupported claim the model should mark as unknown.

## Metrics to report honestly

Use a few measurable checks rather than claiming generic accuracy:

1. **Evidence-link validity:** percent of material output objects whose referenced source IDs exist and whose excerpt actually supports the claim (manual review for support).
2. **Process coverage:** compare generated process steps against the human reference; note omitted and invented steps.
3. **Conflict recall and precision:** whether seeded contradictions were found and whether normal variations were incorrectly flagged.
4. **Question usefulness:** reviewer ratings for relevance, specificity, actionability, and non-redundancy.
5. **Human correction persistence:** whether a validated correction survives reload and influences the next checkpoint.
6. **Operational behaviour:** response latency, model/API failure handling, malformed output rate, and measured cost/usage if available.

Do not say an LLM judge score is ground truth. Use deterministic checks where possible and human review for semantic support and usefulness. Report sample size and limitations.

## Privacy and safety requirements

- Display a clear notice and obtain appropriate permission before capturing real conversations.
- Use synthetic workshop data for the hackathon demo.
- Keep API keys server-side and out of git, frontend bundles, prompts, demo footage, and logs.
- Collect only what is needed for the current feature. Do not retain raw audio by default unless there is a clear reason and user control.
- Provide a clear session reset/delete path for the MVP where feasible.
- Design data structures with engagement boundaries, even if full multi-tenant auth is deferred.
- Validate file type and size; do not execute uploaded content.
- Treat transcript text, images, and documents as untrusted data. They can contain prompt-injection-like instructions; never let quoted client content override system instructions or authorize tools/actions.
- The model may propose decisions, never make the actual client decision.
- No automatic writes to external enterprise systems in the hackathon MVP.

## Reliability behaviours

- Preserve input if model inference fails.
- Show honest loading/error/retry states.
- Validate model output against a schema and verify source IDs.
- Use bounded retry, not endless loops.
- Avoid duplicate database records after retry; make writes idempotent where practical.
- Log useful diagnostics without logging keys or unnecessarily exposing source content.
- Show when a summary is incomplete or stale.
- Treat evidence status as independent of model confidence.

## Evaluation record template

| Test case | Expected outcome | Actual outcome | Pass/partial/fail | Notes |
|---|---|---|---|---|
| Clear process | Core steps extracted with sources | Fill after running | | |
| Missing rule | Targeted question generated | Fill after running | | |
| Cross-session contradiction | Conflict shown with both sources | Fill after running | | |
| Human correction | Status/history persists | Fill after running | | |
| Unsupported claim | Marked unknown or unsupported | Fill after running | | |

Do not leave placeholder evaluation results in the final submission. Fill them with actual observations or omit the unsupported claim.
