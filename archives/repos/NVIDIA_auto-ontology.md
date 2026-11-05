<!--
SPDX-FileCopyrightText: Copyright (c) 2026, NVIDIA CORPORATION & AFFILIATES.
All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Auto Ontology

Agents can retrieve documents and query databases, but reliability gates agentic analytics: a revenue metric answered faster is worth nothing if the number is wrong. Agents need a context layer that tells them where data lives, what it means, whether to use it, how to use it, where it came from, and what is similar. NVIDIA Auto Ontology is an open library that builds that layer from enterprise metadata, reconciles definitions across systems, and exposes it to any agent harness through MCP, CLI, and API. It complements the semantic models customers already own.

It enables developers to:

- Discover: generate enterprise ontologies from metadata; connect existing ontologies and semantic models; build AI-ready knowledge graphs.
- Ground: give agents trusted business meaning for metrics, entities, and relationships; reconcile inconsistent definitions across systems.
- Validate: check generated queries against certified definitions and lineage; return provenance with every answer.
- Expose: serve context to any agent harness through MCP, CLI, and API.
Learn: fold certified corrections and usage back into the ontology, so shared context improves with every question.

## Benchmarks

To run a text-to-SQL benchmark such as BIRD, refer to the
[ontology SQL evaluation repository](https://github.com/NVIDIA/ontology-sql-eval/).

> **Licensing & contributions.** Auto Ontology is distributed under the
> [Apache License 2.0](./LICENSE). Third-party open-source components
> bundled, linked, or otherwise used by this project are listed in
> [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md). **This project
> is currently not accepting external contributions.**

<p>
<img src="./docs/assets/arch.png" alt="Auto Ontology Architecture" width="800">
</p>

## Key Features

- **Natural-language querying** of structured data — quest

... (truncated)