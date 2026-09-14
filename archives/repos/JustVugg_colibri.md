<p align="center">
  <img src="assets/colibri-logo.svg" width="560" alt="colibrì — tiny engine, immense model">
</p>

<p align="center">
  <a href="https://justvugg.github.io/colibri"><img src="https://img.shields.io/badge/website-justvugg.github.io%2Fcolibri-1f6feb" alt="Website"></a>
  <a href="https://github.com/JustVugg/colibri/releases"><img src="https://img.shields.io/github/v/release/JustVugg/colibri?color=2ea043" alt="Latest release"></a>
</p>

<p align="center">
  <a href="https://justvugg.github.io/colibri"><b>Website</b></a> ·
  <a href="https://discord.gg/RXV83nSZdk"><b>Discord</b></a> ·
  English · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.it.md">Italiano</a>
</p>

**Tiny engine, immense model.** Run **frontier MoE models — 744B to 2.8T
parameters** — on consumer and heterogeneous hardware, in pure C with zero
engine dependencies, by treating storage, RAM, and VRAM as a single inference
hierarchy (AI memory multitiering).

Nine families run today: **GLM-5.2/5.3** (744B), **GLM-5.3-Flash** (321B, with
vision), **Inkling** (975B), **Kimi K3** (2.8T), **DeepSeek V4 Flash** (284B), **DeepSeek V4.1 Flash** (552B, with vision),
**Qwen3.8-Flash-Next** (125B + 51B n-gram), **Qwen3.6** (35B-A3B) and
**OLMoE** (7B) —
one C file each, the same `coli chat` / `coli serve` / `coli web` front end.
[Full roster ↓](#other-supported-models)

> **Colibrì is an inference engine you can run today, and an open research
> platform.** Its primary goal is to pursue inference-side performance across
> the entire software/hardware boundary — model formats, memory hierarchy,
> storage I/O, placement, scheduling, kernels, speculation, and CPU/GPU
> overlap — so large models depend less on scarce hardware and cost less to run.

Colibrì treats VRAM, RAM, and storage as a single multitier hierarchy, and it is
deliberately a place to test aggressive systems ideas — so there is **no SLA on
speed, and a hard guarantee on semantics**: experi

... (truncated)