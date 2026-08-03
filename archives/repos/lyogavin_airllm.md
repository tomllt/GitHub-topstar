![airllm_logo](https://github.com/lyogavin/airllm/blob/main/assets/airllm_logo_sm.png?v=3&raw=true)

[**Quickstart**](#quickstart) | 
[**Configurations**](#configurations) | 
[**MacOS**](#macos) | 
[**Example notebooks**](#example-python-notebook) | 
[**FAQ**](#faq)

**AirLLM** dramatically reduces inference memory usage, letting 70B large language models run on a single 4GB GPU card — without quantization, distillation, or pruning. You can even run **405B Llama 3.1** on **8GB**, **DeepSeek-V3 (671B)** on **~12GB**, and **Kimi K3 (2.8T)** — the largest open-source model released to date — on **under 4GB**, because sparse MoE models stream one expert at a time rather than a whole layer.

<a href="https://github.com/lyogavin/airllm/stargazers">![GitHub Repo stars](https://img.shields.io/github/stars/lyogavin/airllm?style=social)</a>
[![Downloads](https://static.pepy.tech/personalized-badge/airllm?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads)](https://pepy.tech/project/airllm)

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/LianjiaTech/BELLE/blob/main/LICENSE)
[![Generic badge](https://img.shields.io/badge/wechat-Anima-brightgreen?logo=wechat)](https://static.aicompose.cn/static/wecom_barcode.png?t=1671918938)
[![Discord](https://img.shields.io/discord/1175437549783760896?logo=discord&color=7289da
)](https://discord.gg/2xffU5sn)
[![PyPI - AirLLM](https://img.shields.io/pypi/format/airllm?logo=pypi&color=3571a3)
](https://pypi.org/project/airllm/)
[![Website](https://img.shields.io/website?up_message=blog&url=https%3A%2F%2Fmedium.com%2F%40lyo.gavin&logo=medium&color=black)](https://medium.com/@lyo.gavin)
[![Website](https://img.shields.io/badge/Gavin_Li-Blog-blue)](https://gavinliblog.com)
[![Support me on Patreon](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Fshieldsio-patreon.vercel.app%2Fapi%3Fusername%3Dgavinli%26type%3Dpatrons&style=flat)](https://patreon

... (truncated)