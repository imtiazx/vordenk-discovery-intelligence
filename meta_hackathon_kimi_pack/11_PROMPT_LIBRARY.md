# Prompt Library for Kimi Project Chats

Use one chat per major topic. Replace bracketed sections. Kimi must teach and guide, not take over by default.

## 1. First chat: orient me, challenge the plan, and teach me

Read the Project files, especially product vision, hackathon rules, MVP, Meta plan, execution plan, and learning contract. Do not write code yet. In beginner-friendly language, summarise: (1) the complete Vordenk vision, (2) the exact hackathon slice, (3) how this is more than meeting notes/basic RAG, (4) how Meta models contribute to the core experience, (5) the biggest feasibility risks before Nov 4, and (6) the smallest next task. Challenge the scope honestly. Ask at most one question if necessary. Do not invent facts or claim any implementation exists.

## 2. Prioritise for judging and time

Given the current date, our actual progress, and the official hackathon rules in the Project files, identify the highest-value next task. Evaluate user value, uniqueness, Meta-model dependence, feasibility, demo impact, and failure risk. Recommend one task, state what to cut, and define a testable exit criterion. Do not promise a win or add features merely to look advanced.

## 3. Learn one concept

Teach me `[CONCEPT]` using Vordenk as the example. Explain why we need it, a simple analogy, a small technical example, common mistakes, and one question/exercise for me. Do not generate production code unless I ask.

## 4. Architecture decision

Help decide `[DECISION]`. First explain the problem, then compare no more than three options by time to build, reliability, learning value, cost, Meta-model support, and maintenance. Verify fast-changing details in current official docs. Recommend one option for the hackathon and propose a decision-log entry marked `PROPOSED` until I approve it. Don't add infrastructure without evidence.

## 5. Meta API spike

Teach me to make the smallest real call to `[Muse Spark / Muse Voice Transcribe / other approved Meta model]` using official current documentation. First identify the exact model ID, endpoint, request/response format, authentication, input limits, and cost/rate-limit considerations. Show one minimal example; explain each part; ensure keys are server-side; then give me a command/test I can run. Do not invent a successful response. Record actual result and model role.

## 6. Plan a feature without coding

Feature: `[FEATURE]`. Inspect the existing repo files I provide. Explain goal, data flow, likely edge cases, files to change, and acceptance criteria. Break it into tasks small enough for a beginner. Highlight any risks to the deadline. Wait for my agreement before modifying code.

## 7. Pair-program one small change

We are implementing `[SMALL CHANGE]`. First inspect the current code and identify the smallest diff. Explain what I should understand before implementation. Do not touch unrelated code. After proposing the plan, wait for approval. Then make the change and show the diff, tests/commands run and actual output. Explain how I can verify it independently.

## 8. Debug methodically

Observed: `[WHAT HAPPENED]`. Expected: `[WHAT SHOULD HAPPEN]`. Help me diagnose this before changing code. Identify missing evidence, suggest safe checks from least to most disruptive, explain what each check proves, and consider at least two plausible hypotheses. Do not rewrite broad modules or pretend tests passed.

## 9. Design a transcript/evidence schema

Help me define a versioned structured schema for Vordenk `[OUTPUT TYPE]`. It must preserve source IDs, excerpt/timestamp when available, knowledge status (Extracted/Inferred/Validated/Decision), validation errors, and cross-session relationships. Show valid and invalid examples, explain how code checks the model response, and identify what must be human-reviewed. Don't assume a model obeys JSON just because it is prompted to.

## 10. Evaluate a model feature

Feature: `[FEATURE]`. Help create a small synthetic evaluation set with expected reference outputs. Define deterministic validation and human review criteria separately. Include good cases, conflict cases, missing evidence, irrelevant information, malformed output, and model failure. Give me a table template, but don't invent result values. Explain what sample size allows us to claim and what it doesn't.

## 11. Code review and teach me the diff

Review this actual diff as a senior engineer and teacher. Prioritise functional bugs, data integrity, provenance, privacy/security, failure handling, accessibility, and missing tests. Separate blockers from improvements. For every blocker, explain the consequence and smallest correction. Do not make broad changes unless I approve them.

## 12. End-of-day checkpoint

Summarise today's actual work only: new features, files changed, Meta models actually called, tests/commands and their real output, unresolved bugs, scope risks, and what I learned. Propose updates to roadmap/backlog/decision log for my review. Include a truthful build-log entry. Do not make plans based on features that are not working yet.

## 13. Prepare the three-minute demo

Using actual implemented functionality only, create a 180-second demo script. The story must show the problem, input evidence, actual Meta model involvement, a useful structured insight, process visual, a gap/question, cross-session memory or human validation, and the long-term Vordenk vision. Include what to click and what to say. Flag anything not built. Do not script fake latency, fabricated metrics, or imaginary users.

## 14. Freeze scope before submission

Inspect current backlog and build log. Classify remaining tasks as must-fix, polish, or cut. Prioritise public repo readiness, key safety/privacy, working demo path, real Meta integration, README, evaluation evidence, and video accessibility. Prohibit major new features after feature freeze unless they fix a blocker.

## 15. Prepare repository instructions for Kimi Code

Inspect the actual repository and official current Kimi Code documentation. Propose a concise `AGENTS.md` or supported repository instruction file with real commands, architecture, coding conventions, test rules, secret handling, and learning-first change policy. Do not invent paths, test commands, or framework choices.
