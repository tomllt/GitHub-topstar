<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="https://cdn.builder.io/api/v1/image/assets%2FYJIGb4i01jvw0SRdL5Bt%2F5476444e54ee4a958966c90caca468e3"
  />
  <source
    media="(prefers-color-scheme: light)"
    srcset="https://cdn.builder.io/api/v1/image/assets%2FYJIGb4i01jvw0SRdL5Bt%2F7628600bc10a4940b78f42c5df7628b0"
  />
  <img
    alt="Agent-Native: The agentic application framework"
    src="https://cdn.builder.io/api/v1/image/assets%2FYJIGb4i01jvw0SRdL5Bt%2F7628600bc10a4940b78f42c5df7628b0"
  />
</picture>

# Agent-Native

Agent-Native is an open-source TypeScript framework for building agents that pair autonomous work with a purpose-built UI. Define each capability once as an [action](https://agent-native.com/docs/actions-overview): the agent uses it as a tool, and the UI calls it from code.

## Quick start

```bash
npx --yes @agent-native/core@latest create my-agent --standalone --template chat
```

Follow the [getting started guide](https://agent-native.com/docs/getting-started) for a full intro to the framework.

## Why build agents with UIs?

Coding agents work with more than a text box. Their environment provides context, tools, files, tests, and previews that make their capabilities and results visible.

Knowledge work needs that same kind of environment. A UI shows what an agent can do and gives people familiar ways to inspect, edit, approve, and share its work.

## How Agent-Native works

- **[Shared actions](https://agent-native.com/docs/actions-overview).** The agent calls each capability as a tool, and the UI calls it from code. Both paths use the same validation, permissions, and implementation.
- **[Shared data](https://agent-native.com/docs/server-database).** Work done by the agent appears in the UI, and work done in the UI is available to the agent.
- **[Shared application state](https://agent-native.com/docs/context-awareness).** The agent receives relevant UI state, such as the current page, selected record, or activ

... (truncated)