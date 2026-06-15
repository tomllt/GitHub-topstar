> ![NEW](https://img.shields.io/badge/%E2%9C%A8_NEW-8250df?style=for-the-badge)
> ## OpenCoworker
> **An AI agent that lives on your desktop, built on aisuite.**
>
> OpenCoworker is a desktop AI agent that can not only chat, but also do deep research and carry out tasks for
> you on your computer. It can read files (with permission) to gain context, read/send messages (slack, email, etc.),
> and create real deliverables like PDF reports, documents, spreadsheets. It also supports scheduled automations,
> such as providing you a daily news summary. 
>
> Requires bringing your own API key (OpenAI, Anthropic, Google) or run fully local with Ollama. Your data stays on your machine.
>
> [**⬇ Download for macOS**](https://github.com/andrewyng/aisuite/releases/latest/download/OpenCoworker-macos-arm64.dmg)
> <sub>&nbsp;&nbsp;macOS 13+ (Apple Silicon)</sub> &nbsp;&nbsp;
> 
> [**⬇ Download for Windows**](https://github.com/andrewyng/aisuite/releases/latest/download/OpenCoworker-windows-setup.exe)
> <sub>&nbsp;&nbsp;Windows 10/11 (x64) &nbsp;·&nbsp; </sub>
>
> [**Quickstart:**](docs/opencoworker-quickstart.md) — install, connect a model, first tasks, automations.
> 
> Its source lives in this repository under `platform/` — a working reference for building your own agent harness on aisuite.

<br>

#  aisuite

[![PyPI](https://img.shields.io/pypi/v/aisuite)](https://pypi.org/project/aisuite/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

`aisuite` is a lightweight Python library for building with LLMs, in two layers: a unified **Chat Completions API** across providers, and an **Agents API** with tools and toolkits on top. This repo is also home to **OpenCoworker**, a desktop AI coworker built using aisuite:

```text
┌───────────────────────────────────────────────┐
│                 OpenCoworker                  │   agent harness for doing everyday tasks
├───────────────────────────────────────────────┤
│        

... (truncated)