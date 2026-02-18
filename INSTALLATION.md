# Installation and Setup

🌐 [English](INSTALLATION.md) | [Deutsch](INSTALLATION.de.md)

## Overview

The Notion AI Papers Skill can be integrated into Claude in various ways. This guide covers all common scenarios.

---

## Option 1: Claude.ai Projects (Recommended)

### Prerequisites
- Claude.ai account (Free, Pro, or Team)
- Access to the Custom Skills feature

### Step-by-Step Guide

1. **Download skill files**
   Download the following files from this repository:
   - `SKILL.md`
   - `references/user-context.md`
   - `references/notion-fields.md`

2. **Import into Claude.ai**
   - Open [claude.ai](https://claude.ai)
   - Create or open a Project
   - Navigate to **Project Settings** → **Custom Skills**
   - Click **"Add Custom Skill"**
   - Upload the `SKILL.md` file
   - Also upload the reference files

3. **Configure Notion Integration**
   - Ensure Claude has access to the Notion MCP connector
   - The skill references a specific Notion database ID — update this in `SKILL.md` (line 129) to match your own database

4. **Verify**
   Test the skill by sharing a paper link:
   ```
   Here's a paper on AI in Education: [paste arXiv or Google Drive link]
   ```
   Claude should analyze the paper and insert it into your Notion database.

---

## Option 2: Claude API (Programmatic)

### Prerequisites
- Anthropic API Key
- Python 3.8+ or Node.js 16+

### Python Example

```python
import anthropic

# Load skill content
with open("SKILL.md", "r") as f:
    skill_content = f.read()

# Load reference files
with open("references/user-context.md", "r") as f:
    user_context = f.read()
with open("references/notion-fields.md", "r") as f:
    notion_fields = f.read()

system_prompt = f"{skill_content}\n\n{user_context}\n\n{notion_fields}"

client = anthropic.Anthropic(api_key="your-api-key")

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": "Analyze this paper: https://arxiv.org/abs/2403.12345"
        }
    ]
)

print(message.content)
```

### Node.js Example

```javascript
import Anthropic from "@anthropic-ai/sdk";
import fs from "fs";

const skillContent = fs.readFileSync("SKILL.md", "utf8");
const userContext = fs.readFileSync("references/user-context.md", "utf8");
const notionFields = fs.readFileSync("references/notion-fields.md", "utf8");

const systemPrompt = `${skillContent}\n\n${userContext}\n\n${notionFields}`;

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

const message = await client.messages.create({
  model: "claude-sonnet-4-20250514",
  max_tokens: 4096,
  system: systemPrompt,
  messages: [
    {
      role: "user",
      content: "Analyze this paper: https://arxiv.org/abs/2403.12345",
    },
  ],
});

console.log(message.content);
```

**Note:** The API approach does not include native Notion integration. You'll need to handle the Notion API calls separately or use MCP.

---

## Option 3: MCP Server (Model Context Protocol)

### Prerequisites
- MCP server setup (see [MCP Docs](https://modelcontextprotocol.io))
- Claude Desktop App or compatible tool
- Notion MCP connector configured

### Step 1: Create MCP Resource

Create a `mcp_server.py`:

```python
from mcp.server import Server
from mcp.types import Resource
import asyncio

server = Server("notion-ai-papers")

@server.list_resources()
async def list_resources() -> list[Resource]:
    return [
        Resource(
            uri="skill://notion-ai-papers",
            name="Notion AI Papers",
            mimeType="text/markdown",
            description="Systematic AI paper analysis and Notion integration"
        )
    ]

@server.read_resource()
async def read_resource(uri: str) -> str:
    if uri == "skill://notion-ai-papers":
        with open("SKILL.md", "r") as f:
            return f.read()
    raise ValueError(f"Unknown resource: {uri}")

async def main():
    async with server.start():
        await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
```

### Step 2: Register MCP Server in Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "notion-ai-papers": {
      "command": "python",
      "args": ["/path/to/mcp_server.py"]
    }
  }
}
```

### Step 3: Restart Claude Desktop

The skill is now available as a resource.

---

## Option 4: Quick Test (Non-Persistent)

For quick testing without permanent installation:

1. Download `SKILL.md`, `references/user-context.md`, and `references/notion-fields.md`
2. In Claude.ai: Upload all files into a chat
3. Write: "Use the methodology from these files to analyze the following paper: [your paper link]"

**Limitation:** Works only for the current chat session, not persistent.

---

## Notion Database Setup

### Creating a Compatible Database

If you're setting up a new Notion database, it should include these properties:

| Property | Type | Required |
|---|---|---|
| Title | Title | ✅ |
| Status | Select | ✅ |
| Typ | Select | ✅ |
| Topics | Multi-Select | ✅ |
| UseCase | Multi-Select | ✅ |
| Zielgruppe | Multi-Select | ✅ |
| Summary | Rich Text | ✅ |
| Authors | Rich Text | ✅ |
| Publication | Date | ✅ |
| PDF_Link | URL | ✅ |
| Google Drive File | URL | Optional |
| NotebookLM | URL | Optional |
| Notes | Rich Text | Optional |
| Rating | Select | Optional |
| LearningItems | Rich Text | Optional |

See `references/notion-fields.md` for detailed field definitions and allowed values.

---

## Troubleshooting

### "Skill not found"
- Ensure the file was uploaded correctly
- Check that the skill is activated in project settings

### "Skill doesn't work as expected"
- Ensure you're using the latest version of `SKILL.md`
- Verify that reference files are also loaded

### "Notion integration fails"
- Check that the Notion MCP connector is configured
- Verify the database ID in `SKILL.md` matches your database
- Ensure field names match exactly (case-sensitive)

### API Integration: "System prompt too long"
- The full skill with references is ~20 KB — use a model with a large context window
- Alternatively: Use only `SKILL.md` without reference files for a lighter setup

---

## Best Practices

1. **Project-specific activation**: Activate the skill only in projects where paper analysis is relevant
2. **Combine with other skills**: Works well with document creation and data analysis skills
3. **Regular updates**: Check monthly for new versions in the GitHub repo
4. **Customize references**: Adapt `references/user-context.md` to your role and focus areas

---

## Support

For questions or issues:
- Open a [GitHub Issue](https://github.com/malkreide/notion-ai-papers/issues)
- Check the [Discussions](https://github.com/malkreide/notion-ai-papers/discussions) section
