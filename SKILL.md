---
name: design-polished-frontends
description: Design, implement, and verify polished frontends for websites, web apps, dashboards, component systems, browser extensions, mobile apps, desktop apps, and embedded interfaces. Use for end-to-end frontend delivery or substantial UI and interaction refinement that requires evidence-backed design choices, responsive behavior, accessibility, performance checks, real-state coverage, and QA on the actual target surface. Do not use for isolated review, bug diagnosis, or deployment-only tasks.
metadata:
  author: YannJY02
  version: "1.0.0"
  repository: "https://github.com/YannJY02/design-polished-frontends"
---

# Resource-routed frontend delivery

Deliver a coherent, working frontend on its real target surface. A resource counts only when it is actually loaded, called, opened, run, or inspected and its output changes or validates the work.

## Execution contract

Within the authority already granted by the governing frontend task and environment, carry out every reversible, task-scoped action needed to complete the frontend:

- inspect and edit the current project;
- read applicable skill instructions;
- use network, browser, simulator, local UI, and available tools;
- install compatible project or local tooling with the project's package manager;
- download selected dependencies, assets, fonts, icons, examples, or model files;
- update task-owned project configuration and lockfiles;
- start services and run builds, tests, accessibility, and performance checks.

Treat these as normal implementation actions and do not ask for permission again. Perform them instead of recommending that the user do them. Reuse the current stack first, keep setup scoped and reversible, verify every installation or configuration change, and retain only resources selected for the result.

Human action is required only for information or authority the agent cannot obtain: credentials, account or device approval, paid purchases, acceptance of legal terms, incompatible licensing, destructive changes, or production/external mutation not already requested. Use the active `wizard` skill for such a gate; when it is not cataloged, load its installed instructions as reference if available, otherwise ask the minimum direct question. Resume afterward. If the environment can request a narrow permission elevation itself, do that before asking the user.

## Execute a route

Inspect the project, active skill catalog, available tools, and target runtime before choosing routes. Read [references/resource-routes.md](references/resource-routes.md) completely before selecting the lanes needed for the current frontend.

Use the matching execution primitive:

- **Skill:** select an exact name from the active catalog, announce it, read its `SKILL.md` completely, and follow its relevant instructions. A name mentioned in prose is not execution. When instructions exist only as a local file outside the active catalog, they may be read as reference; record `loaded from path`, not `invoked skill`.
- **Tool:** make the tool call and inspect its result. Availability by name is not execution.
- **Source:** open or fetch the exact page, component, documentation, license, or terms. A search result or gallery thumbnail is discovery evidence only.
- **Runtime:** run the command or interact with the browser, simulator, app, extension host, or device and inspect the output.

For each selected route record one compact receipt:

`Need | Kind | Executed capability/source | Observed evidence | Decision | Applied delta | Verification`

A route is complete only when the receipt contains observed evidence. If setup fails, add useful context, try one safe recovery, then select the declared fallback. Stop a provider after an authentication, quota, credit, or terms failure.

## 1. Frame the frontend

Inspect the governing instructions, source, dependencies, design system, content, assets, Git state, and running product. Establish the product, users, primary task, proof or trust needs, platform, input methods, adaptive sizes, states, and delivery target. Ask one concise question only when an undiscoverable answer would materially change the result.

Before building, define a small acceptance matrix for the actual evaluator and target surfaces: immediate comprehension, primary action or journey, required evidence and states, representative sizes, accessibility and performance checks, high-impact defect criteria, and the stopping condition. Use numeric thresholds only when the current tools can measure them. For evidence-bearing surfaces, map quantified or outcome claims to their source and state unknown impact explicitly.

Choose the branch:

- **New frontend:** define one product-specific visual concept, information journey, component strategy, and interaction baseline.
- **Existing frontend:** compare the current system with routed evidence and classify findings as **keep**, **improve**, or **replace**; preserve strong foundations.
- **Component system:** define its consumers, representative stories or compositions, variants, states, tokens, accessibility contract, and integration surface.

