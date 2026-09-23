<h1>
  <img src="assets/axolotl.svg" width="70" align="absmiddle" alt="AX axolotl">
  AX
</h1>

> [!WARNING]
> We are still actively refining our core concepts, protocols,
> and specifications. We will likely to introduce major breaking
> changes prior to a stable release.

**Declare an agentic task with workspaces and gateway specifications. AX sandboxes it, wires up its workspace, fences its network, and helps running it at scale.**

AX is a high-throughput, declarative orchestrator to run billions of autonomous agent workloads in a cluster. It runs on top of [Agent Substrate](https://github.com/agent-substrate/substrate) for sandboxed execution and is built to run billions of tasks per cluster. If you have used Kubernetes, `ax` will feel similar.

```yaml
# task.yaml
apiVersion: ax.io/v1alpha1
kind: Workspace
metadata:
  name: golang
spec:
  git:
    - repo: https://github.com/golang/go.git
      branch: "my-fix"
---
apiVersion: ax.io/v1alpha1
kind: Task
metadata:
  name: test
spec:
  workspaces:
    - name: golang
      goal: "Ensure that Go tool chain is available and is built from source"
  debug: true   # lets you `ax ssh` into the sandbox
```

Then apply it, watch it come up, and look over the agent's shoulder:

```bash
ax apply -f task.yaml
ax watch task test
ax ssh test -- ls -al /workspace
```

## Why?

Agents are a new kind of workload. They are neither stateless microservices nor run-to-completion batch jobs. They accumulate state, need strict isolation, call out to model APIs and tool servers, and can burn money in a loop if nobody is watching. AX gives you four small primitives that handle all of that declaratively:

| You want to... | AX gives you |
|---|---|
| Run untrusted agent code in an isolated sandbox with CPU/memory limits | **`Task`** |
| Pre-wire Git repos, MCP servers, and skill packages so every agent starts warm | **`Workspace`** |
| Lock outbound traffic down to an explicit host allowlist | **`Gateway`** |
| Configure which LLM the plat

... (truncated)