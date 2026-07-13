# dcg (Destructive Command Guard)

<div align="center">
  <img src="illustration.webp" alt="Destructive Command Guard - Protecting your code from accidental destruction">
</div>

<div align="center">

[![Coverage](https://img.shields.io/codecov/c/github/Dicklesworthstone/destructive_command_guard?label=coverage)](https://codecov.io/gh/Dicklesworthstone/destructive_command_guard)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

A high-performance hook for AI coding agents that blocks destructive commands before they execute, protecting your work from accidental deletion across Claude Code, Codex CLI, Gemini CLI, Copilot CLI, VS Code Copilot Chat, Cursor, Hermes Agent, Grok (xAI), and related tools.

**Supported:** [Claude Code](https://claude.ai/code), [Codex CLI 0.125.0+](https://github.com/openai/codex), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-hooks), [VS Code Copilot Chat](https://code.visualstudio.com/docs/agent-customization/hooks), [Cursor IDE](https://cursor.com), [Hermes Agent](https://github.com/NousResearch/hermes-agent), [Grok (xAI)](https://x.ai/news/grok-build-cli) (native `~/.grok/hooks/` plus Claude compatibility layer), [Antigravity CLI (`agy`)](https://antigravity.google) (native `~/.gemini/config/hooks.json` via `dcg install --agy`), [OpenCode](https://opencode.ai) (via [community plugin](https://github.com/aspiers/ai-config/blob/main/.config/opencode/plugins/dcg-guard.js)), [Pi](https://github.com/earendil-works/pi) (via [extension recipe](docs/pi-integration.md)), [Aider](https://aider.chat/) (limited—git hooks only), [Continue](https://continue.dev) (detection only)

<div align="center">
<h3>Quick Install</h3>

```bash
curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/destructive_command_guard/main/install.sh?$(date +%s)" | bash -s -- --easy-mode
```

<p><em

... (truncated)