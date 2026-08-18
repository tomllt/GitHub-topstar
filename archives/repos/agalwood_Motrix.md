<div>
  <img src="./public/app-icon.png" alt="Motrix" width="256" />
  <h1>Motrix</h1>
  <p>A modern, full-featured download manager that stays simple to use</p>
</div>

[![GitHub release](https://img.shields.io/github/v/release/agalwood/Motrix.svg)](https://github.com/agalwood/Motrix/releases) ![Build/release](https://github.com/agalwood/Motrix/workflows/Build/release/badge.svg) ![Total Downloads](https://img.shields.io/github/downloads/agalwood/Motrix/total.svg)

English | [简体中文](./README.zh-CN.md)

## Overview

Motrix is a clean, full-featured desktop download manager for HTTP, FTP, BitTorrent, magnet links, and more.

**Motrix Turbo** is Motrix v2, rebuilt from the ground up with Electron, React, and TypeScript while keeping the clean, straightforward experience of v1. The download core is independent of the UI. Browser extensions and command-line tools communicate with the app over **MDXP** (Motrix Download eXchange Protocol), an open protocol built on JSON-RPC 2.0, while plugins run in isolated sandboxes.

The same core powers two ways to run Motrix:

- **Desktop app:** Runs on macOS, Windows, and Linux
- **Headless server:** Runs without a desktop environment, either directly on Node.js or in Docker, and includes a web UI for NAS devices and home servers

## 🧪 Beta testing

Motrix Turbo v2 is currently in beta. After its remaining release gates pass,
download [v2.0.0-beta.18 from GitHub Releases](https://github.com/agalwood/Motrix/releases/tag/v2.0.0-beta.18)
and read the [full release notes](./docs/release-notes/2.0.0-beta.18.md) before
installing it.

Back up your existing Motrix data and downloads before testing. Migration from
Motrix v1 data has not yet been validated, so do not use your only copy of v1
data with this beta. When practical, test v2 in parallel using a separate OS
account, machine, or Docker data directory.

## Screenshots

### Dashboard

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./screenshots/motrix-dashboard-dark.we

... (truncated)