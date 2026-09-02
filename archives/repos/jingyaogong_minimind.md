<div align="center">

![logo](./images/logo.png)

</div>

<div align="center">

![visitors](https://visitor-badge.laobi.icu/badge?page_id=jingyaogong/minimind)
[![GitHub Repo stars](https://img.shields.io/github/stars/jingyaogong/minimind?style=social)](https://github.com/jingyaogong/minimind/stargazers)
[![GitHub Code License](https://img.shields.io/github/license/jingyaogong/minimind)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/jingyaogong/minimind)](https://github.com/jingyaogong/minimind/commits/master)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/jingyaogong/minimind/pulls)
[![Collection](https://img.shields.io/badge/🤗-MiniMind%20%20Collection-blue)](https://huggingface.co/collections/jingyaogong/minimind-66caf8d999f5c7fa64f399e5)

</div>

<div align="center">

![GitHub Trend](https://trendshift.io/api/badge/repositories/12586)

</div>

<div align="center">
  <h3>"大道至简"</h3>
</div>

<div align="center">

中文 | [English](./README_en.md)

</div>

* 此开源项目旨在完全从 0 开始，仅用 3 块钱成本与 2 小时训练时间，即可训练出规模约为 64M 的超小语言模型 MiniMind。
* MiniMind 系列极其轻量，主线最小版本体积约为 GPT-3 的 $\frac{1}{2700}$，力求让普通个人 GPU 也能快速完成训练与复现。
* 项目同时开源了大模型的极简结构与完整训练链路，覆盖 MoE、数据清洗、预训练（Pretrain）、监督微调（SFT）、LoRA、RLHF（DPO）、RLAIF（PPO / GRPO / CISPO）、Tool Use、Agentic RL、自适应思考与模型蒸馏等全过程代码。
* MiniMind 同时拓展了视觉模态模型 [MiniMind-V](https://github.com/jingyaogong/minimind-v)、多模态 Omni 模型 [MiniMind-O](https://github.com/jingyaogong/minimind-o)、扩散语言模型（MiniMind-dLM）、线性模型（MiniMind-Linear），详见 [Discussion](https://github.com/jingyaogong/minimind/discussions)。
* 项目所有核心算法代码均从 0 使用 PyTorch 原生实现，不依赖第三方库提供的高层抽象接口。
* 这不仅是一个大语言模型全阶段开源复现项目，也是一套面向 LLM 入门与实践的教程。
* 希望此项目能为更多人提供一个可复现、可理解、可扩展的起点，一起感受创造的乐趣，并推动更广泛 AI 社区的进步。

> 注：本项目基于 Apache 2.0 协议开源，完全免费。“2 小时” 指 SFT 阶段在单张 NVIDIA 3090 上跑完 `1 epoch` 的实测耗时，“3 块钱” 指对应时段的 GPU 租用成本。

---

<div align="center">

![minimind-3](./images/minimind-3.gif)

[🔗 在线体验](https://www.modelscope.cn/studios/gongjy/MiniMind) | [🔗 视频介绍](https://www.

... (truncated)