# Design Polished Frontends

[中文说明](README.zh-CN.md)

Design Polished Frontends is an Agent Skill for end-to-end frontend delivery. It helps a coding agent turn product intent into a coherent interface, implement it in the existing stack, and verify the result where people will actually use it.

It covers websites, web apps, dashboards, component systems, browser extensions, mobile apps, desktop apps, and embedded interfaces. The work does not stop at a clean screenshot. The skill also checks responsive behavior, real states, accessibility, performance, input methods, and runtime evidence.

## Install

```bash
npx skills add YannJY02/design-polished-frontends@design-polished-frontends
```

Install for a specific agent:

```bash
npx skills add YannJY02/design-polished-frontends \
  --skill design-polished-frontends \
  --agent codex
```

Then invoke it in your request:

```text
Use $design-polished-frontends to redesign this product, implement the primary journey, and verify it on the real target surface.
```

## What makes it different

This skill owns the whole delivery loop instead of stopping at visual direction or code generation.

### It starts with the product, not a style preset

The agent first identifies the users, primary task, trust needs, platform, adaptive sizes, required states, and acceptance criteria. Existing products are assessed as keep, improve, or replace so a redesign does not erase strong foundations.

### It routes resources by need

The skill can use existing project components, platform-native controls, specialized design skills, browser tools, simulators, authoritative references, and selected assets. A resource only counts when the agent actually loads, calls, opens, runs, or inspects it and uses the result in the work.

Each selected route leaves a compact receipt:

```text
Need | Kind | Executed capability/source | Observed evidence | Decision | Applied delta | Verification
```

This makes the design process inspectable. A list of tool names is not treated as proof.

### It follows the real platform

The route changes with the target. Web projects use semantic HTML, CSS, browser diagnostics, and the established component stack. Apple platforms prefer SwiftUI or AppKit patterns. Extensions run inside their browser host. Desktop and cross-platform apps are checked in their actual runtime when available.

### It verifies states, behavior, and accessibility

The target-surface loop covers representative sizes and the primary journey. It also checks navigation, forms, menus, dialogs, focus order, keyboard and pointer behavior, touch input where relevant, readable scaling, reduced motion, loading, failure, and recovery.

Aggregate audit scores are summaries, not verdicts. High-impact failures still need inspection and a clean rerun.

### It keeps claims honest

If the real app, simulator, device, or host cannot run, the skill uses the strongest available equivalent and names the gap. A browser preview does not prove a native app is green. A passing build does not prove the interaction works.

## Delivery flow

| Phase | Result |
| --- | --- |
| Frame | A compact product brief, target surfaces, acceptance matrix, and stopping condition |
| Resolve | Verified design, implementation, asset, accessibility, performance, and QA routes selected only as needed |
| Build | One coherent implementation in the current stack, including real states and adaptive behavior |
| Verify | The primary journey exercised on the real target surface or a clearly named equivalent |
| Deliver | Relevant checks, route receipts, repository state, and an exact delivery status |

## Good fits

- Build a new product interface from a brief or working backend.
- Redesign an existing website or application without discarding useful foundations.
- Bring a dashboard, extension, mobile client, desktop client, or embedded UI to a release-ready state.
- Create or repair a component system and verify representative compositions, variants, states, and accessibility behavior.
- Turn an attractive prototype into a tested interface with responsive, accessibility, performance, and runtime evidence.

Use a narrower skill for a standalone code review, an isolated bug diagnosis, or a deployment-only task.

## Supported targets

- Websites, landing pages, PWAs, web apps, and dashboards
- Design systems and component libraries
- Browser extensions and WebViews
- iOS and macOS frontends
- Other mobile, desktop, cross-platform, and embedded interfaces when the environment provides the relevant runtime or simulator

## FAQ

### What is Design Polished Frontends?

It is a reusable Agent Skill that coordinates frontend product framing, design decisions, implementation, target-surface QA, accessibility, performance checks, and delivery evidence.

### How is it different from a frontend design prompt?

A prompt may improve visual output once. This skill defines a repeatable delivery contract. It inspects the current project, selects resources for specific needs, implements the working journey, and verifies observable behavior before calling the result ready.

### Does it force a framework or design system?

No. It reuses the current stack first, then platform-native features, active skills, installed dependencies, and the smallest compatible addition that closes a demonstrated gap.

### Does it deploy automatically?

Only when deployment is requested or already authorized by the governing task. Otherwise it stops at a verified deployable artifact.

### Does every environment support every route?

No. Browser, simulator, design, and deployment capabilities vary by agent and machine. The skill records the route that actually ran and states any unverified target.

## Repository structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    └── resource-routes.md
```

The canonical skill instructions live in [`SKILL.md`](SKILL.md). The route catalog lives in [`references/resource-routes.md`](references/resource-routes.md).

## Author

Created and maintained by [YannJY02](https://github.com/YannJY02).
