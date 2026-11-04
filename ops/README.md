# Delivery

Add `deliver` to a same-repository pull request targeting `main` to run the official agent-autoloop review and required CI before merging. Add `deliver-review` alongside it for review only. The trusted configuration and review points are read from `main`; the first setup PR must be independently reviewed and bootstrapped before this path can operate.

All paths are reviewed (`internal` is empty). No administrator merge bypass is enabled. CI uses no application credentials. Workflow success and the `check` job must both pass for the exact PR head. The local service must remain online and authenticated to GitHub and Codex.

This repository has no public health endpoint or configured production deployment. Accordingly `health` is omitted and the official receipt means **merged only**. Release readiness is checked in CI as described below; no synthetic health URL, release tag or production deployment is created.

Official references: [delivery setup](https://github.com/KKKKhazix/agent-autoloop/blob/main/skills/agent-autoloop/SKILL.md#交付流水线), [GitHub workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).

CI validates skill frontmatter, agent metadata, relative documentation links and a distribution archive of the five installable files. Installation still uses the existing GitHub/skills command; no package registry credential is needed.
