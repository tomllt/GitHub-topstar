# SkillSpector

**Security scanner for AI agent skills.** Detect vulnerabilities, malicious patterns, and security risks before installing agent skills.

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

## Overview

AI agent skills (used by Claude Code, Codex CLI, Gemini CLI, etc.) execute with implicit trust and minimal vetting. Research shows that **26.1% of skills contain vulnerabilities** and **5.2% show likely malicious intent**.

SkillSpector helps you answer: **"Is this skill safe to install?"**

## Documentation

- **[Development guide](docs/DEVELOPMENT.md)** — Architecture, package layout, and how to extend the analyzer pipeline.

## Features

- **Multi-format input**: Scan Git repos, URLs, zip files, directories, or single files
- **64 vulnerability patterns** across 16 categories: prompt injection, data exfiltration, privilege escalation, supply chain, excessive agency, output handling, system prompt leakage, memory poisoning, tool misuse, rogue agent, trigger abuse, dangerous code (AST), taint tracking, YARA signatures, MCP least privilege, and MCP tool poisoning
- **Two-stage analysis**: Fast static analysis + optional LLM semantic evaluation
- **Live vulnerability lookups**: SC4 queries [OSV.dev](https://osv.dev) for real-time CVE data with automatic offline fallback
- **Multiple output formats**: Terminal, JSON, Markdown, and SARIF reports
- **Risk scoring**: 0-100 score with severity labels and clear recommendations

## Quick Start

### Installation

Create and activate a virtual environment first (all `make` targets assume the venv is active). Use **uv** or **pip**; the Makefile uses `uv` if available, otherwise `pip`.

```bash
# Clone the repository
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

# Create and activate virtual environment
uv ve

... (truncated)