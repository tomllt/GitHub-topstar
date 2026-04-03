# oh-my-codex (OMX)

<p align="center">
  <img src="https://yeachan-heo.github.io/oh-my-codex-website/omx-character-nobg.png" alt="oh-my-codex character" width="280">
  <br>
  <em>Start Codex stronger, then let OMX add better prompts, workflows, and runtime help when the work grows.</em>
</p>

[![npm version](https://img.shields.io/npm/v/oh-my-codex)](https://www.npmjs.com/package/oh-my-codex)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/node-%3E%3D20-brightgreen)](https://nodejs.org)
[![Discord](https://img.shields.io/discord/1452487457085063218?color=5865F2&logo=discord&logoColor=white&label=Discord)](https://discord.gg/PUwSMR9XNk)

**Website:** https://yeachan-heo.github.io/oh-my-codex-website/  
**Docs:** [Getting Started](./docs/getting-started.html) · [Agents](./docs/agents.html) · [Skills](./docs/skills.html) · [Integrations](./docs/integrations.html) · [Demo](./DEMO.md) · [OpenClaw guide](./docs/openclaw-integration.md)

OMX is a workflow layer for [OpenAI Codex CLI](https://github.com/openai/codex).

It keeps Codex as the execution engine and makes it easier to:
- start a stronger Codex session by default
- run one consistent workflow from clarification to completion
- invoke the canonical skills with `$deep-interview`, `$ralplan`, `$team`, and `$ralph`
- keep project guidance, plans, logs, and state in `.omx/`

## Recommended default flow

If you want the default OMX experience, start here:

```bash
npm install -g @openai/codex oh-my-codex
omx setup
omx --madmax --high
```

Then work normally inside Codex:

```text
$deep-interview "clarify the authentication change"
$ralplan "approve the auth plan and review tradeoffs"
$ralph "carry the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"
```

That is the main path.
Start OMX strongly, clarify first when needed, approve the plan, then choose `$team` for coordinated parall

... (truncated)