# Cloudflare Computer

Cloudflare Computer is a virtual filesystem that lives inside a
Durable Object. The Durable Object holds the authoritative state in
SQLite and exposes one pluggable execution surface through
`workspace.runtime`. Three backends ship today:

- **Container** projects the SQLite state into a sandbox container as
  a real FUSE mount. A sandbox-side daemon (`computerd`) mounts the state
  as a filesystem and syncs changes back over a capnweb RPC channel.
  Full Linux userland, real binaries, real network.
- **Isolate shell** runs [just-bash](https://github.com/vercel-labs/just-bash)
  in a Dynamic Worker. It reaches the authoritative Workspace over
  Workers RPC, so there is no second store or sync round trip.
- **Isolate JavaScript** runs an ECMAScript module in a fresh Dynamic
  Worker with structured input/results, durable relative imports,
  configured libraries, Workspace-backed `node:fs/promises`, and trusted `ws:git` and
  `ws:artifacts` modules.

A Workspace may register multiple backends under stable IDs.
`workspace.runtime.exec(source, { backend })` is the single execution
entry point; the selected backend defines whether `source` is a shell
command or an ECMAScript module. Backends connect lazily on first use.

Workspace can also be constructed without a backend at all, giving
callers the filesystem on its own.

> [!IMPORTANT]
> **PREVIEW ONLY** This package is provided as a preview for feedback only.
> APIs are unstable and the design is subject to change.
>
> Suitable for experiments, exploration and prototypes. It is NOT suitable
> for production use at this time.
>
> The specification under [`docs/`](docs/) is forward-looking — read it for
> intent, not as description of the code today.

## Using it

If you want to build on Cloudflare Computer, install
[`@cloudflare/computer`](packages/computer/README.md) and follow that
package's README — it has the installation steps, the entrypoint map,
and worked examples of the `fs` and `runtime`

... (truncated)