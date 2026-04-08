# CLAUDE.md — XAUTOMATA User Manual Project

This file provides context for Claude (VS Code extension or CLI) when working on this project.
Read this before making any changes to the documentation.

---

## What this project is

This is the **operational user manual** for the **XAUTOMATA platform** — a Digital Twin platform
for monitoring, automating and governing complex IT and cloud infrastructures.

The manual is built with **MkDocs + Material theme**. It is a **bilingual project**: English is
the default language, Italian is the secondary language, managed via the MkDocs Material `i18n`
plugin.

### Target audience
- **Operators and analysts** who use dashboards daily
- **Administrators** who configure the platform

### Tone and purpose
This is an **operational manual**, not a technical reference.
- Focus on **what to do and how to do it**
- Avoid internal technical details unless strictly necessary
- Write in the second person ("clicca", "seleziona", "apri" in Italian; "click", "select", "open" in English)
- Short sentences, direct language

---

## i18n setup

The project uses the MkDocs Material `i18n` plugin with the following convention:

- `page.md` → **English** (default, served at `/page/`)
- `page.it.md` → **Italian** (served at `/it/page/`)

Images are **shared** between languages — paths are identical in both versions.
The language switcher is rendered automatically by the Material theme.

### Bilingual maintenance rules

The Italian translation is **complete** — every `page.md` has a corresponding `page.it.md`.

**Any change to the English version must be reflected in the Italian version.** This applies to:
- New pages: create both `page.md` and `page.it.md` together
- Content edits: apply the equivalent change to the `.it.md` file in the same session
- Structural changes (sections added/removed): mirror them in Italian

Do not leave the two versions out of sync. If a factual correction is made to the English source, fix the Italian too.

---

## Italian adaptation rules

The XAutomata UI is in **English**. Italian pages must handle UI terms intelligently:

### General principle
Translate the prose into natural Italian, but **preserve English UI labels** exactly as they
appear in the interface (button names, menu items, field labels, section titles).

### Strategies by case

| Situation | Strategy | Example |
|---|---|---|
| UI element used inline | Keep English, add Italian gloss on first use | `la vista **Tree Hierarchy** (gerarchia ad albero)` |
| UI element repeated | Use English alone after first introduction | `Apri la Tree Hierarchy View` |
| Ambiguous term | English in parentheses | `il pannello di filtro (*filter panel*)` |
| Purely descriptive concept | Translate fully | `clicca sul pulsante di salvataggio` |

### Do not
- Translate button labels, field names, or menu items that appear verbatim in the UI
- Invent Italian equivalents for product-specific terms (e.g. "Virtual Domain", "Probe", "Dispatcher")
- Use overly formal or bureaucratic Italian — keep the same direct, operational tone as the English version

### Gender of English loanwords
- **dashboard** is feminine: "la dashboard", "le dashboard", "una dashboard"
  - Adjectives and participles must agree: "condivisa", "visualizzate", "stessa", "mostrata", ecc.

### Second person
- Use the **informal "tu"** form throughout: "clicca", "seleziona", "apri", "inserisci"
- Avoid "Lei" or passive constructions

---

## Writing style rules

These rules are established and must be followed consistently:

### Language
- **English pages**: always English, second person imperative ("Click **SAVE CHANGES**")
- **Italian pages**: Italian prose + English UI labels, informal "tu", present tense
- Present tense throughout in both languages

### MkDocs Material syntax
- Admonitions: `!!! info`, `!!! warning`, `!!! note`, `!!! example`
- Image captions: `/// caption` / `///` block immediately after the image
- Always number captions: `Fig.1 - Description`, `Fig.2 - Description`

### Images
- Path convention: `../images/<section>/<subsection>/<filename>.png`
- Example: `../images/dashboards/cloud_cost/cloud_cost_dashboard.png`
- Always include a caption with figure number

### Internal links
- Always use relative paths: `../widgets/cloud_cost.md#costs-by-day`
- Widget anchors follow the pattern `#widget-title-in-lowercase-with-hyphens`

### Page structure
- Each page starts with a short intro sentence (1-2 lines max) explaining what the page covers
- Use `---` horizontal rules to separate major sections
- Tables for structured comparisons (buttons, fields, roles)
- Numbered lists for sequential steps
- Bullet lists for non-sequential items

---

## Project structure

