# Executable frontend route cards

Read this file completely before route selection, then apply only the lanes needed by the brief. Candidates are conditional: resolve them against the active skill catalog, available tools, installed stack, target platform, network access, and current source terms.

## Route resolution and setup

### Resolve in this order

1. Existing project implementation, components, tokens, assets, scripts, and package manager.
2. Platform-native controls, layout, animation, accessibility, and diagnostics.
3. An applicable skill present in the active catalog.
4. An available tool that can produce observable output.
5. An exact authoritative source, component, or asset with compatible terms.
6. The smallest native implementation that satisfies the brief.

Execute the matching skill, tool, source, or runtime primitive defined in `SKILL.md`; record its observed output in the route receipt.

### Bootstrap automatically

Use the project's existing package manager and lockfile; inspect installed versions before consulting version-specific documentation. Install only the selected dependency and its required peers. Prefer project-local configuration and temporary evaluation directories over global changes.

After setup, prove the route with the smallest meaningful check:

- skill: observed guidance applied to a named decision;
- package: import, build, or rendered component succeeds;
- CLI: version plus one relevant command succeeds;
- tool: returned result is inspected;
- asset: file opens, renders, and has recorded provenance;
- browser or simulator: target launches and the changed flow runs.

Remove rejected downloads and evaluation artifacts. Apply the human-gate contract from `SKILL.md` when setup needs unavailable information or authority.

### License and provenance gate

Before copying code, fonts, images, models, demos, or templates, open the exact official source and current terms. Check commercial use, modification, attribution, redistribution, prohibited uses, version, upstream assets, and model/output terms separately. Record URL, version or access date, selected material, modifications, and attribution. Inspiration supplies relationships, not branding, copy, or assets.

## Product journey and hierarchy

Use when audience, information order, task flow, trust, or attention is unresolved.

- Start with user-supplied requirements, analytics, interviews, screenshots, and existing flows.
- Use an active product-design or research skill only when its description matches the decision.
- Use `cognitive-design` when visual hierarchy, grouping, density, perception, or attention needs an explicit rationale.
- Inspect current official product material and at least one live comparable journey when market or interaction context affects the design.

**Extract:** audience question, value proposition or task promise, primary action, proof, objections, information order, success path, and unsupported claims.

**Evidence:** named artifacts or URLs plus the brief decisions they changed or validated.

## Implementation and platform

Use the branch that matches the real target.

### Web, PWA, dashboard, extension, or WebView

