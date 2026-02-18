---
name: notion-ai-papers
description: Systematische Analyse und Integration von AI-Research-Papers in eine Notion-Datenbank. Nutze diesen Skill wenn der User (1) Links zu AI-Papers teilt – arxiv, DOI, ScienceDirect, Nature, IEEE oder andere Quellen – und diese in die Notion-Datenbank "AI Papers & Resources" einfügen möchte, (2) Paper-Titel oder Referenzen nennt und eine Aufnahme in die Datenbank wünscht, (3) Papers mit Fokus auf Bildung, öffentliche Verwaltung, KI-Governance oder Verwaltungsdigitalisierung analysieren lässt, (4) systematische Paper-Reviews für strategische GL-Entscheidungen benötigt, (5) eine Übersichtstabelle zu eingefügten Papers anfordert. Typische Trigger: "Füge ein:", "Paper hinzufügen", ein arxiv/DOI-Link ohne weiteren Kontext, oder mehrere Links nacheinander.
---

# Notion AI Papers Integration

Dieser Skill ermöglicht die systematische Analyse von AI-Research-Papers und deren strukturierte Integration in die Notion-Datenbank "AI Papers & Resources".

## Workflow-Übersicht

1. **Identifikation**: Analysiere Links oder Paper-Referenzen
2. **Beschaffung**: Lade Papers von öffentlichen Quellen (arXiv, DOI, etc.)
3. **Analyse**: Extrahiere alle erforderlichen Informationen
4. **Integration**: Füge strukturierte Daten in Notion-Datenbank ein
5. **Reporting**: Erstelle Übersichtstabelle mit Relevanzeinschätzung

## Kontext laden

**Vor Beginn der Arbeit immer lesen:**
- `references/user-context.md` - Rolle, Perspektiven und Fokusgebiete des Users
- `references/notion-fields.md` - Vollständige Felddefinitionen und Qualitätskriterien

## Schritt 1: Paper-Identifikation

**Input-Formate:**
- arxiv-Links: `https://arxiv.org/abs/2403.12345` oder `https://arxiv.org/pdf/2403.12345`
- DOI-Links: `https://doi.org/10.xxxx/...`
- Publisher-Links: ScienceDirect, Nature, IEEE, ACM, Springer, PNAS etc.
- Paper-Titel als Freitext: z.B. "Constitutional AI: Harmlessness from AI Feedback"
- Dateinamen: z.B. `1-s2.0-S2666920X25000736-main.pdf`
- Bare Links ohne Kontext: User schickt nur einen Link – behandle als Paper-Einfüge-Auftrag

**Vorgehen:**
1. **Link-Typ erkennen**: Bestimme anhand der URL die Quelle (arxiv, DOI, Publisher, Google Drive)
2. **Direkt-Zugriff versuchen**: Verwende `web_fetch` für arxiv, DOI und Publisher-Links
3. **Google Drive**: Verwende `google_drive_fetch` (nur Google Docs, keine PDFs)
4. **Freitext/Titel**: Suche via `web_search` nach dem Paper
5. **Dateinamen**: Extrahiere PII-Nummer oder Titel-Hinweise, dann Web-Suche
6. Falls Paper nicht direkt lesbar: Extrahiere Metadaten von der Landing Page (Abstract, Autoren, Datum)

## Schritt 2: Paper-Beschaffung