```
xautomata-user-manual/
├── mkdocs.yml                  # MkDocs navigation and config
├── CLAUDE.md                   # This file
├── qa.md                       # ✅ Open questions log for domain experts
└── docs/
    ├── index.md                # Manual home page
    ├── images/                 # All screenshots and images
    │   ├── getting_started/
    │   ├── dashboards/
    │   │   ├── cloud_cost/
    │   │   ├── it_infrastructure/
    │   │   └── network/
    │   ├── data_manager/
    │   │   ├── customers/
    │   │   ├── contacts/
    │   │   ├── sites/
    │   │   ├── groups/
    │   │   ├── objects/
    │   │   ├── metric_types/
    │   │   ├── metrics/
    │   │   ├── services/
    │   │   └── tree_hierarchy/
    │   ├── tracking/
    │   │   ├── calendars/
    │   │   ├── downtimes/
    │   │   └── dispatchers/
    │   ├── administration/
    │   │   ├── users/
    │   │   ├── virtual_domains/
    │   │   ├── probes/
    │   │   ├── probe_types/
    │   │   ├── messages/
    │   │   ├── notification_providers/
    │   │   └── notification_provider_types/
    │   ├── cost_management/
    │   │   ├── cloud_cost_registration/
    │   │   └── cost_views/
    │   └── widgets/
    ├── getting_started/
    │   ├── login.md                        # ✅ written
    │   └── navigation.md                   # ✅ written
    ├── dashboards/                         # ✅ COMPLETE
    │   ├── index.md
    │   ├── management.md
    │   ├── it_infrastructure.md
    │   ├── network.md
    │   └── cloud_cost.md
    ├── widgets/                            # ✅ COMPLETE (from colleague)
    │   ├── overview.md
    │   ├── it_infrastructure.md
    │   ├── it_analytics.md
    │   ├── it_anomalies.md
    │   ├── network.md
    │   ├── network_analytics.md
    │   ├── net_flow.md
    │   ├── support_service_kpi.md
    │   ├── cloud_cost.md
    │   ├── analytical_accounting.md
    │   ├── mcd_dedicated.md
    │   ├── mcd_reboot.md
    │   ├── mcd_rebuild_vm.md
    │   └── mcd_downtime.md
    ├── data_manager/                       # ✅ COMPLETE
    │   ├── overview.md                     # ✅ written
    │   ├── working_with_entities.md        # ✅ written
    │   ├── tree_hierarchy_view.md          # ✅ written
    │   ├── customers/
    │   │   ├── customers.md                # ✅ written
    │   │   ├── contacts.md                 # ✅ written
    │   │   └── sites.md                    # ✅ written
    │   ├── objects/
    │   │   ├── groups.md                   # ✅ written
    │   │   ├── objects.md                  # ✅ written
    │   │   ├── metric_types.md             # ✅ written
    │   │   ├── metrics.md                  # ✅ written
    │   │   └── services.md                 # ✅ written
    │   └── tracking/
    │       ├── calendars.md                # ✅ written
    │       ├── downtimes.md                # ✅ written
    │       └── dispatchers.md              # ✅ written
    ├── cost_management/                    # ✅ COMPLETE
    │   ├── overview.md                     # ✅ written
    │   ├── cloud_cost_registration.md      # ✅ written
    │   └── cost_views.md                   # ✅ written (Nodes Tree; Azure Tags coming soon)
    ├── administration/                     # ✅ COMPLETE
    │   ├── overview.md                     # ✅ written
    │   ├── access_control.md               # ✅ written
    │   ├── users.md                        # ✅ written
    │   ├── virtual_domains.md              # ✅ written
    │   ├── probes.md                       # ✅ written
    │   ├── probe_types.md                  # ✅ written
    │   ├── messages.md                     # ✅ written
    │   ├── notification_providers.md       # ✅ written
    │   └── notification_provider_types.md  # ✅ written
    └── super_admin/                        # ✅ COMPLETE
        ├── widgets.md                      # ✅ written
        ├── widget_groups.md                # ✅ written
        ├── dashboards.md                   # ✅ written
        └── acl_overrides.md                # ✅ written
```

---

## Open questions

A `qa.md` file tracks questions that emerged during writing and need verification by a domain expert.
Always check `qa.md` before finalizing pages related to:

- Access control and user permissions (Q1)
- Cost Views — Azure Tags origin (Q2)
- Cost Views — child node resource scoping (Q3)

---

## Known limitations / pending items

- **Screenshots**: all pages use placeholder image paths. Screenshots need to be added by the user following the path convention.
- **Cost Views — Azure Tags type**: the configuration interface is `Coming soon` in the platform. The page documents the Nodes Tree type only.

---

## Source reference

The **technical reference manual** is available in the project knowledge base (uploaded to this
Claude project). It covers the same topics in depth and is the authoritative conceptual source.

When writing a new page:
1. Search the project knowledge for the relevant technical page
2. Extract the **operational meaning** — what the user needs to do, not how it works internally
3. Follow the writing style rules above
4. Add screenshots where available (ask the user to provide them)

### Key conceptual mapping (technical → operational)

| Technical manual section | Operational manual section |
|---|---|
| Platform Concepts / System Overview | Not included — too technical |
| Platform Models | Not included — too technical |
| Access / Login | getting_started/login.md |
| User Interface | getting_started/navigation.md |
| Data Manager | data_manager/ |
| Dashboards | dashboards/ |
| Cost Management | cost_management/ |
| Widgets | widgets/ |
| Administration | administration/ |
| Super Admin | super_admin/ |

---

## Co-authors

### English version
- **Colleague**: wrote the original widget pages (`widgets/`), initial dashboard pages, `working_with_entities.md`, and `tree_hierarchy_view.md`. His style is the reference — keep it consistent.
- **Session 1**: wrote `dashboards/index.md`, `dashboards/management.md`.
- **Session 2**: wrote all remaining pages across `data_manager/`, `cost_management/`, `administration/`, `super_admin/`, `getting_started/navigation.md`.

### Italian adaptation (`.it.md` files)
- **Complete** — all pages have an Italian version.
- Going forward, update both `.md` and `.it.md` whenever a page is added or modified.

---

## Screenshot workflow

Screenshots are provided by the user during the documentation session.
When a page references screenshots that are not yet available, use placeholder paths
following the naming convention and note them for the user to fill in.

Placeholder format:
```markdown
![Description](../images/section/subsection/filename.png)
/// caption
Fig.N - Description (screenshot pending)
///
```
