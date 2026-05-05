# 🐳 DeepSeek TUI

> **This terminal-native coding agent is built around DeepSeek V4's 1M-token context window and prefix cache capability. It is distributed as a single binary and requires no Node.js or Python runtime. It also includes an MCP client, a sandbox, and a durable task queue out of the box.**

[简体中文 README](README.zh-CN.md)

Before proceeding, ensure that `Node.js` and `npm` are installed.

```bash
node --version
npm --version
```

If `Node.js` and `npm` are not installed in your environment, refer to the installation guides provided below:

* English version: [https://nodejs.org/en/download](https://nodejs.org/en/download)
* Chinese version: [https://nodejs.org/zh-cn/download](https://nodejs.org/zh-cn/download)

Select the version that best matches your device specifications and operating system. 

Install the `deepseek-tui` now:

```bash
npm install -g deepseek-tui

# When installing deepseek-tui in China's internet environment, you can use an npm mirror to speed up the installation process.
# npm install -g deepseek-tui@latest --registry=https://registry.npmmirror.com
```

[![CI](https://github.com/Hmbown/DeepSeek-TUI/actions/workflows/ci.yml/badge.svg)](https://github.com/Hmbown/DeepSeek-TUI/actions/workflows/ci.yml)
[![npm](https://img.shields.io/npm/v/deepseek-tui)](https://www.npmjs.com/package/deepseek-tui)
[![crates.io](https://img.shields.io/crates/v/deepseek-tui-cli?label=crates.io)](https://crates.io/crates/deepseek-tui-cli)
[![DeepWiki](https://img.shields.io/badge/DeepWiki-Ask_AI-_.svg?style=flat&color=0052D9&labelColor=000000&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAyCAYAAAAnWDnqAAAAAXNSR0IArs4c6QAAA05JREFUaEPtmUtyEzEQhtWTQyQLHNak2AB7ZnyXZMEjXMGeK/AIi+QuHrMnbChYY7MIh8g01fJoopFb0uhhEqqcbWTp06/uv1saEDv4O3n3dV60RfP947Mm9/SQc0ICFQgzfc4CYZoTPAswgSJCCUJUnAAoRHOAUOcATwbmVLWdGoH//PB8mnKqScAhsD0kYP3j/Yt5LPQe2KvcXmGvRHcDnpxfL2zOYJ1mFwrryWTz0advv1Ut4CJgf5uhDuDj5eUcAUoahrdY/56ebRWeraTjMt/00Sh3UDtjgHtQNHwcRGOC98BJEAEymycmYcWwOprTgcB6VZ5

... (truncated)