# Humanizer

[![skills.sh installs](https://skills.sh/b/blader/humanizer)](https://skills.sh/blader/humanizer)

Humanizer rewrites AI-sounding text so it reads like a person wrote it, without changing what it says. Because it is just Markdown, it works with any agent that supports skills.

## How it works

Humanizer uses 35 patterns from Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. It makes a first pass without treating the original structure as fixed. Then it checks the draft against those patterns and the original claims before rewriting whatever still needs work.

> "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

It does not make things up. A name, number, date, quote, citation, or other factual detail must come from the source or the writer. For personal writing, Humanizer keeps the writer's style. Technical and reference prose stays neutral and plain. If you provide a writing sample, Humanizer follows that sample instead of its default style rules.

When you paste text, Humanizer shows its work before giving you the final version. You see the first rewrite and a short critique of anything that still sounds artificial. Point it at a file and it changes only the prose, leaving code, data, frontmatter, and link targets alone.

## Usage

Call the skill directly:

```
/humanizer

[paste your text here]
```

Or ask in plain language:

```
Please humanize this text: [your text]
```

To rewrite a file, give Humanizer its path:

```
Humanize the prose in docs/launch-post.md
```

### Match your voice

If you want the rewrite to sound more like you, include a sample:

```
/humanizer

Here's a sample of my writing for voice matching:
[paste 2-3 paragraphs of your own writing]

Now humanize this text:
[paste AI text to humanize]
```

Humanizer follows the sample

... (truncated)