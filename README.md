# Notion AI Papers Skill

Ein spezialisierter Claude Skill für die systematische Analyse von AI-Research-Papers und deren strukturierte Integration in Notion-Datenbanken.

## 🎯 Übersicht

Dieser Skill wurde entwickelt für die effiziente Verarbeitung wissenschaftlicher Publikationen im Kontext öffentlicher Verwaltung und Bildungswesen. Er automatisiert den Workflow von der Paper-Identifikation bis zur strukturierten Ablage in Notion.

**Entwickelt für:** Schulamt der Stadt Zürich  
**Anwendungskontext:** KI-Fachgruppe Stadtverwaltung, Geschäftsleitungs-Entscheidungen, Bildungsforschung

## ✨ Hauptfunktionen

- **Automatische Paper-Analyse**: Extrahiert Metadaten, Kernaussagen und Relevanzeinschätzungen
- **Multi-Source-Beschaffung**: Unterstützt arXiv, DOI, ScienceDirect, Google Drive
- **Notion-Integration**: Direktes Einfügen in strukturierte Datenbanken
- **Fokussierte Bewertung**: Spezialisiert auf Bildung, Verwaltungsdigitalisierung, KI-Governance
- **Reporting**: Automatische Übersichtstabellen mit Relevanzeinschätzung

## 🚀 Verwendung

### Voraussetzungen

- Zugang zu Claude (claude.ai oder API)
- Notion-Datenbank mit entsprechenden Feldern (siehe [Notion Field Definitions](references/notion-fields.md))
- Optional: Google Drive Integration

### Installation

1. Lade den Skill in dein Claude Skills-Verzeichnis:
   ```
   /mnt/skills/user/notion-ai-papers/
   ```

2. Stelle sicher, dass folgende Dateien vorhanden sind:
   - `SKILL.md` (Haupt-Skill-Definition)
   - `references/user-context.md`
   - `references/notion-fields.md`
   - `scripts/pdf_analyzer.py` (optional)

### Beispiel-Anwendung

```
User: "Hier ist ein Paper zu AI in Education: 
https://drive.google.com/open?id=1ABC..."

Claude: [Analysiert Paper, extrahiert Metadaten, 
fügt in Notion-Datenbank ein, erstellt Summary]
```

## 📋 Workflow

```
1. Paper-Identifikation
   ↓
2. Beschaffung (arXiv, DOI, Web)
   ↓
3. Vollständige Analyse
   - Metadaten
   - Klassifikation
   - Inhaltliche Analyse
   ↓
4. Notion-Integration
   ↓
5. Reporting & Übersichtstabelle
```

## 🎓 Fokusgebiete

Der Skill bewertet Papers besonders im Hinblick auf:

- **Bildungskontext**: Unterricht, Lernprozesse, Lehrerunterstützung
- **Sonderpädagogik**: Individualisierte Förderung, Inklusion, adaptive Systeme
- **Verwaltungseffizienz**: Prozessoptimierung, Automatisierung
- **Strategische Positionierung**: Thought Leadership, Policy-Entwicklung
- **Marktchancen**: Innovative Lösungen, neue Geschäftsmodelle

## 📁 Struktur

```
notion-ai-papers/
├── SKILL.md                      # Haupt-Skill-Definition
├── references/
│   ├── user-context.md          # Rollenprofil und Perspektiven
│   └── notion-fields.md         # Notion-Felddefinitionen
└── scripts/
    └── pdf_analyzer.py          # Hilfsskript (optional)
```

## 🔧 Konfiguration

### Notion-Datenbank

Erforderliche Felder (siehe `references/notion-fields.md` für Details):

- **Basis**: Title, Status, Typ
- **Klassifikation**: Topics, UseCase, Zielgruppe
- **Metadaten**: Authors, Publication, PDF_Link
- **Inhalt**: Summary, Notes
- **Links**: Google Drive File, NotebookLM
- **Bewertung**: Rating, LearningItems

### Anpassung an eigene Notion-Datenbank

1. Passe die Datenbank-ID in `SKILL.md` an (Zeile 129)
2. Stelle sicher, dass alle Feldnamen übereinstimmen
3. Passe `references/notion-fields.md` an deine Anforderungen an

## 📖 Dokumentation

- **[SKILL.md](SKILL.md)**: Vollständige Skill-Definition mit detailliertem Workflow
- **[User Context](references/user-context.md)**: Rollenprofil und Perspektiven
- **[Notion Fields](references/notion-fields.md)**: Detaillierte Felddefinitionen

## 🤝 Beitragen

Dieses Projekt ist als Beispiel für spezialisierte Claude Skills konzipiert. Feedback und Verbesserungsvorschläge sind willkommen:

- Issues für Bugs oder Feature-Requests
- Pull Requests für Verbesserungen
- Diskussionen für Anpassungen an andere Kontexte

## 📄 Lizenz

MIT License - siehe [LICENSE](LICENSE) für Details.

## 🙏 Danksagungen

Entwickelt für das Schulamt der Stadt Zürich im Rahmen der KI-Fachgruppe der Stadtverwaltung.

---

**Hinweis**: Dieser Skill ist speziell auf den Kontext öffentliche Verwaltung und Bildungswesen zugeschnitten. Für andere Anwendungsfälle sind Anpassungen in `references/user-context.md` und `SKILL.md` erforderlich.
