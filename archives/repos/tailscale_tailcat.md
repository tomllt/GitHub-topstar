<p align="center">
  <img src="tailcat.png" alt="Tailcat" width="149" height="176">
</p>

<p align="center"><em>"Tailscale without Tailscale, by Tailscale"</em></p>

<p align="center">
  <a href="https://pkg.go.dev/github.com/tailscale/tailcat"><img src="https://pkg.go.dev/badge/github.com/tailscale/tailcat.svg" alt="Go Reference"></a>
  <a href="https://bsky.app/profile/tailcat.dev"><img src="https://img.shields.io/badge/Bluesky-@tailcat.dev-0285FF?logo=bluesky&logoColor=white" alt="Follow @tailcat.dev on Bluesky"></a>
</p>

# Tailcat

Tailcat is a remix of Tailscale open source pieces to act like
[netcat](https://en.wikipedia.org/wiki/Netcat), but over Tailscale's data plane,
without Tailscale's control plane. Tailscale's data plane (`magicsock`,
internally) gives you point-to-point WireGuard®-encrypted tunnels between two
machines with DERP as the NAT-hole-punching communication side channel and the
ultimate relay-of-last-resort if NAT traversal fails. Instead of using the
Tailscale control plane, all `tailcat` connection metadata is exchanged out of
band, however you want.

The `tailcat` CLI (in `cmd/tailcat`) is built on the `tailcat` Go library
(importable as [`github.com/tailscale/tailcat`](https://pkg.go.dev/github.com/tailscale/tailcat)).

Whether you use `tailcat` as a CLI tool or library, one side runs a `tailcat`
server (listener) and gets back a short tailcat address. The other side passes
that tailcat address to `tailcat`'s client side to connect. All traffic between
the two is
encrypted end-to-end with WireGuard. The initial connection bootstraps through
a DERP server ([see below](#bring-your-own-derp-relay)), and then magicsock performs NAT traversal to
upgrade to a direct peer-to-peer UDP connection when possible (usually!).

You don't need a Tailscale account, root/admin access on the machine
(it doesn't alter your machine's routing tables, DNS, etc.). It's just
a userspace library and CLI tool.

And it's all open source.

You can use our free rate

... (truncated)