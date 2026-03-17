# Cost Management Overview

The **Cost Management** section provides tools to connect XAUTOMATA to cloud providers, import billing data, and organize costs for analysis.

---

## How it works

Cost management in XAUTOMATA follows three steps:

1. **Register a cloud provider** — configure the credentials that allow XAUTOMATA to retrieve billing data from Azure, AWS, or Google Cloud.
2. **Import billing data** — the platform periodically queries the provider APIs and stores the raw cost data.
3. **Organize and analyze** — use the imported data directly through Cloud Cost dashboards, or reorganize it into custom structures using Cost Views for analytical accounting.

---

## Two analysis perspectives

Once data is imported, it can be analyzed in two ways:

| Perspective | Tool | Best for |
|---|---|---|
| **Raw billing data** | Cloud Cost widgets and dashboard | Monitoring spending trends, breakdowns by category, subscription, or resource group — as reported by the provider |
| **Custom cost structure** | Analytical Accounting widgets + Cost Views | Organizing costs by department, project, or cost center — according to your internal accounting model |

These two perspectives are complementary. Most organizations use both.

---

## Section contents

| Page | Purpose |
|---|---|
| [Cloud Cost Registration](cloud_cost_registration.md) | Configure connections to cloud providers |
| [Cost Views](cost_views.md) | Build custom cost hierarchies for analytical accounting |

---

!!! note
    Cloud Cost Registration is typically configured during onboarding by the XAUTOMATA delivery team.
    Cost Views are created and maintained by administrators according to the organization's accounting needs.
