<h1 align="center">pgrust</h1>

<p align="center">
  <strong>A Postgres rewrite in Rust.</strong>
</p>

<p align="center">
  <img alt="Postgres 18.3" src="https://img.shields.io/badge/Postgres-18.3-336791">
  <img alt="Regression queries: 46k+" src="https://img.shields.io/badge/regression_queries-46k%2B-brightgreen">
  <a href="https://github.com/malisper/pgrust/blob/main/LICENSE">
    <img alt="License: AGPL-3.0" src="https://img.shields.io/badge/license-AGPL--3.0-blue">
  </a>
</p>

<div align="center">
  <a href="https://pgrust.com">Browser demo</a>
  <span>&nbsp;&nbsp;|&nbsp;&nbsp;</span>
  <a href="https://discord.gg/FZZ4dbdvwU">Discord</a>
  <span>&nbsp;&nbsp;|&nbsp;&nbsp;</span>
  <a href="https://pgrust.com/#updates">Get pgrust updates</a>
  <span>&nbsp;&nbsp;|&nbsp;&nbsp;</span>
  <a href="https://github.com/malisper/pgrust/issues">Issues</a>
</div>

<br />

pgrust targets compatibility with Postgres 18.3 and matches Postgres's
expected output across more than 46,000 regression queries.

pgrust is disk compatible with Postgres and can boot from an existing Postgres
18.3 data directory.

The goal is to make Postgres easier to change from the inside: keep the behavior
Postgres-shaped, keep the real Postgres tests as the oracle, and use Rust plus
AI-assisted programming to explore deeper server changes.

Update: We're working on a new not yet published version of pgrust that currently passes 100% of Postgres regression suite, has a thread per connection model instead of process per connection, is 50% faster than Postgres on transaction workloads, and is ~300x faster than Postgres on analytical workloads (2x slower than Clickhouse on clickbench and we think it can get faster than Clickhouse). Follow pgrust or join our Discord for updates!

## Follow pgrust

[Get project updates by email](https://pgrust.com/#updates), including new
releases, compatibility milestones, and architecture experiments.

## Status

pgrust is not production-ready yet. It is not performa

... (truncated)