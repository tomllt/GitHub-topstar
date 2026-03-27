# Insanely Fast Whisper

An opinionated CLI to transcribe Audio files w/ Whisper on-device! Powered by 🤗 *Transformers*, *Optimum* & *flash-attn*

**TL;DR** - Transcribe **150** minutes (2.5 hours) of audio in less than **98** seconds - with [OpenAI's Whisper Large v3](https://huggingface.co/openai/whisper-large-v3). Blazingly fast transcription is now a reality!⚡️

```
pipx install insanely-fast-whisper==0.0.15 --force
```

<p align="center">
<img src="https://huggingface.co/datasets/reach-vb/random-images/resolve/main/insanely-fast-whisper-img.png" width="615" height="308">
</p>

Not convinced? Here are some benchmarks we ran on a Nvidia A100 - 80GB 👇

| Optimisation type    | Time to Transcribe (150 mins of Audio) |
|------------------|------------------|
| large-v3 (Transformers) (`fp32`)             | ~31 (*31 min 1 sec*)             |
| large-v3 (Transformers) (`fp16` + `batching [24]` + `bettertransformer`) | ~5 (*5 min 2 sec*)            |
| **large-v3 (Transformers) (`fp16` + `batching [24]` + `Flash Attention 2`)** | **~2 (*1 min 38 sec*)**            |
| distil-large-v2 (Transformers) (`fp16` + `batching [24]` + `bettertransformer`) | ~3 (*3 min 16 sec*)            |
| **distil-large-v2 (Transformers) (`fp16` + `batching [24]` + `Flash Attention 2`)** | **~1 (*1 min 18 sec*)**           |
| large-v2 (Faster Whisper) (`fp16` + `beam_size [1]`) | ~9.23 (*9 min 23 sec*)            |
| large-v2 (Faster Whisper) (`8-bit` + `beam_size [1]`) | ~8 (*8 min 15 sec*)            |

P.S. We also ran the benchmarks on a [Google Colab T4 GPU](/notebooks/) instance too!

P.P.S. This project originally started as a way to showcase benchmarks for Transformers, but has since evolved into a lightweight CLI for people to use. This is purely community driven. We add whatever community seems to have a strong demand for! 

## 🆕 Blazingly fast transcriptions via your terminal! ⚡️

We've added a CLI to enable fast transcriptions. Here's how you can use it:

Install `insanely-fast-

... (truncated)