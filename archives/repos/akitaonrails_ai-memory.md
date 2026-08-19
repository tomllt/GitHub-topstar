<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/logo-dark.png">
    <img alt="ai-memory" src="docs/logo-light.png" width="480">
  </picture>
</p>

> Long-term memory for AI coding agents. Quit Claude Code mid-task,
> start OpenAI Codex in the same directory, continue without
> re-explaining the architecture, the failed approaches, or the open
> questions.

[![Release](https://img.shields.io/github/v/release/akitaonrails/ai-memory)](https://github.com/akitaonrails/ai-memory/releases/latest)
[![Rust](https://img.shields.io/badge/rust-1.95+-blue)](rust-toolchain.toml)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

## Support Matrix

| Area | Status | Notes |
|---|---|---|
| Linux | Supported | Primary Docker/server target and CI platform. Published Docker images support `linux/amd64` and `linux/arm64`. Native Arch/AUR packages include system and user systemd units. |
| macOS | Supported | Workspace tests run in CI; tagged releases publish native `ai-memory-macos-aarch64.tar.gz` and `ai-memory-macos-x86_64.tar.gz` binaries. The native binary is the recommended path on Apple Silicon. See [`docs/macos.md`](docs/macos.md). |
| Windows via WSL2 | Supported | Use the Linux install path inside WSL2 when the agent runs there. |
| Native Windows | Experimental | Tagged releases publish `ai-memory-windows-x86_64.zip` with `ai-memory.exe`; Docker Desktop wrapper and source builds are also available. Local supported profiles default to host-native hook commands; Claude Code may use its Windows exec form, while other agents use native single command strings matching their hook schema. PowerShell/Git Bash scripts are compatibility fallbacks. See [`docs/windows.md`](docs/windows.md). |
| Claude Code | Supported | MCP config + lifecycle hooks; native commands enforce capture exclusions. `install-mcp --session-aware` optionally enables per-session auto-scope isolation through a local stdio bridge. Optionally captures t

... (truncated)