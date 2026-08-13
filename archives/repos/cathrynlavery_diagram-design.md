# Diagram Design

**Editorial diagrams your designer won't hate.**

![Content site architecture](docs/screenshots/architecture.png)

![The self-improving loop](docs/screenshots/loop.png)

*New in 2.0 — the Loop: flywheels with a shared-memory hub. The dashed lines are the write-backs.*

*New in 2.3: semantic system patterns and optional accessible motion, while static output stays the default.*

27 visual types. One agent skill for Claude Code, Codex, and Pi. Semantic patterns describe behavior separately from layout, so a queue, policy trace, or trust boundary can use the nearest existing type without expanding the type count. Static HTML remains the default; optional motion is available for ordered explanations. The skill also redraws draw.io or Mermaid sources at a chosen format, size, and detail level.

No Figma. No generic rounded boxes. No 30-minute color-picking sessions.

---

## Why I built it

I write at [littlemight.com](https://littlemight.com?utm_source=diagram-design&utm_medium=readme&utm_campaign=github&utm_content=intro) (and run [BestSelf.co](https://bestself.co?utm_source=diagram-design&utm_medium=readme&utm_campaign=github&utm_content=intro) on the side). Every time I needed a diagram — an architecture sketch, a flowchart, a pyramid of what matters most — I'd ask Claude and get back a generic rounded-box thing that looked nothing like the rest of the site. I'd either fight with Figma for 30 minutes or just skip the diagram.

So I built a Claude Code skill for it. Twenty-seven visual types, editorial quality, matches your brand in 60 seconds by reading your website.

> *The highest-quality move is usually deletion.* Every node earns its place. The accent color is reserved for the 1–2 things the reader should look at first. Target density: 4/10.

---

## What it makes

All 27 visual types ship in three static variants: minimal light, minimal dark, and full-editorial. Open any of them directly in a browser. There is no build step, JavaScript, or exte

... (truncated)