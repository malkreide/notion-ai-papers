# Installation & Setup

Diese Anleitung hilft dir, den Notion AI Papers Skill in deiner Claude-Umgebung einzurichten.

## Voraussetzungen

1. **Claude-Zugang**
   - claude.ai Account ODER
   - Claude API Zugang

2. **Notion-Datenbank**
   - Workspace mit Notion-Datenbank
   - Notion Integration mit entsprechenden Berechtigungen
   - Datenbank-ID (siehe Abschnitt "Notion Setup")

3. **Optional: Google Drive**
   - Für die Verarbeitung von Papers aus Google Drive
   - Google Drive Integration in Claude aktiviert

## Schritt 1: Skill-Installation

### Option A: In claude.ai (empfohlen)

1. Navigiere zu den Skills-Einstellungen in claude.ai
2. Lade die Skill-Dateien hoch:
   ```
   SKILL.md
   references/user-context.md
   references/notion-fields.md
   scripts/pdf_analyzer.py (optional)
   ```
3. Stelle sicher, dass die Verzeichnisstruktur erhalten bleibt

### Option B: Über API/lokale Installation

1. Clone das Repository:
   ```bash
   git clone https://github.com/malkreide/notion-ai-papers.git
   ```

2. Kopiere die Dateien in dein Skills-Verzeichnis:
   ```bash
   cp -r notion-ai-papers /mnt/skills/user/
   ```

## Schritt 2: Notion Setup

### 2.1 Datenbank-ID ermitteln

1. Öffne deine Notion-Datenbank im Browser
2. Die URL hat folgendes Format:
   ```
   https://www.notion.so/workspace/DATABASE_ID?v=VIEW_ID
   ```
3. Kopiere die `DATABASE_ID` (32 Zeichen, ohne Bindestriche)

### 2.2 Notion Integration erstellen

1. Gehe zu https://www.notion.so/my-integrations
2. Klicke auf "New integration"
3. Gib einen Namen ein (z.B. "AI Papers Skill")
4. Wähle den Workspace aus
5. Kopiere den "Internal Integration Token"

### 2.3 Integration mit Datenbank verbinden

1. Öffne die Notion-Datenbank
2. Klicke auf "..." (oben rechts) → "Connections"
3. Wähle deine Integration aus

### 2.4 Datenbank-Felder einrichten

Erstelle folgende Felder in deiner Notion-Datenbank (siehe `references/notion-fields.md` für Details):

**Pflichtfelder:**
- Title (Title)
- Status (Select)
- Typ (Select)
- Topics (Multi-Select)
- UseCase (Multi-Select)
- Zielgruppe (Multi-Select)
- Summary (Rich Text)
- Authors (Rich Text)
- Publication (Date)
- PDF_Link (URL)

**Optionale Felder:**
- Google Drive File (URL)
- NotebookLM (URL)
- Rating (Number oder Select)
- LearningItems (Rich Text)
- Notes (Rich Text)

## Schritt 3: Skill-Konfiguration

### 3.1 Datenbank-ID aktualisieren

Öffne `SKILL.md` und aktualisiere Zeile 129-130:

```markdown
**Datenbank:**
- ID: `DEINE_DATABASE_ID_HIER`
- URL: https://www.notion.so/WORKSPACE/DEINE_DATABASE_ID_HIER
```

### 3.2 User Context anpassen (optional)

Falls du den Skill für einen anderen Kontext verwendest:

1. Öffne `references/user-context.md`
2. Passe Rolle, Organisation und Fokusgebiete an
3. Aktualisiere die Perspektiven nach deinen Bedürfnissen

### 3.3 Feld-Definitionen überprüfen

Öffne `references/notion-fields.md` und stelle sicher, dass:
- Alle Feldnamen mit deiner Notion-Datenbank übereinstimmen
- Die Select/Multi-Select Optionen korrekt sind
- Die Qualitätskriterien deinen Anforderungen entsprechen

## Schritt 4: Testen

### 4.1 Einfacher Test

Starte eine Konversation mit Claude:

```
Ich möchte einen Test machen. Analysiere dieses Paper: 
https://arxiv.org/abs/2303.08774
```

Claude sollte:
1. Das Paper von arXiv abrufen
2. Metadaten extrahieren
3. Eine strukturierte Analyse erstellen
4. Das Paper in Notion einfügen (wenn konfiguriert)

### 4.2 Google Drive Test (optional)

Falls Google Drive Integration aktiv ist:

```
Hier ist ein Paper aus Google Drive:
https://drive.google.com/open?id=DEINE_FILE_ID
```

## Fehlerbehebung

### Problem: "Notion-Datenbank nicht gefunden"

**Lösung:**
1. Überprüfe die Datenbank-ID in `SKILL.md`
2. Stelle sicher, dass die Integration verbunden ist
3. Prüfe die Berechtigungen der Integration

### Problem: "Felder nicht gefunden"

**Lösung:**
1. Überprüfe, dass alle Feldnamen exakt übereinstimmen (case-sensitive!)
2. Stelle sicher, dass die Feldtypen korrekt sind (Select, Multi-Select, etc.)
3. Siehe `references/notion-fields.md` für die exakte Konfiguration

### Problem: "Paper nicht zugänglich"

**Lösung:**
1. Überprüfe, ob das Paper öffentlich verfügbar ist
2. Bei ScienceDirect: Suche nach alternativen Quellen (arXiv Preprint)
3. Lade das PDF direkt hoch, falls verfügbar

### Problem: "Summary nicht hochwertig"

**Lösung:**
1. Überprüfe `references/user-context.md` - ist dein Kontext klar?
2. Stelle sicher, dass die Qualitätskriterien in `references/notion-fields.md` definiert sind
3. Gib spezifisches Feedback für bessere Anpassung

## Support

Bei Problemen:

1. Prüfe die [häufigsten Fehler](#fehlerbehebung)
2. Suche in den [GitHub Issues](https://github.com/malkreide/notion-ai-papers/issues)
3. Erstelle ein neues Issue mit detaillierter Beschreibung

## Nächste Schritte

- Lies die [vollständige Dokumentation](SKILL.md)
- Passe den Skill an deine Bedürfnisse an
- Teile dein Feedback und Verbesserungen!