**Priorität der Quellen:**
1. **arXiv** (https://arxiv.org) - Open Access, meist vollständig verfügbar
2. **DOI-Resolver** (https://doi.org/) - Leitet zu Publisher weiter
3. **Web-Suche** - Nach Titel oder Autoren suchen
4. **Publisher-Websites** - Falls Open Access verfügbar

**Strategie bei ScienceDirect-Papers:**
- Dateiname: `1-s2.0-SXXXXXXXXX-main.pdf`
- PII-Nummer extrahieren (S-Teil)
- Web-Suche mit: `"S2666920X25000736" site:sciencedirect.com`
- Oder: Titel-basierte Suche wenn PII nicht hilft

**Wenn Paper nicht öffentlich verfügbar:**
Informiere den User: "Das Paper '[Titel/Dateiname]' ist nicht öffentlich zugänglich. Bitte laden Sie das PDF hoch oder teilen Sie einen direkten Link zur Quelle."

## Schritt 3: Vollständige Analyse

Verwende `web_fetch` Tool um Paper-Seiten zu laden. Extrahiere:

### Basis-Metadaten
- **Title**: Vollständiger, exakter Titel
- **Authors**: Alle Autoren, kommasepariert (z.B. "Müller M, Schmidt A, Weber T")
- **Publication**: Datum im Format DD/MM/YYYY (z.B. "15/03/2024")
- **PDF_Link**: Original arXiv/DOI/Publisher-Link (z.B. "https://arxiv.org/abs/2403.12345")

### Klassifikation (siehe `references/notion-fields.md` für Details)

**Typ**: Wähle aus: Paper, Article, Study, Course, Video
- Standard: "Paper" für wissenschaftliche Publikationen

**Status**: Immer "To Read" setzen

**Topics** (Multi-Select, alle zutreffenden wählen):
- NLP, Computer Vision, Machine Learning, AI Ethics, LLM, Transformer, Deep Learning, Reinforcement Learning, Multimodal
- Berücksichtige sowohl technische Methoden als auch Anwendungsdomäne

**UseCase** (Multi-Select, 1-3 wählen):
- Research: Grundlagenforschung, wissenschaftliche Erkenntnisse
- Strategy: GL-Entscheidungen, Policy-Entwicklung, Thought Leadership
- Implementation: Konkrete Umsetzung in Schulamt/Verwaltung
- Education: Unterricht, Lernprozesse, Sonderpädagogik
- Analysis: Datenbasierte Erkenntnisse, Evaluationen
- Communication: PR, Media Relations, Content Creation

**Zielgruppe** (Multi-Select, 1-3 primäre wählen):
- Executives: GL-relevante, strategische Inhalte
- Developers: Technische Umsetzung
- Researchers: Wissenschaftliche Tiefe
- General: Breite Anwendbarkeit
- Students: Lernmaterialien

### Inhaltliche Analyse

**Summary** (3-4 Sätze, KRITISCH WICHTIG):

**Struktur:**
1. Satz: Kernaussage/Forschungsfrage
2. 1-2 Sätze: Haupterkenntnisse/Resultate  
3. Satz: Relevanz für mindestens EINEN dieser Bereiche:
   - Bildungskontext (Unterricht, Lernprozesse, Lehrerunterstützung)
   - Sonderpädagogik (individualisierte Förderung, Inklusion, adaptive Systeme)
   - Verwaltungseffizienz (Prozessoptimierung, Automatisierung, Ressourceneinsparung)
   - Strategische Positionierung (Thought Leadership, Policy-Entwicklung)
   - Marktchancen für AI-Startups (innovative Lösungen, neue Geschäftsmodelle)

**Qualitätskriterien:**
- Schweizerische Rechtschreibung verwenden
- Geschäftsleitungsebene-taugliche Sprache (präzise, professionell)
- Konkrete Anwendungsfälle für Schulamt/Stadtverwaltung Zürich identifizieren
- Verwaltungsdigitalisierungs-Potenzial hervorheben
- Sonderpädagogik-Relevanz bei adaptiven Systemen betonen
- Startup/Markt-Opportunitäten aufzeigen wenn relevant
- Policy- und Governance-Implikationen berücksichtigen

**Notes** (optional, aber wertvoll):
Zusätzliche Informationen die in keinem anderen Feld Platz hatten:
- Verwaltungs-spezifische Implikationen
- Sonderpädagogik-Potenzial (Details)
- Implementierungshürden oder -chancen
- Vergleich zu ähnlichen Ansätzen
- Kritische Bewertung der Methodik

### Links und leere Felder
- **NotebookLM**: Leer lassen
- **Rating**: Leer lassen  
- **LearningItems**: Leer lassen

## Schritt 4: Notion-Integration

**Datenbank:**
- ID: `d8d80ff0d3034736970ea9a9349b405c`
- URL: https://www.notion.so/hayal/d8d80ff0d3034736970ea9a9349b405c

**Tool verwenden:**
```
notion-create-pages mit:
parent: {
  database_id: "d8d80ff0d3034736970ea9a9349b405c"
}
```

**Property-Mapping (WICHTIG - exakte Namen verwenden):**
```javascript
properties: {
  "Title": "Paper-Titel hier",
  "Status": "To Read",
  "Typ": "Paper",
  "Topics": ["NLP", "Machine Learning"],  // Array
  "UseCase": ["Strategy", "Education"],   // Array
  "Zielgruppe": ["Executives"],           // Array
  "Summary": "3-4 Sätze Summary hier...",
  "Authors": "Autor1, Autor2, Autor3",
  "date:Publication:start": "2024-03-15",  // YYYY-MM-DD Format!
  "date:Publication:is_datetime": 0,
  "PDF_Link": "https://arxiv.org/abs/...",
  "Google Drive File": "https://drive.google.com/...",
  "Notes": "Zusätzliche Informationen..."
}
```

**KRITISCHE Hinweise:**
- Date Properties werden aufgeteilt: `date:Publication:start`, `date:Publication:is_datetime`
- Datumsformat in properties: YYYY-MM-DD (nicht DD/MM/YYYY!)
- Multi-Select Felder sind Arrays: `["Option1", "Option2"]`
- Leere Felder (Rating, NotebookLM, LearningItems) NICHT in properties aufnehmen
- Field-Namen sind case-sensitive

## Schritt 5: Reporting

Nach erfolgreicher Integration ALLER Papers: Erstelle Übersichtstabelle

**Format:**
```markdown
## Übersicht eingefügte Papers

| Nr. | Title | Topics | UseCase | Relevanz | Einschätzung |
|-----|-------|--------|---------|----------|--------------|
| 1   | ...   | ...    | ...     | Hoch     | ...          |
| 2   | ...   | ...    | ...     | Mittel   | ...          |
```

**Relevanz-Kategorien:**
- **Hoch**: Direkt umsetzbar, GL-relevante Strategieentscheidungen, unmittelbarer Nutzen
- **Mittel**: Mittelfristig relevant, Thought Leadership, Potenzial für Pilotprojekte
- **Spezifisch**: Fokus auf Teilbereich (z.B. nur Sonderpädagogik, nur Kommunikation)

**Einschätzung** (ein prägnanter Satz):
Konkretester Nutzen für Schulamt oder Stadtverwaltung Zürich.

## Fehlerbehandlung

**Paper nicht zugänglich:**
```
Paper '[Titel/Dateiname]' ist nicht öffentlich verfügbar. 
Optionen:
1. PDF direkt hochladen
2. Zugänglichen alternativen Link teilen
3. Wenn verfügbar: ArXiv Preprint-Link verwenden
```

**Metadaten unvollständig:**
- Ergänze mit Web-Suche
- Markiere fehlende Informationen in Notes: "⚠️ Publikationsdatum nicht gefunden"
- Setze Plausible Defaults (z.B. aktuelles Jahr wenn kein Datum)

**Notion-API Fehler:**
```
Fehler beim Einfügen in Notion-Datenbank: [Fehlermeldung]

Vorbereitete Daten für manuelle Eingabe:
[Strukturierte Darstellung aller Felder]
```

## Spezielle Aufmerksamkeitsbereiche

Bei Papers zu folgenden Themen besondere Sorgfalt:

**AI in Public Administration:**
- UseCase: Strategy + Implementation
- Fokus auf konkrete Anwendungsfälle für Stadtverwaltung
- Policy-Implikationen hervorheben

**Adaptive Learning Systems:**
- UseCase: Education
- Sonderpädagogik-Relevanz ausführlich beschreiben
- Individualisierungs-Potenzial betonen

**Process Automation:**
- UseCase: Implementation
- Verwaltungseffizienz-Potenzial quantifizieren wenn möglich
- Ressourceneinsparungen identifizieren

**AI Ethics & Governance:**
- UseCase: Strategy
- GL-Relevanz klar darstellen
- Policy-Entwicklung Bezug herstellen

**Personalization at Scale:**
- UseCase: Education + Strategy
- Sonderpädagogik UND reguläre Volksschule berücksichtigen
- Datenschutz-Aspekte nicht vergessen

**Startup/Market Opportunities:**
- Marktpositionierung analysieren
- Partnerschafts-Potenziale identifizieren
- Innovative Geschäftsmodelle hervorheben

## Best Practices

1. **Kontext zuerst**: IMMER `references/user-context.md` und `references/notion-fields.md` konsultieren
2. **Vollständigkeit**: Alle 18 Felder beachten, auch wenn einige leer bleiben
3. **Qualität vor Quantität**: Summary ist das wichtigste Feld - investiere hier die meiste Sorgfalt
4. **Systematisch**: Ein Paper nach dem anderen, keine Parallelverarbeitung
5. **Transparenz**: Bei Unsicherheiten oder fehlenden Infos offen kommunizieren
6. **Relevanz**: Immer die User-Perspektive (GL-Mitglied, Schulamt, KI-Fachgruppe) berücksichtigen
7. **Schweizer Kontext**: Schweizerische Rechtschreibung, lokaler Bezug wo möglich

## Resources

### references/
- `user-context.md` - Vollständiger Kontext zu Rolle und Perspektiven
- `notion-fields.md` - Detaillierte Felddefinitionen und Qualitätskriterien

### scripts/
- `pdf_analyzer.py` - Hilfsskript für PDF-Analyse (optional, manueller Einsatz)
