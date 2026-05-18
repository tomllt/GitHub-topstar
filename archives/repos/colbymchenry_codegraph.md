<div align="center">

# CodeGraph

### Supercharge Claude Code, Cursor, Codex, and OpenCode with Semantic Code Intelligence

**94% fewer tool calls · 77% faster exploration · 100% local**

[![npm version](https://img.shields.io/npm/v/@colbymchenry/codegraph.svg)](https://www.npmjs.com/package/@colbymchenry/codegraph)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-18+-green.svg)](https://nodejs.org/)

[![Windows](https://img.shields.io/badge/Windows-supported-blue.svg)](#)
[![macOS](https://img.shields.io/badge/macOS-supported-blue.svg)](#)
[![Linux](https://img.shields.io/badge/Linux-supported-blue.svg)](#)

[![Claude Code](https://img.shields.io/badge/Claude_Code-supported-blueviolet.svg)](#)
[![Cursor](https://img.shields.io/badge/Cursor-supported-blueviolet.svg)](#)
[![Codex CLI](https://img.shields.io/badge/Codex_CLI-supported-blueviolet.svg)](#)
[![opencode](https://img.shields.io/badge/opencode-supported-blueviolet.svg)](#)

<br />

### Get Started

```bash
npx @colbymchenry/codegraph
```

<sub>Interactive installer auto-configures your agent(s) — Claude Code, Cursor, Codex CLI, opencode</sub>

#### Initialize Projects

```bash
cd your-project
codegraph init -i
```

![1_C_VYnhpys0UHrOuOgpgoyw](https://github.com/user-attachments/assets/f168182f-4d9a-44e0-94d7-08d018cc8a3a)

</div>

---

## Why CodeGraph?

When Claude Code explores a codebase, it spawns **Explore agents** that scan files with grep, glob, and Read — consuming tokens on every tool call.

**CodeGraph gives those agents a pre-indexed knowledge graph** — symbol relationships, call graphs, and code structure. Agents query the graph instantly instead of scanning files.

### Benchmark Results

Tested across 6 real-world codebases comparing Claude Code's Explore agent **with** and **without** CodeGraph:

> **Average: 92% fewer tool calls · 71% faster**

| Codebase | With CG | Without CG | Improv

... (truncated)