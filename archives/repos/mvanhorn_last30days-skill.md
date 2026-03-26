# /last30days v2.9.5

### Claude Code (recommended)
```
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days@last30days-skill
```

[![ClawHub](https://img.shields.io/badge/ClawHub-last30days--official-blue)](https://clawhub.ai/skills/last30days-official)

```bash
clawhub install last30days-official
```

**The AI world reinvents itself every month. This skill keeps you current.** /last30days researches your topic across Reddit, X, Bluesky, YouTube, TikTok, Instagram, Hacker News, Polymarket, and the web from the last 30 days, finds what the community is actually upvoting, sharing, betting on, and saying on camera, and writes you a grounded narrative with real citations. Whether it's Seedance 2.0 access, paper.design prompts, or the latest Nano Banana Pro techniques, you'll know what people who are paying attention already know.

**New in v2.9.5 — Bluesky, Comparative Mode, and Config Improvements:**

- **Bluesky/AT Protocol** is now a social source. Opt-in via `BSKY_HANDLE` + `BSKY_APP_PASSWORD` (create at bsky.app/settings/app-passwords). Full pipeline: search, score, dedupe, render.
- **Comparative mode** - ask "X vs Y" (e.g., `/last30 cursor vs windsurf`) and get 3 parallel research passes with a side-by-side comparison: strengths, weaknesses, head-to-head table, and a data-driven verdict.
- **Per-project .env config** - drop a `.claude/last30days.env` in your project root for per-project API keys.
- **SessionStart config check** - validates your config automatically when a Claude Code session starts.
- **Expanded test coverage** - 455+ tests across all modules.

**New in v2.9.1 — Auto-save to ~/Documents/Last30Days/:** Every run now saves the complete briefing as a topic-named `.md` file to your Documents folder. Build a personal research library automatically. Inspired by [@devin_explores](https://x.com/devin_explores).

**New in v2.9 — ScrapeCreators Reddit + Top Comments + Smart Discovery:**

Reddit now runs on [ScrapeCreators](https://

... (truncated)