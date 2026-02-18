# Notion AI Papers Skill

🌐 [English](README.md) | [Deutsch](README.de.md)

A specialized Claude Skill for the systematic analysis of AI research papers and their structured integration into Notion databases.

## 🎯 Overview

This skill was developed for the efficient processing of scientific publications. It automates the workflow from paper identification to structured storage in Notion.

**Designed for:** Individuals and organizations  
**Application context:** AI specialist groups, executive-level decision-making, education research, etc.

## ✨ Key Features

* **Automatic Paper Analysis**: Extracts metadata, key findings, and relevance assessments
* **Multi-Source Retrieval**: Supports arXiv, DOI, ScienceDirect, Google Drive
* **Notion Integration**: Direct insertion into structured databases
* **Focused Evaluation**: Specialized in education, public administration digitization, AI governance
* **Reporting**: Automatic overview tables with relevance ratings

## 🚀 Usage

### Prerequisites

* Access to Claude (claude.ai or API)
* Notion database with corresponding fields (see [Notion Field Definitions](references/notion-fields.md))
* Optional: Google Drive integration

### Installation

1. Load the skill into your Claude Skills directory:

   ```
   /mnt/skills/user/notion-ai-papers/
   ```
2. Ensure the following files are present:

   * `SKILL.md` (main skill definition)
   * `references/user-context.md`
   * `references/notion-fields.md`
   * `scripts/pdf_analyzer.py` (optional)

For detailed installation instructions, see [INSTALLATION.md](INSTALLATION.md) ([Deutsch](INSTALLATION.de.md)).

### Example Usage

```
User: "Here's a paper on AI in Education: 
https://drive.google.com/open?id=1ABC..."

Claude: [Analyzes paper, extracts metadata, 
inserts into Notion database, creates summary]
```

## 📋 Workflow

```
1. Paper Identification
   ↓
2. Retrieval (arXiv, DOI, Web)
   ↓
3. Full Analysis
   - Metadata
   - Classification
   - Content Analysis
   ↓
4. Notion Integration
   ↓
5. Reporting & Overview Table
```

## 🎓 Focus Areas

The skill evaluates papers with particular emphasis on:

* **Education**: Teaching, learning processes, teacher support
* **Special Education**: Individualized support, inclusion, adaptive systems
* **Administrative Efficiency**: Process optimization, automation
* **Strategic Positioning**: Thought leadership, policy development
* **Market Opportunities**: Innovative solutions, new business models

## 📁 Structure

```
notion-ai-papers/
├── SKILL.md                      # Main skill definition (German)
├── README.md                     # Documentation (English)
├── README.de.md                  # Documentation (German)
├── CONTRIBUTING.md               # Contribution guidelines (English)
├── CONTRIBUTING.de.md            # Contribution guidelines (German)
├── INSTALLATION.md               # Installation guide (English)
├── INSTALLATION.de.md            # Installation guide (German)
├── CHANGELOG.md                  # Changelog (English)
├── CHANGELOG.de.md               # Changelog (German)
├── LICENSE                       # MIT License
├── references/
│   ├── user-context.md          # Role profile and perspectives
│   └── notion-fields.md         # Notion field definitions
└── scripts/
    └── pdf_analyzer.py          # Helper script (optional)
```

## 🔧 Configuration

### Notion Database

Required fields (see `references/notion-fields.md` for details):

* **Basic**: Title, Status, Type
* **Classification**: Topics, UseCase, Target Audience
* **Metadata**: Authors, Publication, PDF\_Link
* **Content**: Summary, Notes
* **Links**: Google Drive File, NotebookLM
* **Rating**: Rating, LearningItems

### Adapting to Your Own Notion Database

1. Update the database ID in `SKILL.md` (line 129)
2. Ensure all field names match
3. Adapt `references/notion-fields.md` to your requirements

## 📖 Documentation

* **[SKILL.md](SKILL.md)**: Complete skill definition with detailed workflow (German)
* **[User Context](references/user-context.md)**: Role profile and perspectives
* **[Notion Fields](references/notion-fields.md)**: Detailed field definitions

## 🤝 Contributing

This project is designed as an example of specialized Claude Skills. Feedback and improvement suggestions are welcome:

* Issues for bugs or feature requests
* Pull requests for improvements
* Discussions for adaptations to other contexts

See [CONTRIBUTING.md](CONTRIBUTING.md) ([Deutsch](CONTRIBUTING.de.md)) for details.

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

Developed for individuals and organizations.

---

**Note**: The SKILL.md is written in German, as it is specifically tailored to the context of Swiss public administration and education. The operational skill language is German, while this documentation is provided in both English and German. For other use cases, adaptations in `references/user-context.md` and `SKILL.md` are required.

---

<div align="center">

**Made with ❤️ in Zürich**

[LinkedIn](https://www.linkedin.com/in/hayaloezkan/) • [Documentation](docs/) • [Contributing](CONTRIBUTING.md)

</div>
