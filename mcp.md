# MCP servers

No keys, tokens or headers from the real setup are in this file. Replace every `<...>` placeholder with your own value. Never paste a placeholder literally: the config stores it as-is and the server fails silently.

## User-scope servers added with the CLI

### Context7 (current library docs)
macOS or Linux:
```sh
claude mcp add --scope user context7 -- npx -y @upstash/context7-mcp@latest
```
Windows (Git Bash; the prefix stops path rewriting, see `skills/claude-mcp-add-windows`):
```sh
MSYS_NO_PATHCONV=1 claude mcp add --scope user context7 -- cmd.exe /d /c npx -y @upstash/context7-mcp@latest
```

### REA (reverse engineering, dual-use: only on targets you own or may test)
```sh
claude mcp add --scope user rea -- npx -y rea-agents@6.5.0 mcp
# Windows:
MSYS_NO_PATHCONV=1 claude mcp add --scope user rea -- cmd.exe /d /c npx -y rea-agents@6.5.0 mcp
```

### 21st.dev Magic (UI components; needs your own API key)
```sh
claude mcp add --scope user --transport http 21st https://21st.dev/api/mcp --header "x-api-key: <YOUR_21ST_API_KEY>"
```
To avoid the key landing in shell history, read it into a variable first and `unset` it after (see `skills/install-agent-tools-safely`).

## Servers that come with plugins (no command needed)

| Server | From plugin | Notes |
|---|---|---|
| vercel (`https://mcp.vercel.com`) | vercel | Log in when first used. |
| chrome-devtools (`npx -y chrome-devtools-mcp@1.10.1`) | ecc | Drives a local Chrome for screenshots and scripted checks. |
| miro (`https://mcp.miro.com/`) | miro | Needs Miro authentication. |

## claude.ai connectors

These are connected in claude.ai settings (Connectors), not with the CLI, and appear in Claude Code when you are logged in with the same account: Claude Docs, Figma, Notion, Google Drive, Gmail, Google Calendar, Higgsfield, Canva (installed but disabled). Each asks for its own OAuth login.

## Check

```sh
claude mcp list
```

`claude mcp list` and `claude mcp get` can print headers. Do not paste their raw output into notes, issues or chats.
