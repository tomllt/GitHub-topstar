# agent-browser

Browser automation for AI agents: open pages, read them as an accessibility tree, and act on elements from the shell.

<p>
  <a href="https://vercel.com/labs#labs-products"><img alt="Vercel Labs Product" src="https://img.shields.io/badge/LABS-PRODUCT-0a0a0a.svg?style=for-the-badge&amp;logo=Vercel&amp;labelColor=000000" height="28"></a>
  <a href="https://www.npmjs.com/package/agent-browser"><img alt="npm version: agent-browser" src="https://img.shields.io/npm/v/agent-browser.svg?style=for-the-badge&amp;labelColor=000000" height="28"></a>
  <a href="https://github.com/vercel-labs/agent-browser/blob/main/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/github/license/vercel-labs/agent-browser.svg?style=for-the-badge&amp;labelColor=000000" height="28"></a>
  <a href="https://www.npmjs.com/package/agent-browser"><img alt="npm downloads per month: agent-browser" src="https://img.shields.io/npm/dm/agent-browser.svg?style=for-the-badge&amp;labelColor=000000&amp;label=npm%20downloads" height="28"></a>
  <a href="https://skills.sh/vercel-labs/agent-browser"><img alt="skills.sh" src="https://skills.sh/b/vercel-labs/agent-browser?style=for-the-badge" height="28"></a>
</p>

agent-browser is a native Rust CLI that gives an AI agent a browser it can drive one command at a time. `snapshot` returns the page as compact text with a ref such as `@e1` for each element. The agent acts on a ref, reads the page again to check the result, and repeats. The browser stays open between commands, so each step is one short shell call.

## Install

```bash
npm install -g agent-browser
agent-browser install           # download Chrome for Testing (first time only)
```

- **Homebrew:** `brew install agent-browser`, then `agent-browser install`.
- **Linux:** `agent-browser install --with-deps` also installs the browser's system libraries.
- **No install:** `npx agent-browser open example.com`.

Project installs, building from source, `upgrade`, and `doctor` are co

... (truncated)