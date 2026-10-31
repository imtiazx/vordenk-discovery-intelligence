# Kimi Code in VS Code — Learning-First Workflow

This is guidance for later; it is not an actual VS Code configuration file. Create repository-specific instructions only after the actual repository and stack exist.

## Before code changes

1. Open the repository root in VS Code.
2. Ask Kimi Code to explain a specific file/folder or trace the data flow. Reference actual files using the extension's file-reference feature when available.
3. Ask for a plan before edits: behaviour, files to change, risks, and acceptance criteria.
4. Approve a small task only. Do not ask for “build all of Vordenk” in one prompt.
5. Review the diff before accepting changes. Ask Kimi to explain non-obvious code and any new dependencies.
6. Run the actual test/build command and inspect output. Save a Git checkpoint after a coherent verified step.

## Example prompts

- “Explain how this feature works from browser to database. Do not edit files.”
- “I am a beginner in this part. Teach me what the current code does, then propose the smallest change.”
- “Plan the feature and acceptance criteria first. Do not make changes until I approve.”
- “Explain this diff, including state management, API calls, validation, and errors. Identify what I should test.”
- “Diagnose this error from the output. Do not rewrite unrelated files.”
- “Check if any keys or sensitive workshop data are in the diff or logs.”

## Rules for repository-specific instructions

Once a repository exists, create `AGENTS.md` (or the convention documented by the current tool) with:
- accurate stack and directory map;
- verified setup, lint, test, type-check, and build commands;
- coding and dependency rules;
- tests required for API, schema, persistence, and UI changes;
- no secrets or unauthorised client data;
- inspect/plan/explain before editing; small diffs; actual test reporting;
- code ownership and learning goals.

Do not copy every product brief into `AGENTS.md`. Keep agent instructions short and put product rationale in normal docs.

## Acceptance checklist for a generated diff

- Is it limited to agreed files/behaviour?
- Are API keys server-side?
- Are request and model response schemas validated?
- Are source references validated rather than trusted blindly?
- Are failures and retries bounded and visible?
- Are new dependencies justified?
- Is persistence/versioning correct?
- Were real tests run, and is the output available?
- Did the change preserve the Extracted/Inferred/Validated/Decision distinction?
- Did any confidential source material enter Git?
