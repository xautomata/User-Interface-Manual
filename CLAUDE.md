# CLAUDE.md — XAUTOMATA User Manual Project

This file provides context for Claude (VS Code extension or CLI) when working on this project.
Read this before making any changes to the documentation.

---

## What this project is

This is the **operational user manual** for the **XAUTOMATA platform** — a Digital Twin platform
for monitoring, automating and governing complex IT and cloud infrastructures.

The manual is built with **MkDocs + Material theme** and written in **English**.

### Target audience
- **Operators and analysts** who use dashboards daily
- **Administrators** who configure the platform

### Tone and purpose
This is an **operational manual**, not a technical reference.
- Focus on **what to do and how to do it**
- Avoid internal technical details unless strictly necessary
- Write in the second person ("click", "select", "open")
- Short sentences, direct language

---

## Writing style rules

These rules are established and must be followed consistently:

### Language
- Always **English**
- Second person imperative for instructions ("Click **SAVE CHANGES**")
- Present tense throughout

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
└── docs/
    ├── index.md                # Manual home page
    ├── images/                 # All screenshots and images
    │   ├── getting_started/
    │   ├── dashboards/
    │   │   ├── cloud_cost/
    │   │   ├── it_infrastructure/
    │   │   └── network/
    │   └── widgets/
    ├── getting_started/
    │   ├── login.md
    │   └── navigation.md
    ├── dashboards/             # ✅ COMPLETE
    │   ├── index.md
    │   ├── management.md
    │   ├── it_infrastructure.md
    │   ├── network.md
    │   └── cloud_cost.md
    ├── widgets/                # ✅ COMPLETE (from colleague)
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
    ├── data_manager/           # 🚧 STUB — to be written
    │   ├── overview.md
    │   ├── working_with_entities.md
    │   ├── tree_hierarchy_view.md
    │   ├── customers/
    │   ├── objects/
    │   └── monitoring/
    ├── cost_management/        # 🚧 STUB — to be written
    ├── administration/         # 🚧 STUB — to be written
    └── super_admin/            # 🚧 STUB — to be written
```

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

- **Colleague**: wrote the original widget pages (`widgets/`) and initial dashboard pages.
  His style is the reference — keep it consistent.
- **This session**: wrote `dashboards/index.md` and `dashboards/management.md`,
  integrating screenshots from the live platform.

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