**Complete when:** a compact brief names the target surfaces, primary journey or representative consumer compositions, required states, visual concept, constraints, verification commands, acceptance matrix, and stopping condition, with unsupported claims marked as placeholders.

## 2. Resolve and bootstrap routes

Choose one primary implementation/design route and one real target-surface QA route. Add strategy, brand, asset, reference, motion, accessibility, performance, or delivery routes only when the brief needs them. Resolve one fallback for every route that depends on an external provider.

Execute required setup now: load skill instructions, install or download selected resources, configure project-local integration, and prove each resource through a minimal import, command, render, or tool result. Follow the project's existing package manager and lockfile. Check exact source terms before copying code or assets.

**Complete when:** every selected route has execution evidence, required setup is verified, and the current frontend can run or render on its target surface or the strongest available target-equivalent with the gap named.

## 3. Build the coherent pass

Implement the primary journey or representative consumer compositions and real states in the existing stack. Prefer the project's components, platform-native behavior, and installed dependencies when they satisfy the brief. Add the smallest compatible resource only when routed evidence shows a real gap.

Keep typography, semantic color, spacing, surfaces, iconography, assets, and motion in one visual language. Create or update `design.md` only when the project needs a durable multi-surface system; otherwise keep the decisions in existing tokens and components. Record provenance and current terms for third-party assets or copied code.

**Complete when:** the primary journey or representative consumer compositions work with their in-scope variants and states, and the implementation expresses the chosen concept without breaking established behavior.

## 4. Make the target-surface loop green

Exercise the frontend where users will use it:

- web at representative wide and narrow viewports plus composition breakpoints;
- mobile in the relevant simulator or device sizes and orientations;
- desktop in the real app and meaningful window sizes;
- extensions or embedded interfaces inside their actual host context.

Test the primary journey or representative component stories plus changed navigation, forms, menus, dialogs, focus order, keyboard, pointer or touch behavior, readable scaling, contrast, reduced motion, loading, failure, and recovery. Inspect console, network, accessibility, screenshots, and runtime traces that the platform exposes. At each adaptive size, check geometry and state as well as appearance: unintended document overflow, overlays both open and closed, first-view action placement, loaded assets, and responsive asset selection.

Judge stable-state screenshots only after fonts, images, layout, and intended entry motion settle; capture transitional states separately when motion itself is under test. Treat aggregate audit scores as summaries, not verdicts: inspect every failed high-impact accessibility, performance, or best-practice item even when a category score is green. Fix the smallest root cause, rerun the affected matrix row, and record the before/after evidence.

If the real target remains unavailable after task-scoped setup, exercise the closest runnable simulator, host, preview, story, or build artifact and keep the real target explicitly unverified.

**Complete when:** the acceptance matrix is green or each residual gap is explicit, the exercised surface has no known high-impact visual, interaction, accessibility, or runtime defect in scope, and the tested surfaces, sizes, flows, proxies, and residual gaps are recorded without claiming an unrun target is green.

## 5. Prove and deliver

Run the repository's relevant build, type, lint, and test commands. Measure before optimizing; fix the largest observed frontend bottleneck and compare again when performance is in scope. Verify third-party licenses, changed lockfiles, asset delivery, and repository state.

Follow the existing release process. Deploy only when requested or already authorized by the governing task; then open the fresh public or distributed build and rerun the primary journey or representative consumer compositions. Otherwise stop at a verified deployable artifact. Commit and push when the governing repository instructions require it.

**Complete when:** relevant checks pass or have explicit blockers, every selected route has an evidence-bearing receipt, the target surface or strongest available target-equivalent has been rerun, any unverified real target remains explicit, and the delivered or deployable state is identified precisely.

## Final gate

- The primary action, task, or component purpose is immediately understandable.
- One memorable visual idea belongs to this product.
- Components, content, assets, and motion speak one language across adaptive states.
- Interaction remains understandable with motion reduced and input methods changed.
- Claims, provenance, licenses, and measured performance are truthful.
- Resource names alone never count as use; receipts contain observed output.

Report changed surfaces, route receipts, setup performed, target-surface evidence, command results, measured performance when applicable, delivery state, and remaining issues.
