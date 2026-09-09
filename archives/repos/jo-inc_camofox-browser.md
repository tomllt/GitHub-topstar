<div align="center">
  <img src="fox.png" alt="camofox-browser" width="200" />
  <h1>camofox-browser</h1>
  <p><strong>Anti-detection browser server for AI agents, powered by Camoufox</strong></p>
  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" /></a>
    <a href="https://github.com/jo-inc/camofox-browser/stargazers"><img src="https://img.shields.io/github/stars/jo-inc/camofox-browser" alt="GitHub stars" /></a>
    <a href="https://www.npmjs.com/package/camofox-browser"><img src="https://img.shields.io/npm/v/camofox-browser" alt="npm version" /></a>
    <a href="https://github.com/jo-inc/camofox-browser/commits"><img src="https://img.shields.io/github/last-commit/jo-inc/camofox-browser" alt="GitHub last commit" /></a>
  </p>
  <p>
    Standing on the mighty shoulders of <a href="https://camoufox.com">Camoufox</a> - a Firefox fork with fingerprint spoofing at the C++ level.
  </p>
</div>

<br/>

> <a href="https://askjo.ai?ref=camofox"><img src="jo-logo.png" alt="Jo" width="80" height="80" align="left" /></a>
>
> Built by the team behind <a href="https://askjo.ai?ref=camofox"><strong>jo, a personal AI agent</strong></a> that runs half on your Mac, half on a dedicated cloud machine just for you -- with zero maintenance needed. Available on macOS, Telegram, WhatsApp, and email. <a href="https://askjo.ai?ref=camofox">Try the beta free -></a>

<br/>

```bash
git clone https://github.com/jo-inc/camofox-browser && cd camofox-browser
npm install && npm start
# -> http://localhost:9377
```

---

## Why

AI agents need to browse the real web. Playwright gets blocked. Headless Chrome gets fingerprinted. Stealth plugins become the fingerprint.

Camoufox patches Firefox at the **C++ implementation level** - `navigator.hardwareConcurrency`, WebGL renderers, AudioContext, screen geometry, WebRTC - all spoofed before JavaScript ever sees them. No shims, no wrappers, no tells.

This project wraps that engine in a REST API

... (truncated)