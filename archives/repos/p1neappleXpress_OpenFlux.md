# OpenFlux

**English** | [Русский](README.ru.md)

Network stack research tool. TCP tunnel with pluggable transports.


# Disclaimer

The author of OpenFlux **does not encourage** the use of this project to bypass restrictions or violate the rules of any platform, and **is not responsible** for the final scenarios of how users apply this tool in real life or on the Internet. Any specific technical features of the application are nothing more than an **architectural coincidence**, created **without any intent**.

The project is **entirely non-commercial**, contains **no paid features, hidden subscriptions, or commercial benefit**.

The author **is not responsible** for forks, modifications, or derivative versions of OpenFlux created by third parties. Any changes added to a fork are the responsibility of its author.

The author **is not responsible** for:

- Any use of OpenFlux by third parties
- Consequences caused by the use of forks and modifications
- Damage resulting from derivative versions
- Violations committed using forks

The original code is provided **as is**, **without any warranties**.

## Clients

| Platform | Download | Notes |
|----------|----------|-------|
| **Android** | [OpenFluxAndroid releases](https://github.com/p1neappleXpress/OpenFluxAndroid) | Standalone APK |
| **iOS** | [TestFlight beta](https://testflight.apple.com/join/BwnAcdus) | System-wide VPN via Network Extension |

> **iOS app** built by [@saharev1](https://github.com/saharev1) — full iOS client, TestFlight pipeline, system VPN support, DNS-over-TLS, and many stability fixes. HUGE thanks! 🙏
>
> **Android app** — [p1neappleXpress/OpenFluxAndroid](https://github.com/p1neappleXpress/OpenFluxAndroid).

## Overview
```
Client (SOCKS5) --> Transport --> Exit Node --> Internet
```

## Requirements
1. Golang v. 1.26.3+ - is required for building desktop client / exit node binary (universal-bypass-tool);
2. Android Native Development Kit (NDK) v.27.0.12077973+ - is required for building And

... (truncated)