<p align="center">
  <a href="https://lightpanda.io"><img src="https://cdn.lightpanda.io/assets/images/logo/lpd-logo.png" alt="Logo" height=170></a>
</p>

<h1 align="center">Lightpanda Browser</h1>

<p align="center"><a href="https://lightpanda.io/">lightpanda.io</a></p>

<div align="center">

[![License](https://img.shields.io/github/license/lightpanda-io/browser)](https://github.com/lightpanda-io/browser/blob/main/LICENSE)
[![Twitter Follow](https://img.shields.io/twitter/follow/lightpanda_io)](https://twitter.com/lightpanda_io)
[![GitHub stars](https://img.shields.io/github/stars/lightpanda-io/browser)](https://github.com/lightpanda-io/browser)

</div>

Lightpanda is the open-source browser made for headless usage:

- Javascript execution
- Support of Web APIs (partial, WIP)
- Compatible with Playwright[^1], Puppeteer, chromedp through [CDP](https://chromedevtools.github.io/devtools-protocol/)

Fast web automation for AI agents, LLM training, scraping and testing:

- Ultra-low memory footprint (9x less than Chrome)
- Exceptionally fast execution (11x faster than Chrome)
- Instant startup

[<img width="350px" src="https://cdn.lightpanda.io/assets/images/github/execution-time.svg">
](https://github.com/lightpanda-io/demo)
&emsp;
[<img width="350px" src="https://cdn.lightpanda.io/assets/images/github/memory-frame.svg">
](https://github.com/lightpanda-io/demo)
</div>

_Puppeteer requesting 100 pages from a local website on a AWS EC2 m5.large instance.
See [benchmark details](https://github.com/lightpanda-io/demo)._

[^1]: **Playwright support disclaimer:**
Due to the nature of Playwright, a script that works with the current version of the browser may not function correctly with a future version. Playwright uses an intermediate JavaScript layer that selects an execution strategy based on the browser's available features. If Lightpanda adds a new [Web API](https://developer.mozilla.org/en-US/docs/Web/API), Playwright may choose to execute different code for the same s

... (truncated)