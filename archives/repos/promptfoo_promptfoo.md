# Promptfoo: LLM evals & red teaming

<p align="center">
  <a href="https://npmjs.com/package/promptfoo"><img src="https://img.shields.io/npm/v/promptfoo" alt="npm"></a>
  <a href="https://npmjs.com/package/promptfoo"><img src="https://img.shields.io/npm/dm/promptfoo" alt="npm"></a>
  <a href="https://github.com/promptfoo/promptfoo/actions/workflows/main.yml"><img src="https://img.shields.io/github/actions/workflow/status/promptfoo/promptfoo/main.yml" alt="GitHub Workflow Status"></a>
  <a href="https://github.com/promptfoo/promptfoo/blob/main/LICENSE"><img src="https://img.shields.io/github/license/promptfoo/promptfoo" alt="MIT license"></a>
  <a href="https://discord.gg/promptfoo"><img src="https://img.shields.io/discord/1146610656779440188?logo=discord&label=promptfoo" alt="Discord"></a>
</p>

<p align="center">
  <code>promptfoo</code> is a CLI and library for evaluating and red-teaming LLM apps. Stop the trial-and-error approach - start shipping secure, reliable AI apps.
</p>

<p align="center">
  <a href="https://www.promptfoo.dev">Website</a> ·
  <a href="https://www.promptfoo.dev/docs/getting-started/">Getting Started</a> ·
  <a href="https://www.promptfoo.dev/docs/red-team/">Red Teaming</a> ·
  <a href="https://www.promptfoo.dev/docs/">Documentation</a> ·
  <a href="https://discord.gg/promptfoo">Discord</a>
</p>

## Quick Start

```sh
npm install -g promptfoo
promptfoo init --example getting-started
```

Also available via `brew install promptfoo` and `pip install promptfoo`. You can also use `npx promptfoo@latest` to run any command without installing.

Most LLM providers require an API key. Set yours as an environment variable:

```sh
export OPENAI_API_KEY=sk-abc123
```

Once you're in the example directory, run an eval and view results:

```sh
cd getting-started
promptfoo eval
promptfoo view
```

See [Getting Started](https://www.promptfoo.dev/docs/getting-started/) (evals) or [Red Teaming](https://www.promptfoo.dev/docs/red-team/) (vulnerability scannin

... (truncated)