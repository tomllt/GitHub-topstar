# Codex Security

Codex Security helps you find, investigate, and fix vulnerabilities in your code.
Use its security workflows in Codex, or automate them with the
`@openai/codex-security` CLI and TypeScript SDK.

- **In Codex:** [choose a security workflow](docs/agent-workflows.md).
- **In a terminal:** [install the CLI and scan your repository](#quick-start).
- **In automation:** use the [TypeScript SDK](#typescript-sdk) or
  [GitHub Action](#github-actions).

## Features

- Scan repositories, selected paths, or Git changes. Deep scans repeat Standard scans and return their deduplicated findings.
- Validate candidate findings, generate patches, and verify existing fixes.
- Draft `SECURITY.md` policies and save threat models for later review.
- Browse saved scans and findings, identify duplicates, assess severity against
  your own rubric, and suggest owners from source and Git history.
- Preview third-party scanner findings, save them locally, or publish supported reports to Codex Security Cloud. [Scanner import guides](docs/scanner-imports/README.md).
- Track findings in Linear, Jira, or GitHub, publish completed scans, or export SARIF, JSON, and CSV. [Integration workflows](docs/plugin-connectors.md).
- Automate scans across repositories or project components, including in CI and
  containers.

## Use in Codex

Open your repository in a Codex session with the Codex Security plugin enabled,
then ask:

> Run a Codex Security scan on this repository, focusing on authentication and
> authorization. Return the saved report, source evidence, and coverage limits.

A completed scan saves a report and findings. Read the report for source
evidence and exclusions, then request a patch or ask Codex to verify an
existing fix. See the [agent workflow guide](docs/agent-workflows.md) for setup,
task selection, and recovery.

## Quick start

Requires Node.js 22.13.0+ within 22.x, or Node.js 24.x or 26.x, and Python 3.10+.
Python 3.10 also requires `tomli`.

Install the CLI global

... (truncated)