# pdf-inspector

[![Crates.io](https://img.shields.io/crates/v/pdf-inspector.svg)](https://crates.io/crates/pdf-inspector)
[![npm](https://img.shields.io/npm/v/@firecrawl/pdf-inspector.svg)](https://www.npmjs.com/package/@firecrawl/pdf-inspector)
[![PyPI](https://img.shields.io/pypi/v/pdf-inspector.svg)](https://pypi.org/project/pdf-inspector/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Fast Rust library for PDF classification and text extraction. Detects whether a PDF is text-based or scanned, extracts text with position awareness, and converts to clean Markdown — all without OCR. Includes bindings for [Python](docs/python.md), [Node.js](napi/README.md), and [browser WebAssembly](wasm/README.md).

Built by [Firecrawl](https://firecrawl.dev) to handle text-based PDFs locally in under 200ms, skipping expensive OCR services for the ~54% of PDFs that don't need them.

## Features

- **Smart classification** — Detect TextBased, Scanned, ImageBased, or Mixed PDFs in ~10-50ms by sampling content streams. Returns a confidence score (0.0-1.0) and per-page OCR routing.
- **Text extraction** — Position-aware extraction with font info, X/Y coordinates, and automatic multi-column reading order.
- **Markdown conversion** — Headings (H1-H4 via font size ratios), bullet/numbered/letter lists, code blocks (monospace font detection), tables (rectangle-based and heuristic), bold/italic formatting, URL linking, and page breaks.
- **Table detection** — Dual-mode: rectangle-based detection from PDF drawing ops, plus heuristic detection from text alignment. Handles financial tables, footnotes, and continuation tables across pages.
- **CID font support** — ToUnicode CMap decoding for Type0/Identity-H fonts, UTF-16BE, UTF-8, and Latin-1 encodings.
- **Multi-column layout** — Automatic detection of newspaper-style columns, sequential reading order, and RTL text support.
- **Encoding issue detection** — Automatically flags broken font encodings so callers 

... (truncated)