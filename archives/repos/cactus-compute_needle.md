![Needle](assets/banner.png)

# Needle 2

Needle 2 is an open 45M-parameter model for tool calling, device use and structured extraction. The whole model is a single 14MB binary that runs a full session in about 28MB of RAM. It is built on our Simple Attention Network findings, compressed to CQ2-bit with Cactus Quants, and baked into its own engine. On the benchmarks below, Needle 2 trades wins with other small models like FunctionGemma 270M, LFM2.5 230M and Apple FM, at 5x to 70x smaller, and 2 bits against their f16.

This repository is the Python package: inference, LoRA fine-tuning, and export. `pip install cactus-needle`, describe your tools, and call them from Python. The inference engine is fetched once from Hugging Face and cached; there is nothing else to build.

- **Self-contained**: weights baked into a single 14MB engine; no separate model files to manage, and inference does no network.
- **Simple contract**: tool calls come back as structured data, text in, JSON out; a byte-level grammar compiled from your schemas constrains every token.
- **Confidence-gated**: every response carries a calibrated confidence score from a learned head; set a threshold, act above it, escalate below it.
- **Tool retrieval**: declare a large catalogue and a built-in retrieval head renders only the top five tools per turn, with the grammar constrained to that subset.
- **Bounded memory**: a 256-token sliding window with the tools pinned as KV sinks, so total memory stays near 28MB no matter how long the conversation runs.

Weights: [huggingface.co/Cactus-Compute/needle2](https://huggingface.co/Cactus-Compute/needle2) &middot; source: [github.com/cactus-compute/needle](https://github.com/cactus-compute/needle).

![Size-quality frontier: mobile-class and below](assets/frontier.png)

## Simple Attention Network

Needle 2 is a Simple Attention Network, our dense small-model recipe: a Hadamard MLP in place of the FFN, GQA attention, engram key-value memory, and multi-lane hyper-co

... (truncated)