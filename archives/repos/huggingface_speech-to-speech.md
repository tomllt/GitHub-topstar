<div align="center">
  <div>&nbsp;</div>
  <img src="https://raw.githubusercontent.com/huggingface/speech-to-speech/main/logo.png" width="600"/>

# Speech To Speech: Build voice agents with open-source models

[![PyPI](https://img.shields.io/pypi/v/speech-to-speech)](https://pypi.org/project/speech-to-speech/)
[![Python](https://img.shields.io/pypi/pyversions/speech-to-speech)](https://pypi.org/project/speech-to-speech/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](./LICENSE)

</div>

A low-latency, fully modular voice-agent pipeline: **VAD -> STT -> LLM -> TTS**, exposed through an **OpenAI Realtime-compatible WebSocket API**. Every component is swappable. The LLM slot speaks OpenAI-compatible protocols, so you can point it at a hosted provider, at [HF Inference Providers](https://huggingface.co/inference-providers), or at a vLLM or llama.cpp server on your own hardware for a fully local, fully open stack.

This pipeline runs in production as the conversation backend for thousands of [Reachy Mini](https://huggingface.co/blog/reachy-mini) robots.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./docs/assets/endpoint-swap-dark.gif">
    <source media="(prefers-color-scheme: light)" srcset="./docs/assets/endpoint-swap-light.gif">
    <img src="./docs/assets/endpoint-swap-light.gif" alt="Switching an OpenAI Realtime client endpoint from hosted OpenAI to a self-hosted speech-to-speech server" width="640">
  </picture>
</p>

## Quickstart

```bash
pip install speech-to-speech
export OPENAI_API_KEY=...
speech-to-speech
```

This starts an OpenAI Realtime-compatible server at `ws://localhost:8765/v1/realtime` using Parakeet TDT for local STT, an OpenAI-compatible LLM, and Qwen3-TTS for local speech output.

From a source checkout, talk to it from a second terminal:

```bash
python scripts/listen_and_play_realtime.py --host 127.0.0.1 --port 8765
```

Prefer to keep the LLM on your own machine? Serve Gemma 4 wi

... (truncated)