# OpenRig

[![npm version](https://img.shields.io/npm/v/@openrig/cli)](https://www.npmjs.com/package/@openrig/cli) [![npm downloads](https://img.shields.io/npm/dw/@openrig/cli)](https://www.npmjs.com/package/@openrig/cli) [![License: Apache 2.0](https://img.shields.io/github/license/mvschwarz/openrig)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/mvschwarz/openrig?style=social)](https://github.com/mvschwarz/openrig/stargazers)

A harness wraps a model. A rig wraps your harnesses. Define your agent team in YAML, boot it with one command. Claude Code and Codex in the same rig, managed as one system.

OpenRig turns AI coding agents from a pile of terminal sessions into a persistent, organized team. Talk to a lead agent about the outcome you want; it can coordinate specialists across teams and bring you results and decisions that need your attention. Start with a repository and one useful change, then keep the team's work and context at the same addresses.

## Install and first run

Requires Node.js 22 or 24 and tmux, on macOS or Linux. On a Mac with Apple silicon, use Node.js 22 ([compatibility history](docs/releases/v0.5.15.md#known-compatibility-limitation)). Native Windows is not supported yet, and WSL2 has not been tested. Launching a rig writes provider hooks and workspace trust settings. Before running the commands below, read [what OpenRig changes on your machine](#what-openrig-changes-on-your-machine) and back up the relevant files.

```bash
npm install -g @openrig/cli
rig setup --dry-run
```

To install with Bun instead, run `bun add -g @openrig/cli`. OpenRig still runs on Node.js, so install Node.js 22 as well. Bun may block this package's postinstall script, in which case the Node.js and SQLite check described under [what OpenRig changes on your machine](#what-openrig-changes-on-your-machine) does not run at install time.

Review setup's plan before applying `rig setup`: it checks both native harnesses and cmux. This starter requires tmux an

... (truncated)