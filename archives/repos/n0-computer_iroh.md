<h1 align="center"><a href="https://iroh.computer"><img alt="iroh" src="./.img/iroh_wordmark.svg" width="100" /></a></h1>

<h3 align="center">
less net work for networks
</h3>

[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg?style=flat-square)](https://docs.rs/iroh/)
[![Crates.io](https://img.shields.io/crates/v/iroh.svg?style=flat-square)](https://crates.io/crates/iroh)
[![downloads](https://img.shields.io/crates/d/iroh.svg?style=flat-square)](https://crates.io/crates/iroh)
[![Chat](https://img.shields.io/discord/1161119546170687619?logo=discord&style=flat-square)](https://discord.com/invite/DpmJgtU7cW)
[![Youtube](https://img.shields.io/badge/YouTube-red?logo=youtube&logoColor=white&style=flat-square)](https://www.youtube.com/@n0computer)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE-MIT)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=flat-square)](LICENSE-APACHE)
[![CI](https://img.shields.io/github/actions/workflow/status/n0-computer/iroh/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/n0-computer/iroh/actions/workflows/ci.yml)

<div align="center">
  <h3>
    <a href="https://iroh.computer/docs">
      Docs Site
    </a>
    <span> | </span>
    <a href="https://docs.rs/iroh">
      Rust Docs
    </a>
  </h3>
</div>
<br/>

## What is iroh?

Iroh gives you an API for dialing by public key.
You say “connect to that phone”, iroh will find & maintain the fastest connection for you, regardless of where it is.

### Hole-punching

The fastest route is a direct connection, so if necessary, iroh tries to hole-punch.
Should this fail, it can fall back to an open ecosystem of public relay servers.
To ensure these connections are as fast as possible, we [continuously measure iroh][iroh-perf].

### Built on [QUIC]

Iroh uses [noq] to establish [QUIC] connections between endpoints.
This way you get authenticated encryption, concurrent streams with

... (truncated)