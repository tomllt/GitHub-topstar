# Agent Substrate

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

NOTE: This is not an officially supported Google product. This project is not
eligible for the [Google Open Source Software Vulnerability Rewards Program](https://bughunters.google.com/open-source-security).

## What is Agent Substrate?

Agent Substrate is a secure-by-default agent execution runtime engineered to run millions of sandboxes with 10x higher density than standard container runtimes. Purpose-built for the era of autonomous agents, Substrate delivers sub-500ms resume operations at over 500 suspend/resume activations per second with native zero-trust kernel and network isolation. It supports multiple sandbox technologies including microVMs and gVisor, enabling consistent lifecycle operations for all sandbox types.

At its core, Agent Substrate maps a larger set of “actors” (applications such as agents) onto a smaller set of ready “workers”, relying on the fact that agent-like applications tend to be idle most of the time to achieve heavy multiplexing.  It provides functionality to manage an actor’s lifecycle (e.g. create/destroy, suspend/resume), to assign actors to workers in real time, and to route incoming traffic to them.

Agent Substrate is intended to be a low-opinion system.  The workloads it manages don't have to be literal AI agents, but those are the best example of the kind of applications it is designed for.  It is not an SDK for building agents, but rather a system for running them at scale.

Agent Substrate leverages Kubernetes for the infrastructure provisioning and worker lifecycle management (Kubernetes Pods). It builds on top of Kubernetes features like Pods and Pod autoscaling, while Agent Substrate provides agent-specific scheduling and control to achieve lower latency. Using Kubernetes as the underlying system enables consistent infrastructure management across all workloads types that are required for 

... (truncated)