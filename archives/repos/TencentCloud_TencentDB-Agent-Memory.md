
<div align="center">

<img src="./assets/images/logo.png" alt="TencentDB Agent Memory" width="880" />

### Agents remember. Humans innovate.

<a href="https://trendshift.io/repositories/29310?utm_source=repository-badge&amp;utm_medium=badge&amp;utm_campaign=badge-repository-29310" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/repositories/29310" alt="TencentCloud%2FTencentDB-Agent-Memory | Trendshift" width="250" height="55"/></a>

[![npm](https://img.shields.io/npm/v/@tencentdb-agent-memory/memory-tencentdb?color=blue)](https://www.npmjs.com/package/@tencentdb-agent-memory/memory-tencentdb)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Node](https://img.shields.io/badge/node-%3E=22.16-brightgreen)](https://nodejs.org/)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-%3E=2026.3.13-orange)](https://github.com/openclaw/openclaw)
[![Hermes](https://img.shields.io/badge/Hermes-Gateway-7B61FF)](https://hermes-agent.nousresearch.com/docs/)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white)](https://discord.gg/dJQM6mKMF)

[Installation](#installation) · [What is it?](#what-is-tencentdb-agent-memory) · [Team Play](#one-play-style-build-a-growing-agent-team-for-a-one-person-company) · [Technical Implementation](#technical-implementation) · [Benchmark](#benchmark)

[**English**](./README.md) · [简体中文](./README_CN.md)

</div>

---

> **Latest:** Team Memory Beta is evolving quickly — install it and start exploring in minutes.

<td>
   <video src="https://github.com/user-attachments/assets/efb1a808-1f86-4cfe-802c-f7453f7ca938" width="100%" controls autoplay loop muted playsinline></video>
</td>

# Installation

Start all three services in one go (`memory-core` + `memory-hub` + `proxy`):

```bash
git clone https://github.com/Tencent/TencentDB-Agent-Memory.git
cd TencentDB-Agent-Memory/deploy/global-images
cp .env.example .env
$EDITOR .env       # Fill in two set

... (truncated)