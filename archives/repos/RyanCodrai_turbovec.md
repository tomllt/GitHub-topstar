<p align="center">
  <img src="docs/header.png" alt="turbovec — Google's TurboQuant for vector search" width="100%">
</p>

<p align="center">
  <a href="https://github.com/RyanCodrai/turbovec/blob/main/LICENSE"><img src="https://img.shields.io/pypi/l/turbovec" alt="License"></a>
  <a href="https://pypi.org/project/turbovec/"><img src="https://img.shields.io/pypi/v/turbovec?label=pypi&color=blue" alt="PyPI version"></a>
  <a href="https://crates.io/crates/turbovec"><img src="https://img.shields.io/crates/v/turbovec?label=crates.io&color=blue" alt="crates.io version"></a>
  <a href="https://arxiv.org/abs/2504.19874"><img src="https://img.shields.io/badge/paper-arXiv-b31b1b.svg" alt="TurboQuant paper"></a>
</p>

---

**A 10 million document corpus takes 31 GB of RAM as float32. turbovec fits it in 4 GB - and searches it faster than FAISS.**

turbovec is a Rust vector index with Python bindings, built on Google Research's [**TurboQuant**](https://arxiv.org/abs/2504.19874) algorithm — a data-oblivious quantizer that matches the Shannon lower bound on distortion, with no codebook training and no separate train phase.

- **Online ingest.** Add vectors, they're indexed — no train step, no parameter tuning, no rebuilds as the corpus grows.
- **Faster than FAISS.** Hand-written NEON (ARM) and AVX-512BW (x86) kernels beat FAISS IndexPQFastScan by 12–20% on ARM and match-or-beat it on x86.
- **Filter at search time.** Pass an id allowlist (or a slot bitmask) to `search()` and the kernel honours it directly. You always get up to `k` results from the allowed set — no over-fetching, no recall hit on selective filters.
- **Pure local.** No managed service, no data leaving your machine or VPC. Pair with any open-source embedding model for a fully air-gapped RAG stack.

Building RAG where privacy, memory, or latency matters? **You're in the right place.**

## Python

```bash
pip install turbovec
```

```python
from turbovec import TurboQuantIndex

index = TurboQuantIndex(dim=1536, bi

... (truncated)