- Use `frontend-design` for end-to-end visual implementation when active.
- Use `design-taste-frontend` for frontend taste and anti-template constraints when active and relevant.
- Prefer existing project components, then semantic HTML, CSS, and SVG.
- For behavior-rich accessible React primitives, inspect the exact [shadcn/ui](https://github.com/shadcn-ui/ui) component and dependencies.
- For lightweight Tailwind sections, inspect exact [HyperUI](https://github.com/markmead/hyperui) code and license.
- Use [Page UI](https://github.com/PageAI-Pro/page-ui) only for a compatible React or Next.js landing-page need.

### Apple mobile or desktop

- Use `mobile-ios-design`, `macos-design-guidelines`, or `macos-developer` when active and matched to the target.
- Use the applicable `build-ios-apps:*` or `build-macos-apps:*` skill for SwiftUI, AppKit, windowing, debugging, performance, signing, or packaging decisions.
- Prefer native SwiftUI or AppKit controls and the project's established component layer.

### Other native, cross-platform, or embedded frontends

- Select the active platform skill whose description exactly matches the installed framework.
- Prefer the framework's native components, accessibility semantics, navigation, adaptive layout, and diagnostics.
- Treat browser screenshots as insufficient proof for a native target; verify inside its real simulator, runtime, or host.

**Extract:** visual concept, layout grammar, component source, state model, input methods, adaptive behavior, compatibility constraints, and setup delta.

**Evidence:** loaded skill guidance or exact source, successful integration check, and a running target surface or named target-equivalent with any unverified-target gap.

## Brand system

Use when the frontend needs new or repaired tokens, typography, iconography, surface language, or motion character.

- Use `cognitive-design` for hierarchy and information-density decisions.
- Reuse the project's token and component system when comparison supports it.
- Web token exploration: [TweakCN](https://tweakcn.com/), [Open Props](https://open-props.style/), and [Radix Colors](https://www.radix-ui.com/colors).
- Typography: project-owned fonts first, then inspect exact families and licenses at [Google Fonts](https://fonts.google.com/) or the platform font source.
- Icons: keep the established family; otherwise inspect [Phosphor Icons](https://phosphoricons.com/) or platform-native symbols and terms.
- Native targets: inspect the current official platform design guidance and accessibility requirements.

**Extract:** brand concept, semantic color roles, type roles, spacing rhythm, surfaces, icon rules, media language, motion character, and adaptive rules.

**Evidence:** exact sources and keep/improve/replace decisions reflected in tokens or components across representative states.

## Assets

Use when visible imagery, illustration, screenshots, diagrams, textures, or branded media affect the result.

1. Owned product captures and brand assets.
2. Purpose-made project SVG, diagram, or illustration.
3. `imagegen` for original raster generation or editing when active and selected.
4. `creative-production:produce` when the asset needs broader exploration or adaptation.
5. Reusable assets such as [unDraw](https://undraw.co/) or [Open Peeps](https://www.openpeeps.com/) after opening their current terms.
6. Local generation such as [ComfyUI](https://github.com/Comfy-Org/ComfyUI) only when its model, hardware, disk, time, and license fit the task.

**Extract:** role, medium, subject, composition, aspect ratio, adaptive crop, palette, alt intent, destination, provenance, and terms.

**Evidence:** selected files render on target surfaces, crops and loading are verified, accessibility intent is implemented, and provenance is recorded.

## Composition references

Use when hierarchy, density, framing, proof cadence, section rhythm, navigation, or reveal order needs external comparison.

- Inspect at least two accessible references from different sources using a real browser or target-platform gallery.
- For web compositions consider [Lapa Ninja](https://www.lapa.ninja/), [Land-book](https://land-book.com/), [Landing.Gallery](https://www.landing.gallery/), or [Codrops](https://tympanus.net/codrops/).
- For native frontends prefer current official platform showcases and real comparable apps.
- If automation is blocked, try a visible browser once, then select an accessible source and record the limitation.

**Extract:** abstract relationships only: alignment, scale, negative space, density, framing, hierarchy, navigation, proof cadence, rhythm, and reveal order.

**Evidence:** exact URLs or inspected apps, current-product comparison, adopted or rejected relationship, and responsive or adaptive rerun.

## Components and motion

Use only for surfaces whose feedback, hierarchy, continuity, or delight underperform.

1. Existing project primitives and installed motion runtime.
2. Native CSS, Web Animations API, or platform animation APIs.
3. Exact compatible components from [Motion Primitives](https://github.com/ibelick/motion-primitives), [Magic UI](https://github.com/magicuidesign/magicui), [Animata](https://github.com/codse/animata), or [Codrops](https://tympanus.net/codrops/) after checking dependencies and terms.
4. Low-level Motion, OGL, Three.js, React Three Fiber, particles, shaders, or 3D only when the product concept depends on them.

Compare two plausible candidates when adding a new interaction dependency. Inspect controls, hard-coded styling, continuous work, bundle or runtime cost, mobile behavior, and reduced-motion behavior. Pause offscreen continuous work and preserve keyboard, pointer, touch, and assistive equivalence.

**Evidence:** candidate comparison, successful integration, normal and reduced-motion interaction, and no input, layout, or performance regression.

## Target-surface QA

Choose the real execution surface when available; otherwise use the strongest runnable target-equivalent and keep the real target explicitly unverified.

- Web: `browser:control-in-app-browser`, `chrome:control-chrome`, or another active browser automation skill/tool; use Playwright only when installed or task-scoped installation succeeds.
- iOS or macOS: applicable simulator, app runtime, or active platform debugging skill.
- Desktop cross-platform: packaged or development app runtime at representative window sizes.
- Extensions and embedded UIs: actual browser, host app, or container context.
- Local UI unreachable by browser automation: `computer-use:computer-use` when active.

Inspect focus order, accessibility tree, screenshots, console, network, runtime logs, scaling, input behavior, reduced motion, and recovery states exposed by the platform.

**Evidence:** real target or named target-equivalent, size or viewport, state, action, expected result, observed result, applied fix, clean rerun, and any unverified-target gap.

## Performance and accessibility

Use an active performance or accessibility skill when it matches the platform; otherwise use native profiling and inspection tools.

- Web: browser Performance, Network, Rendering, Accessibility, Lighthouse where suitable, framework production output, and current framework bundle-analysis guidance.
- Native: platform profiler, accessibility inspector, launch/render traces, memory and energy diagnostics appropriate to the target.
- Assets: framework image tooling or Squoosh-compatible inspection when useful.

Capture a comparable baseline before changing performance. Fix the largest observed bottleneck first while preserving design intent. Numeric improvement claims require before-and-after measurements.

**Evidence:** command or trace, baseline, bottleneck, affected journey, applied delta, comparable result, and remaining ceiling.

## Repository and delivery

Follow governing repository and release instructions. Use the existing Git, CI, signing, packaging, and deployment route. Load a provider-specific skill only when it is active and the task actually targets that provider.

Deployment, publishing, store submission, or production mutation proceeds only when requested or already authorized. After external delivery, open the fresh public, distributed, or installed result and rerun the primary journey or representative consumer compositions. Otherwise verify the build artifact and configured route without external mutation.

**Evidence:** repository status, checkpoint or commit, build artifact, provider or packaging result, public/distributed target when applicable, and fresh-flow verification.
