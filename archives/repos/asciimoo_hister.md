# Hister

**Your own search engine**

Hister is a private search engine for the pages you visit and the files you keep. It indexes their full contents so you can find information again from the web interface, terminal, or an AI assistant connected through MCP.

[Try the demo](https://demo.hister.org/) · [Download Hister](https://github.com/asciimoo/hister/releases/latest) · [Read the quickstart](https://hister.org/docs/quickstart) · [Documentation](https://hister.org/docs)

![Hister web interface](webui/website/src/lib/assets/screenshot.png)

## Quickstart

1. Download the binary for your platform from the [latest release](https://github.com/asciimoo/hister/releases/latest), then rename it to `hister` (`hister.exe` on Windows).

2. On Linux or macOS, make it executable:

   ```bash
   chmod +x hister
   ```

3. Start Hister on Linux or macOS:

   ```bash
   ./hister listen
   ```

   On Windows, run `.\hister.exe listen` in PowerShell.

   Keep this terminal open while using Hister. The server must be running to index pages and search them.

4. Open <http://127.0.0.1:4433> and install the browser extension for [Firefox](https://addons.mozilla.org/en-US/firefox/addon/hister/) or [Chrome](https://chromewebstore.google.com/detail/hister/cciilamhchpmbdnniabclekddabkifhb).

5. Visit a web page with the extension enabled, then return to Hister and search for a phrase from that page to find your first indexed result.

No configuration is required for a local personal setup. See the [complete quickstart](https://hister.org/docs/quickstart) to choose what Hister indexes.

To search existing content, [import browser history](https://hister.org/docs/import#importing-browser-history), [index local directories](https://hister.org/docs/configuration#local-directory-indexing), or [import files](https://hister.org/docs/import#importing-files).

Alternative installation methods include Homebrew (`brew install hister`), Docker, and Nix. See the [installation guide](https://hister.org

... (truncated)