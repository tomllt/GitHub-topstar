<div align="center">

**简体中文** | [繁體中文](README.zh-TW.md) | [English](README.en.md) | [日本語](README.ja.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [Čeština](README.cs.md)

![Banner](docs/images/DiscImageStudio_Banner_2.png)

<h2>全能的光盘盘面可见图像生成与刻录工具</h2>

Disc Image Studio 是一个多平台的光盘盘面图像生成与刻录工具，帮助您使用任何刻录光驱在任何 DVD / CD / 单层蓝光 光盘上刻蚀出肉眼可见的图像。

![.NET 版本](https://img.shields.io/badge/.NET-10.0-512bd4?style=flat-square)
![运行平台](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-0078d6?style=flat-square)
![开发语言](https://img.shields.io/badge/Language-C%23-68217A?style=flat-square)
![GitHub Repo size](https://img.shields.io/github/repo-size/JiaFeiMiao-K-Cat/DiscImageStudio?style=flat-square&color=3cb371)
![贡献欢迎](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square)
[![许可证：GPL-3.0-or-later](https://img.shields.io/badge/License-GPL--3.0--or--later-blue?style=flat-square)](LICENSE)

</div>

---

## 效果预览

![](docs/images/case1.jpg)

![](docs/images/case2.jpg)

---

## 概述

Disc Image Studio 可将一张图片转换成符合 CD、DVD 与单层 BD-R 光盘物理层约束的数据，刻录后将使光盘盘面呈现肉眼可见的图案。

## 界面预览

![主页：模板与最近工程](docs/images/ui-home.png)

![设计页：图层画布与影调](docs/images/ui-design.png)

![导出页：浅色主题与输出镜像](docs/images/ui-export.png)

---

## 快速开始

Windows 下载 `win-x64.exe` 后可直接运行。Linux 或 macOS 请下载与 CPU 匹配的**实验性 CLI** 压缩包，解压后运行 `./disc-image-studio --help`。这些发布包均自带 .NET 运行时。 [GitHub Releases](https://github.com/JiaFeiMiao-K-Cat/DiscImageStudio/releases)

### 1. 新建工程

在主页选择 CD、DVD 或蓝光，指定输出位置后创建工程。

### 2. 设计盘面

在设计页导入图片，用图层完成排版，并在右栏「影调」模块调整抖动、伽马、亮度与灰阶档位。

### 3. 预览与导出

在预览页核对盘面投影，在导出页生成 ISO / RAW / WAV+CUE，或使用即时刻录功能直接写入空白盘片。

即时刻录为实验性功能，请只使用可报废的测试介质。

## 功能

### 光盘数据生成

- **CD 支持**：支持任何 CD 。您可导出带格式头的 WAV 音轨及配套 CUE，兼容 cdrecord, ImgBurn等刻录软件；也允许导出 RAW 音轨。详见 [CD 刻录兼容说明](docs/CD_AUDIO_COMPATIBILITY.md)。
- **DVD 支持**：支持任何 DVD。您可导出 ISO 镜像。
- **蓝光支持**：支持任何单层 BD-R 25 GB，支持纯绘图与 UDF 2.01 文件。详见 [ADDING_BLURAY.md](docs/ADDING_BLURAY.md)。
- **随盘文件**：CD／DVD／蓝光可在设计页直接选择要保存的文件夹及内圈／外圈位置，也可在导出页调整；设置随工

... (truncated)