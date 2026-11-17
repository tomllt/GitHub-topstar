<div align="center">

# ![SkillEvaluator](https://raw.githubusercontent.com/NVIDIA/SkillEvaluator/ad2815fe78c045db91d230681d32863698da08cf/docs/assets/skillevaluator-wordmark.svg)

<h4>Evaluate and improve AI agent skills and plugins: quality, security, overlap, compatibility, and real impact across agents</h4>

[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12%20%7C%203.13%20%7C%203.14-blue.svg)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/skillevaluator.svg?label=PyPI)](https://pypi.org/project/skillevaluator/)
[![Documentation](https://img.shields.io/badge/Documentation-docs.nvidia.com-blue.svg)](https://docs.nvidia.com/skills/skillevaluator/)
[![Paper](https://img.shields.io/badge/arXiv-2608.20614-b31b1b.svg)](https://arxiv.org/abs/2608.20614)
[![Blog](https://img.shields.io/badge/Blog-NVIDIA%20Developer-76B900.svg)](https://developer.nvidia.com/blog/evaluating-ai-agent-skill-performance-with-nvidia-skillevaluator/)
[![Stars](https://img.shields.io/github/stars/NVIDIA/SkillEvaluator)](https://github.com/NVIDIA/SkillEvaluator/stargazers)
[![Forks](https://img.shields.io/github/forks/NVIDIA/SkillEvaluator)](https://github.com/NVIDIA/SkillEvaluator/forks)

</div>

> 📺 **Livestream:** [Ask the Experts: Evaluating Agent Skills](https://www.youtube.com/watch?v=4rI0zATFxYI)

SkillEvaluator checks AI agent skills and plugins, and measures a skill's effect
on task results: start with quality checks, then compare runs with and without a skill.

Agent skills are folders of instructions and supporting files defined by the
[Agent Skills specification](https://agentskills.io/). SkillEvaluator is part of
the [NVIDIA Verified Skills pipeline](https://github.com/NVIDIA/skills).

## Get started

Install the CLI in a Python 3.12–3.14 environment:

```bash
pip install skillevaluator
```

<details><summary>Or use uv</summary>

```bash
uv tool install --python 3.13 skillevaluator


... (truncated)