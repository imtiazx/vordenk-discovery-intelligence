# Meta Global AI Developer Hackathon — Rules and Strategy

## Official themes

The participant guide names two themes:

- **Build for Your World:** bring Meta's models into a domain you know firsthand and solve a real problem.
- **Push the Frontier:** use Meta's models to create new capabilities in areas such as software, robotics, manufacturing, energy, materials, and more.

**Recommended fit for Vordenk:** Build for Your World. The idea comes from firsthand enterprise AI consulting and requirements-discovery experience. Manufacturing/engineering process examples can add specificity, but do not claim the product is manufacturing-only.

## Track

The event has an Indie Developer track for individual builders/students, described as judged on creativity, technical ambition, and whether the project works, and a Startup track for teams/founders with emphasis on technical execution and production readiness. Confirm which track is recorded on the accepted application. Do not change the claimed track in project materials without verifying the application.

## Rules from the participant guide

- Repository must be **public**.
- Team size is at most four; solo builders are permitted.
- The demo must highlight the specific code, features, and functionality built during the hackathon. Judges must be able to identify new work clearly.
- Startups can build on an existing product/codebase, but must clearly identify what was newly developed during the event. Do not misrepresent old work as new.
- Do not use data, code, or assets without rights or permission.
- The guide explicitly warns against generic projects and names **basic RAG applications**, simple image analysers, generic AI education chatbots, job screeners, nutrition/medical advice apps, personality analysers, sports analysers, and political/war projects as examples to avoid.
- The submission needs a working project, public repository, accessible video link, and a **three-minute demo video** showing the new work.
- Stage one is a pass/fail check: the project must fit the theme and reasonably use Meta Model API and/or Meta open-weight models.

## Deadline and schedule

As stated in the participant guide and official event page:
- Build period: October 27–November 4, 2026.
- Submission deadline: November 4, 2026, 9:00 PM Eastern Time.
- Conversion to India Standard Time: November 5, 2026, 7:30 AM IST. Submit well before the deadline and re-check the official platform for changes.
- Judging: November 4–8; closing ceremony listed for November 9.
- Official programming listed in the guide: Agents 101 on Oct 27; Agents 102 / verifiable agents on Oct 28; Fireworks session on open models on Oct 30; office hours on weekdays.

## Strategy for a strong submission

Do not try to build all of Vordenk in nine calendar days. Build one complete, coherent, demonstrable loop that makes the long-term product vision credible:

**conversation + workshop artifact → Meta model reasoning → evidence-linked transformation model → prioritised questions + editable visual → human correction → persistent cross-session update.**

Make the Meta model use visible and essential. Show where it is used, what structured output it produces, how the application validates it, and how it changes the user's workflow. Do not add models only to tick boxes.

Optimise the build for:
1. Clear, personally experienced problem and a distinctive product insight.
2. A functioning end-to-end workflow, not a collection of mock screens.
3. Meaningful Meta model integration and technical explanation.
4. Verifiable evidence links, explicit uncertainty, and a useful human feedback loop.
5. A polished visual demonstration that reveals the value in under three minutes.
6. Public, readable code and documentation, with a clear record of what was created during the hackathon.
7. Honest evaluation, limitations, and privacy handling.

No file or strategy can guarantee a win. It can make the project easier to understand, test, and judge.

## Credits described in the participant guide

- **Meta Model API:** accepted participants can apply for $150 in credits. Guide says each participant must claim their own; a valid payment method may be required and can trigger a temporary authorisation. Set a spend-limit alert. Claim by Nov 4, 9 PM ET.
- **Baseten:** request $100 credits and a 2M tokens-per-minute limit; reviewed, not guaranteed, per individual. For the hackathon's Muse Spark Open, guide says to use `meta-models/muse-spark-open-1026` (not the older model name in generic docs).
- **Modal:** request $100 credits; guide describes the first 1,000 participants, for Meta open-weight inference through Endpoints plus serverless GPUs/sandboxes/training tools. Check current availability.
- **Fireworks:** request $25 in credits for the team; shortlist only, not guaranteed.

Credits are optional and not guaranteed. Do not block core development while waiting for them. The default plan uses Meta Model API directly.

## Official links

See `15_OFFICIAL_RESOURCES.md` for current docs, credit forms, official event page, community channels, and submission portal.
