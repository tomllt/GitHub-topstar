<div align="center">

<img src="assets/mempalace_logo.png" alt="MemPalace" width="240">

# MemPalace

Local-first AI memory. Verbatim storage, pluggable backend, 96.6% R@5 raw on LongMemEval — zero API calls.

[![][version-shield]][release-link]
[![][python-shield]][python-link]
[![][license-shield]][license-link]
[![][discord-shield]][discord-link]

</div>

> [!CAUTION]
> **Beware of impostor sites.** MemPalace has no other official websites. The **only** official sources are this **[GitHub repository](https://github.com/MemPalace/mempalace)**, the **[PyPI package](https://pypi.org/project/mempalace/)**, and the docs at **[mempalaceofficial.com](https://mempalaceofficial.com)**. Any other domain (including `.tech`, `.net`, or other `.com` variants) is an impostor and may distribute malware. Details and timeline: [docs/HISTORY.md](docs/HISTORY.md).

> [!IMPORTANT]
> **Claude Code sessions expire in 30 days without auto-save hooks wired.** [Read this →](https://github.com/MemPalace/mempalace/discussions/1388)
>
> Need the shortest recovery/setup path? Use the [Claude Code retention setup checklist](https://mempalaceofficial.com/guide/claude-code-retention.html).

---

## What it is

MemPalace stores your conversation history as verbatim text and retrieves
it with semantic search. It does not summarize, extract, or paraphrase.
The index is structured — people and projects become *wings*, topics
become *rooms*, and original content lives in *drawers* — so searches
can be scoped rather than run against a flat corpus.

The retrieval layer is pluggable. The current default is ChromaDB; the
interface is defined in [`mempalace/backends/base.py`](mempalace/backends/base.py)
and alternative backends can be dropped in without touching the rest of
the system.

Nothing leaves your machine unless you opt in.

Architecture, concepts, and mining flows:
[mempalaceofficial.com/concepts/the-palace](https://mempalaceofficial.com/concepts/the-palace.html).

---

## Install

MemPalace sh

... (truncated)