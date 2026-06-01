![main image](https://cdn-images-1.medium.com/max/5200/1*r99Hq3YBd5FTTWLNYKKvPw.png)

<div align="center">

<!-- omit in toc -->
# Train LLM From Scratch
  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Contributions](https://img.shields.io/badge/Contributions-Welcome-blue) [![Docs](https://img.shields.io/badge/Docs-Available-success)](#step-by-step-code-explanation)

**I am Looking for a PhD position in AI**. [GitHub](https://github.com/FareedKhan-dev)

</div>

I implemented a transformer model from scratch using PyTorch, based on the paper [Attention is All You Need](https://arxiv.org/abs/1706.03762). You can use my scripts to train your own **billion** or **million** parameter LLM using a single GPU.

Below is the output of the trained 13 million parameter LLM:

```
In ***1978, The park was returned to the factory-plate that 
the public share to the lower of the electronic fence that 
follow from the Station's cities. The Canal of ancient Western 
nations were confined to the city spot. The villages were directly 
linked to cities in China that revolt that the US budget and in
Odambinais is uncertain and fortune established in rural areas.
```
<!-- omit in toc -->
## Table of Contents
- [Training Data Info](#training-data-info)
- [Prerequisites and Training Time](#prerequisites-and-training-time)
- [Code Structure](#code-structure)
- [Usage](#usage)
- [Step by Step Code Explanation](#step-by-step-code-explanation)
  - [Importing Libraries](#importing-libraries)
  - [Preparing the Training Data](#preparing-the-training-data)
  - [Transformer Overview](#transformer-overview)
  - [Multi Layer Perceptron (MLP)](#multi-layer-perceptron-mlp)
  - [Single Head Attention](#single-head-attention)
  - [Multi Head Attention](#multi-head-attention)
  - [Transformer Block](#transformer-block)
  - [The Final Model](#the-final-model)
  - [Batch Processing](#batch-processing)
  - [Training Parameters](#trai

... (truncated)