# <img src="./.github/img/modern-web-guidance.svg" alt="Modern Web Guidance" width="30" height="30"> Modern Web Guidance (Source)

This repo is the source repository for [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance) and includes the code and documentation for authoring, calibrating, and evaluating its contents.

[**Modern Web Guidance**](https://developer.chrome.com/docs/modern-web-guidance) is a set of skills that embed web platform expertise, best practices, and browser compatibility data directly into your coding agents. It helps to steer your coding agents away from legacy patterns, and instead toward solutions that harness the power and capabilities of the modern web platform.

See [CONTRIBUTING.md](./CONTRIBUTING.md) and [GOVERNANCE.md](./GOVERNANCE.md) for how we work on the project and orientation of the codebase.

---

*Stewarded by the Google Chrome, Microsoft Edge, Mozilla Firefox, and MDN teams, alongside the web development community.*

[Documentation](https://developer.chrome.com/docs/modern-web-guidance) · [Eval Dashboard](https://googlechrome.github.io/modern-web-guidance-src/) · [Source Code](https://github.com/GoogleChrome/modern-web-guidance-src) · [Report an Issue](https://github.com/GoogleChrome/modern-web-guidance-src/issues)

## <img src="https://github.com/GoogleChrome/modern-web-guidance/raw/main/.github/img/terminal.svg" width="24" height="24" style="vertical-align: middle; margin-right: 4px;"> Quickstart

```shell
npx modern-web-guidance@latest install
```

This command runs an interactive wizard to install Modern Web Guidance. See [Alternative Installation Methods](#-alternative-installation-methods) below.

#### Try it out (without installing)

```shell
# Search for relevant guides
npx modern-web-guidance@latest search "animate a dialog modal backdrop"

# Retrieve a guide by ID
npx modern-web-guidance@latest retrieve "animate-to-from-top-layer"

# Scan a codebase for legacy patterns to modernize


... (truncated)