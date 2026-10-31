# Meta-First Model Integration Plan

## Guiding rule

Meta models must be meaningfully involved in the product's core loop. Do not use an unrelated model for the core reasoning and add a trivial Meta API call merely to satisfy the event. Also do not add extra Meta models only for quantity: every integration needs a visible role and a fallback plan.

Verify all names, API fields, limits, and availability against official docs before coding. Model IDs below are what the official docs/participant guide currently list as of the hackathon guide; re-check before implementation.

## Primary path (recommended)

### 1. Meta Muse Spark via Meta Model API — core reasoning

**Model ID in current docs:** `muse-spark-1.3`.

Use for:
- structured extraction of facts, process steps, roles, systems, rules, pain points, metrics, assumptions, and decisions;
- combining transcript evidence with uploaded approved image/PDF artifacts where supported;
- identifying contradictions, missing context, dependencies, and high-value discovery questions;
- generating a typed process representation and checkpoint synthesis;
- optionally applying reasoning or structured output features when supported by the official API.

Expected behaviour: prompt the model for a JSON object conforming to a versioned schema. Parse it, validate it, reject malformed output or retry carefully, and never trust free-form model output as database state without validation. Include source IDs/snippets in the input and ask for references to those source IDs. Then validate that every reference actually exists in the input.

### 2. Meta Muse Voice Transcribe — audio input

**Model ID in current docs:** `muse-voice-transcribe-1.0`.

Use for audio-to-text, including speaker attribution/turns where available. Official docs describe a file transcription endpoint and real-time WebSocket at `wss://api.meta.ai/v1/asr/realtime`. Check the current guide for request frames, authentication, event schema, limits, and supported audio formats.

Implementation order:
1. Prove a transcript can be pasted/uploaded and analysed. This keeps development unblocked.
2. Add transcription of a synthetic/consented audio clip if feasible.
3. Try live browser capture and streaming only after the first two steps work. Do not make the whole demo depend on an unproven WebSocket integration.

### 3. Use multimodality where it adds product value

Muse Spark supports image/PDF and other multimodal inputs according to Meta's model docs. A strong demo can upload a synthetic process slide or whiteboard photo alongside a transcript and ask Vordenk to reconcile them. The output should note disagreement and source evidence; do not assume the image is correct or use model output as an unquestioned fact.

### 4. Muse Image — optional

Current docs list `muse-image-1.0`. Use only if you have a concrete customer-facing function, such as producing a labelled conceptual illustration of an approved future-state solution. Keep it clearly separate from the canonical process graph, facts, and process steps. Do not spend precious time on decorative image generation.

### 5. SAM 3.1 — optional

Current docs list `sam-3.1` for image/video segmentation. Do not include it unless the app genuinely needs segmentation of a visual artifact; segmentation does not replace reading or understanding the business process. Optional and likely lower priority than completing the main flow.

## API and secrets

The current official Model API overview lists base URL `https://api.meta.ai/v1` and bearer authentication using `MODEL_API_KEY`. Use the official SDK/example for the exact request shape. Keep the key server-side in an environment variable; never put it in frontend code, public source, screenshots, demo videos, or logs.

Create `.env.example` with placeholder variable names only, not real credentials. Add `.env`, local credential files, logs containing keys, and uploaded private content to `.gitignore` as appropriate. Use a spend-limit alert and monitor actual usage.

## Provider architecture and optional inference partners

Create a very small internal model-service interface so the rest of the application does not care whether a request goes directly to Meta Model API or a hosted open-weight provider. Do not build a general-purpose inference platform.

- **Default:** Meta Model API, which directly establishes Meta model usage.
- **Optional open-weight test:** Muse Spark Open through a provider if selected/available. The participant guide specifically says Baseten users should select `meta-models/muse-spark-open-1026` for this hackathon. Baseten/Modal/Fireworks credits are not guaranteed.
- Do not wire up multiple providers unless there is time to compare real quality, latency, or cost.

## Proof of meaningful Meta integration

The app/demo should show, without exposing secrets:
- the Meta model actually called;
- the part of the workflow it powers;
- at least one example of structured output used in the UI;
- measured latency and token/usage information only if available;
- graceful user-readable error handling if the model API fails.

Keep a brief `META_MODEL_USAGE.md` or a section in the README describing model roles, API calls, actual testing, limitations, and costs.

## Official model links

- Meta Model API overview: https://dev.meta.ai/docs/overview
- Models: https://dev.meta.ai/docs/models
- Quickstart: https://dev.meta.ai/docs/quickstart
- Meta API cookbook: https://github.com/meta-models/meta-model-cookbook
- Muse Voice Transcribe: https://dev.meta.ai/models/muse-voice-transcribe
- Muse Spark: https://dev.meta.ai/models/muse-spark
- Muse Image: https://dev.meta.ai/models/muse-image
- SAM 3.1: https://dev.meta.ai/models/sam-3-1
- Muse Spark Open: https://dev.meta.ai/models/muse-spark-open
