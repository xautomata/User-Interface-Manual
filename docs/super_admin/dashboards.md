# Dashboards

The **Dashboards** section in Super Admin manages the dashboard definitions available across the platform.
Use this section to create, configure, and organize dashboards — defining their type, scope, layout, and widget associations.

!!! warning
    This section is reserved for **Super Admin** users. Changes here affect the dashboards visible to all users of the platform.

---

## Opening the section

From the main navigation menu, go to **Administration → Super Admin → Dashboards**.

The interface opens with a table listing all dashboard definitions.

| Column | Description |
|---|---|
| Name | Name of the dashboard |
| Description | Optional description |
| Type | Global or Personal |
| Scope | Customers or Virtual Domains |
| User | Associated user (for Personal dashboards) |
| Order | Priority for ordering in the interface |
| Refresh Interval | Auto-refresh interval in milliseconds |

---

## Dashboard details

Click the **search icon (🔍)** on any row to open the dashboard record.

| Field | Description |
|---|---|
| Name | Display name of the dashboard |
| Description | Optional description |
| Type | Global or Personal |
| Scope | Customers or Virtual Domains |
| User | Associated user (Personal dashboards only) |
| Order | Ordering priority |
| Refresh Interval (ms) | How often the dashboard refreshes automatically |
| Thumbnail | Optional image reference for the dashboard card |

### Dashboard types

| Type | Description |
|---|---|
| **Global** | Shared dashboard available across multiple users and contexts |
| **Personal** | Dashboard associated with a specific user account |

### Dashboard scope

| Scope | Description |
|---|---|
| **Customers** | Dashboard is available in customer contexts |
| **Virtual Domains** | Dashboard is available in virtual domain contexts |

---

## Connections View

Click the **link icon (🔗)** on any row to open the Connections View.

| Tab | Description |
|---|---|
| Widgets | Widgets placed in this dashboard, with layout properties |
| Users | Users who have access to this dashboard |
| Customers | Customers this dashboard is associated with |

### Widgets tab

This is the most important relationship for a dashboard. Each widget association stores not just which widget is included, but also its **position and size** in the dashboard grid:

| Property | Description |
|---|---|
| Index | Ordering of the widget within the dashboard |
| Width | Width in grid units |
| Height | Height in grid units |
| Grid X | Horizontal position |
| Grid Y | Vertical position |
| Settings | Widget-specific configuration payload |

### Users tab

Shows the users who have access to this dashboard. Use this tab to grant or revoke dashboard access for specific users.

### Customers tab

Shows the customers this dashboard is associated with. Relevant for dashboards displayed in customer-specific contexts.

---

!!! note
    Dashboard layout and widget configuration can also be managed interactively from the dashboard interface itself.
    See [Dashboard Management](../dashboards/management.md) for the end-user workflow.
