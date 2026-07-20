# 深入理解 AI Agent：设计原理与工程实践

**[English](README.en.md) | 中文 | [Tiếng Việt](README.vi.md) | [தமிழ்](README.ta.md)**

本仓库是《深入理解 AI Agent：设计原理与工程实践》一书的开源主仓库，包含**全书正文**与**配套示例代码**。全书正文、配图与配套实验代码全部开源，欢迎把实验亲手跑一遍、提 issue 和 PR。

## 📖 电子书

全书提供多种语言版本：

- **中文 PDF（原版）**：[`book/深入理解-AI-Agent-李博杰-v1.2.pdf`](book/深入理解-AI-Agent-李博杰-v1.2.pdf)
- **英文 PDF**（社区贡献翻译，by [@nsdevaraj](https://github.com/nsdevaraj)）：[`book-en/AI-Agents-in-Depth-Bojie-Li-v1.2.pdf`](book-en/AI-Agents-in-Depth-Bojie-Li-v1.2.pdf)
- **泰米尔语 PDF**（社区贡献翻译，by [@nsdevaraj](https://github.com/nsdevaraj)）：[`book-ta/AI-Agents-in-Depth-Bojie-Li-v1.2-ta.pdf`](book-ta/AI-Agents-in-Depth-Bojie-Li-v1.2-ta.pdf)
- **越南语 PDF**（社区贡献翻译，by [@toanalien](https://github.com/toanalien)）：[`book-vi/AI-Agents-in-Depth-Bojie-Li-v1.1-vi.pdf`](book-vi/AI-Agents-in-Depth-Bojie-Li-v1.1-vi.pdf)

中文正文与编译好的 PDF 位于 [`book/`](book/) 目录；英文、泰米尔语与越南语翻译为**社区贡献**，分别位于 [`book-en/`](book-en/)、[`book-ta/`](book-ta/) 与 [`book-vi/`](book-vi/) 目录，内容可能滞后于中文原版：

- **正文源码**：`book/introduction.md`（引言）、`book/chapter1.md` ~ `book/chapter10.md`（第一至第十章）、`book/afterword.md`（后记）
- **自行编译**：安装 pandoc、xelatex、ElegantBook 文档类与相关字体后，运行

  ```bash
  cd book && bash build_pdf.sh
  ```

  图表由 `book/gen_*_figs.py` 生成、存于 `book/images/`，排版细节见 `book/preamble.tex` 与 `book/*.lua`。

## 📑 内容速览（第 1–10 章）

全书围绕核心公式 **Agent = LLM + 上下文 + 工具** 展开，十章内容如下：

- **第 1 章 · Agent 基础知识**：从“模型即 Agent”的新范式出发，建立 **Agent = LLM + 上下文 + 工具** 的核心公式，并引入 Harness 工程——模型之外的一切工程能力，才是真正的竞争力所在。
- **第 2 章 · 上下文工程**：上下文决定 Agent 的能力上限。深入大模型 API 的上下文结构、KV Cache 友好设计、提示工程、动态提示词与 Agent Skills、状态栏元信息，以及上下文压缩策略。
- **第 3 章 · 用户记忆和知识库**：让 Agent 跨会话记住用户、并接入外部知识。涵盖用户记忆系统、RAG 基础管道，以及超越扁平文本的知识组织与检索（结构化索引、知识图谱等）。
- **第 4 章 · 工具**：工具是 Agent 的双手。讲工具分类与通用设计原则、MCP 协议与工具选择的挑战、感知/执行/协作三类工具，以及事件驱动的异步 Agent。
- **第 5 章 · Coding Agent 与代码生成**：代码是“能创造新工具的工具”，是通用 Agent 的元能力。以生产级 Coding Agent 为例，展示这一最强通用工具的完整实现。
- **第 6 章 · Agent 的评估**：把 Agent 的表现变成可比较的信号。从评估环境、数据集设计、指标体系，到统计显著性、可观测性、评估驱动选型，直至生产级内部评估与仿真环境。
- **第 7 章 · 模型后训练**：预训练、SFT、R

... (truncated)