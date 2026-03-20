# Tree Hierarchy View

The **Tree Hierarchy View** lets you navigate the monitored infrastructure as a structured hierarchy, expanding levels progressively from a root entity down to individual metrics and services.

---

## Accessing the view

The Tree Hierarchy View is available for **Objects**, **Groups**, and **Customers**.

- For **Objects**: clicking the **link icon** on a table row opens the Tree Hierarchy View directly.
- For **Groups** and **Customers**: open the Connections view, then use the **toggle switch** in the top bar to switch to the Tree Hierarchy View.

From the Tree Hierarchy View, use the **Connections View** button in the top bar to switch back.

---

## Page layout

The page is divided into two panels:

- **Left panel** — read-only details of the selected root entity, with action buttons such as **EDIT INFORMATIONS** and **DOWNTIMES**
- **Right panel** — the expandable hierarchy of related entities

![Tree Hierarchy View layout](../images/data_manager/tree_hierarchy/layout.png)
/// caption
Fig.1 — Tree Hierarchy View — entity details on the left, expandable hierarchy on the right
///

---

## Hierarchy structure

The right panel displays the infrastructure as expandable sections. Click any row to expand it and reveal the next level.

A typical navigation path from a Customer looks like:

1. **Customer**
2. **Sites**
3. **Groups**
4. **Objects**
5. **Metric Types**
6. **Metrics / Services**

![Hierarchy expansion](../images/data_manager/tree_hierarchy/hierarchy_expansion.png)
/// caption
Fig.2 — Progressive expansion of hierarchy levels from Customer to Metrics
///

!!! note
    The available levels depend on the entity type and its configuration. Not all paths lead to the same depth.

---

## Hierarchy tabs

Some entities offer multiple hierarchical perspectives accessible via tabs at the top of the right panel.

For example, a **Customer** can expose:

- **Sites** — the geographic and logical grouping of objects
- **Service Profiles** — the service-oriented view of the same infrastructure

![Hierarchy tabs](../images/data_manager/tree_hierarchy/tabs.png)
/// caption
Fig.3 — Hierarchy tabs on a Customer — Sites and Service Profiles
///

---

## Filtering the hierarchy

Next to the hierarchy tabs, a **filter icon** lets you narrow down the rows displayed in the right panel.

Two filter modes are available:

| Filter | Description |
|---|---|
| **Filter by name or code** | Type a string to show only rows whose name or code contains the entered text |
| **Severity** | Select one or more status values (green, red, yellow, purple, gray) to show only rows matching that status |

The filter applies to the currently visible level. Clear the filter to restore the full list.

When viewing a **Customer** hierarchy, an additional **Disabled sites** toggle is available next to the filter icon. Disabled sites are hidden by default — enable the toggle to include them in the hierarchy.

![Hierarchy filter](../images/data_manager/tree_hierarchy/filter.png)
/// caption
Fig.4 — Hierarchy filter — name/code search and severity selector
///

---

## Entity rows

Each row in the hierarchy shows:

- A **status indicator** (colored dot)
- The entity **name** and identifier
- Optional **child counters**
- **Action icons** on the right side

![Entity row actions](../images/data_manager/tree_hierarchy/entity_row.png)
/// caption
Fig.5 — Entity row with status indicator and contextual action icons
///

---

## Row actions

Each row exposes contextual action icons depending on the entity type.

### View metric data

Click the **chart icon** to open the metric data modal.

The modal displays:

- Time range filters
- Historical values in table or chart form

![Metric data modal](../images/data_manager/tree_hierarchy/metric_data_modal.png)
/// caption
Fig.6 — Metric data modal with historical values and time filters
///

!!! info
    Use the date range selector to focus the analysis on a specific period.

---

### Manage downtimes

Click the **clock icon** to open the **Active Downtimes** modal.

From the modal you can:

- View scheduled downtime periods
- Add a new downtime

![Active Downtimes modal](../images/data_manager/tree_hierarchy/downtime_modal.png)
/// caption
Fig.7 — Active Downtimes modal
///

!!! warning
    Downtimes suppress monitoring alerts. Apply them only during planned maintenance windows.

---

### Open dispatchers

Click the **paper plane icon** to access the dispatchers associated with the entity.

Dispatchers define automated actions triggered by monitoring events.

---

### Open entity structure

Click the **external link icon** to open the full structure page for the selected entity.

From there you can switch between the Tree Hierarchy View and the Connections View.

---

### Open entity details

Click the **magnifier icon** to open the entity's CRUD dialog.

From the dialog you can view, edit, duplicate, or delete the record.

---

## Services

Some branches expose **Services** rather than metrics. A service represents a higher-level aggregation of monitoring data (for example `cost.analytics.forecast.monthly`).

Opening a service row displays time-based data in the same format as the metric data modal.

![Service data modal](../images/data_manager/tree_hierarchy/service_data_modal.png)
/// caption
Fig.8 — Service data modal — example: forecast cost monthly
///

---

## Tree Hierarchy View vs Connections View

| | Tree Hierarchy View | Connections View |
|---|---|---|
| **Purpose** | Navigate the structural hierarchy of an entity | Explore relationships between entities |
| **Layout** | Expandable levels, top-down | Two-panel, tab-based |
| **Typical use** | Understand where an object belongs and reach its metrics | Link or unlink related records |

Use the **Tree Hierarchy View** to drill from a customer or site down to individual metrics.
Use the **Connections View** to manage associations between entities.
