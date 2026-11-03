# agent-desktop

Computer use for AI agents: read and operate desktop apps through the OS accessibility tree.

<p>
  <a href="https://vercel.com/labs#labs-products"><img alt="Vercel Labs Product" src="https://img.shields.io/badge/LABS-PRODUCT-0a0a0a.svg?style=for-the-badge&amp;logo=Vercel&amp;labelColor=000000" height="28"></a>
  <a href="https://www.npmjs.com/package/agent-desktop"><img alt="npm version: agent-desktop" src="https://img.shields.io/npm/v/agent-desktop.svg?style=for-the-badge&amp;labelColor=000000" height="28"></a>
  <a href="https://github.com/vercel-labs/agent-desktop/blob/main/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/github/license/vercel-labs/agent-desktop.svg?style=for-the-badge&amp;labelColor=000000" height="28"></a>
  <a href="https://www.npmjs.com/package/agent-desktop"><img alt="npm downloads per month: agent-desktop" src="https://img.shields.io/npm/dm/agent-desktop.svg?style=for-the-badge&amp;labelColor=000000&amp;label=npm%20downloads" height="28"></a>
</p>

A CLI and C library for macOS, Windows and Linux. A snapshot returns JSON with a ref for every element an agent can act on. The agent acts on a ref and snapshots again to check, with no pixel matching; the loop stays in your agent.

Every CLI call runs in its own process. Headless calls still prohibit foreground activation and synthesized input.

Snapshots, clipboard reads, screenshots, command output and debug artifacts can contain private desktop content. Keep them out of public logs and uploads. The optional [JEV helper](skills/jev-desktop/SKILL.md) sends screen descriptions to a configured model provider; it is separate from the native CLI. See [privacy and data handling](docs/faq.md#what-data-can-contain-private-information).

## Installation

Install on macOS, Windows or Linux with npm:

```bash
npm install -g agent-desktop
agent-desktop version
```

Bun, Yarn and pnpm can install the same package. It includes native binaries and platform helpers for x64

... (truncated)