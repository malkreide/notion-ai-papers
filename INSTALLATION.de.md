# Installation und Einrichtung

🌐 [English](INSTALLATION.md) | [Deutsch](INSTALLATION.de.md)

## Übersicht

Der Notion AI Papers Skill kann auf verschiedene Arten in Claude integriert werden. Diese Anleitung deckt alle gängigen Szenarien ab.

---

## Option 1: Claude.ai Projekte (Empfohlen)

### Voraussetzungen
- Claude.ai Account (kostenlos, Pro oder Team)
- Zugriff auf die Custom Skills-Funktion

### Schritt-für-Schritt-Anleitung

1. **Skill-Dateien herunterladen**
   Lade folgende Dateien aus diesem Repository herunter:
   - `SKILL.md`
   - `references/user-context.md`
   - `references/notion-fields.md`

2. **In Claude.ai importieren**
   - Öffne [claude.ai](https://claude.ai)
   - Erstelle oder öffne ein Projekt
   - Navigiere zu **Projekteinstellungen** → **Custom Skills**
   - Klicke auf **«Benutzerdefinierten Skill hinzufügen»**
   - Lade die `SKILL.md` Datei hoch
   - Lade auch die Referenzdateien hoch

3. **Notion-Integration konfigurieren**
   - Stelle sicher, dass Claude Zugriff auf den Notion MCP-Connector hat
   - Der Skill referenziert eine spezifische Notion-Datenbank-ID — aktualisiere diese in `SKILL.md` (Zeile 129) entsprechend deiner eigenen Datenbank

4. **Verifizierung**
   Teste den Skill mit einem Paper-Link:
   ```
   Hier ist ein Paper zu AI in Education: [arXiv- oder Google-Drive-Link einfügen]
   ```
   Claude sollte das Paper analysieren und in deine Notion-Datenbank einfügen.

---

## Option 2: Claude API (Programmgesteuert)

### Voraussetzungen
- Anthropic API Key
- Python 3.8+ oder Node.js 16+

### Python-Beispiel

```python
import anthropic

# Skill-Inhalt laden
with open("SKILL.md", "r") as f:
    skill_content = f.read()

# Referenzdateien laden
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
            "content": "Analysiere dieses Paper: https://arxiv.org/abs/2403.12345"
        }
    ]
)

print(message.content)
```

### Node.js-Beispiel

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
      content: "Analysiere dieses Paper: https://arxiv.org/abs/2403.12345",
    },
  ],
});

console.log(message.content);
```

**Hinweis:** Der API-Ansatz beinhaltet keine native Notion-Integration. Du musst die Notion-API-Aufrufe separat handhaben oder MCP verwenden.

---

## Option 3: MCP Server (Model Context Protocol)

### Voraussetzungen
- MCP-Server-Setup (siehe [MCP Docs](https://modelcontextprotocol.io))
- Claude Desktop App oder kompatibles Tool
- Notion MCP-Connector konfiguriert

### Schritt 1: MCP-Resource erstellen

Erstelle eine `mcp_server.py`:

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
            description="Systematische AI-Paper-Analyse und Notion-Integration"
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

### Schritt 2: MCP-Server in Claude Desktop registrieren

Füge in `~/Library/Application Support/Claude/claude_desktop_config.json` hinzu:

```json
{
  "mcpServers": {
    "notion-ai-papers": {
      "command": "python",
      "args": ["/pfad/zu/mcp_server.py"]
    }
  }
}
```

### Schritt 3: Claude Desktop neu starten

Der Skill steht jetzt als Resource zur Verfügung.

---

## Option 4: Schnelltest (Nicht-persistent)

Für schnelles Testen ohne dauerhafte Installation:

1. Lade `SKILL.md`, `references/user-context.md` und `references/notion-fields.md` herunter
2. In Claude.ai: Lade alle Dateien in einen Chat hoch
3. Schreibe: «Verwende die Methodik aus diesen Dateien für die Analyse des folgenden Papers: [Paper-Link]»

**Einschränkung:** Funktioniert nur für den aktuellen Chat, nicht persistent.

---

## Notion-Datenbank einrichten

### Kompatible Datenbank erstellen

Wenn du eine neue Notion-Datenbank einrichtest, sollte sie folgende Properties enthalten:

| Property | Typ | Erforderlich |
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

Siehe `references/notion-fields.md` für detaillierte Felddefinitionen und erlaubte Werte.

---

## Troubleshooting

### «Skill nicht gefunden»
- Stelle sicher, dass die Datei korrekt hochgeladen wurde
- Prüfe, ob der Skill in den Projekteinstellungen aktiviert ist

### «Skill funktioniert nicht wie erwartet»
- Stelle sicher, dass du die aktuellste Version der `SKILL.md` verwendest
- Verifiziere, dass auch die Referenzdateien geladen sind

### «Notion-Integration fehlerhaft»
- Prüfe, ob der Notion MCP-Connector konfiguriert ist
- Verifiziere, dass die Datenbank-ID in `SKILL.md` mit deiner Datenbank übereinstimmt
- Stelle sicher, dass die Feldnamen exakt übereinstimmen (Gross-/Kleinschreibung beachten)

### API-Integration: «System Prompt zu lang»
- Der vollständige Skill mit Referenzen ist ca. 20 KB — verwende ein Modell mit grossem Context Window
- Alternativ: Verwende nur `SKILL.md` ohne Referenzdateien für ein leichteres Setup

---

## Best Practices

1. **Projekt-spezifische Aktivierung**: Aktiviere den Skill nur in Projekten, wo Paper-Analyse relevant ist
2. **Kombination mit anderen Skills**: Lässt sich gut kombinieren mit Dokumentenerstellungs- und Datenanalyse-Skills
3. **Regelmässige Updates**: Prüfe monatlich auf neue Versionen im GitHub-Repo
4. **Referenzen anpassen**: Passe `references/user-context.md` an deine Rolle und Fokusgebiete an

---

## Support

Bei Fragen oder Problemen:
- Öffne ein [GitHub Issue](https://github.com/malkreide/notion-ai-papers/issues)
- Prüfe den [Diskussionsbereich](https://github.com/malkreide/notion-ai-papers/discussions)
