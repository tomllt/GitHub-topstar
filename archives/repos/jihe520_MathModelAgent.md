<h1 align="center">🤖 MathModelAgent 📐</h1>
<p align="center">
    <img src="./docs/icon.png" height="250px">
</p>
<h4 align="center">
    专为数学建模设计的 Agent<br>
    自动完成数学建模，生成一份完整的可以直接提交的论文。
</h4>

<h5 align="center">简体中文 | <a href="README_EN.md">English</a></h5>

<p align="center">
    <a href="https://github.com/jihe520/MathModelAgent/releases/latest"><b>⬇️ 下载最新桌面版（推荐）</b></a>
</p>
<p align="center">
    🎨 姊妹项目：<a href="https://github.com/jihe520/sci-box"><b>sci-box</b></a> —— 科研图表 & 流程图 SKILL 合集
</p>

---

## 🖥️ 桌面版（推荐使用方式）

> **不想折腾环境？直接下载桌面版，开箱即用。**
>
> 👉 **[前往 Releases 下载最新版本](https://github.com/jihe520/MathModelAgent/releases/latest)**

桌面版已内置 Claude Code 与全套 MathModelAgent SKILLS，无需安装 Python / Node.js / Redis，也无需手动配置 SKILL，装好填一个模型 API Key 即可开始建模。

| 系统 | 下载文件 |
|------|----------|
| macOS（Apple 芯片 M 系列） | `mathmodel-<version>-arm64.dmg` |
| macOS（Intel 芯片） | `mathmodel-<version>-x64.dmg` |
| Windows 64 位 | `mathmodel-<version>-x64.exe` |

macOS 安装包已 Developer ID 签名并通过 Apple 公证。

> [!TIP]
> 不确定自己的 Mac 是哪种芯片？点击左上角  → 关于本机，看「芯片」一栏：显示 Apple M 系列选 arm64，显示 Intel 选 x64。

> [!WARNING]
> Windows 安装包当前未签名，首次安装或运行时可能出现 Microsoft Defender SmartScreen 提示，请选择「更多信息」→「仍要运行」，并务必从官方 [Releases 页面](https://github.com/jihe520/MathModelAgent/releases/latest) 下载。

安装后应用会自动检查更新（macOS 支持自动更新，Windows 待代码签名证书配置完成后启用）。

如果你是开发者，想自行部署或参与贡献，请继续阅读下方的 [SKILLS](#skills) 与 [使用教程](#-使用教程)。

---

## 🌟 愿景：

3 天的比赛时间变为 1 小时
自动完整一份可以获奖级别的建模论文

<p align="center">
    <img src="./docs/chat.png">
    <img src="./docs/coder.png">
</p>

## ✨ 功能特性

- 🔍 自动分析问题，数学建模，编写代码，纠正错误，撰写论文
- 💻 Code Interpreter
    - local Interpreter: 基于 jupyter , 代码保存为 notebook 方便再编辑
    - 云端 code interpreter: [E2B](https://e2b.dev/) 和 [daytona](https://app.daytona.io/)
- 📝 生成一份编排好格式的论文
- 🤝 multi-agents: 建模手，代码手，论文手等
- 🔄 multi-llms: 每个 agent 设置不同的、合适的模型
- 🤖 支持所有模型: [litellm](https://docs.litellm.ai/docs/providers)
- 💰 成本低：workflow agentless，不依赖 agent 框架
- 🧩 自定义模板：prompt inject 为每个 subtask 单独设置需求
- 🌐 Web Search: Agent 自主搜索互联网获取真实数

... (truncated)