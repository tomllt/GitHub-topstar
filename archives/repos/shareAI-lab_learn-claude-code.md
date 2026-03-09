[English](./README.md) | [中文](./README-zh.md) | [日本語](./README-ja.md)  
# Learn Claude Code -- A nano Claude Code-like agent, built from 0 to 1
<img width="260" src="https://github.com/user-attachments/assets/fe8b852b-97da-4061-a467-9694906b5edf" /><br>

Scan with Wechat to fellow us,  
or fellow on X: [shareAI-Lab](https://x.com/baicai003)  


```
                    THE AGENT PATTERN
                    =================

    User --> messages[] --> LLM --> response
                                      |
                            stop_reason == "tool_use"?
                           /                          \
                         yes                           no
                          |                             |
                    execute tools                    return text
                    append results
                    loop back -----------------> messages[]


    That's the minimal loop. Every AI coding agent needs this loop.
    Production agents add policy, permissions, and lifecycle layers.
```

**12 progressive sessions, from a simple loop to isolated autonomous execution.**
**Each session adds one mechanism. Each mechanism has one motto.**

> **s01** &nbsp; *"One loop & Bash is all you need"* &mdash; one tool + one loop = an agent
>
> **s02** &nbsp; *"Adding a tool means adding one handler"* &mdash; the loop stays the same; new tools register into the dispatch map
>
> **s03** &nbsp; *"An agent without a plan drifts"* &mdash; list the steps first, then execute; completion doubles
>
> **s04** &nbsp; *"Break big tasks down; each subtask gets a clean context"* &mdash; subagents use independent messages[], keeping the main conversation clean
>
> **s05** &nbsp; *"Load knowledge when you need it, not upfront"* &mdash; inject via tool_result, not the system prompt
>
> **s06** &nbsp; *"Context will fill up; you need a way to make room"* &mdash; three-layer compression strategy for infinite sessions
>
> **s07** &nbsp; *"Break big goals into 

... (truncated)