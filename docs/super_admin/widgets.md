# Widgets

The **Widgets** section manages the catalog of widget definitions available in the platform.
Each widget definition is the administrative record that corresponds to a visual component displayed in dashboards.

!!! warning
    This section is reserved for **Super Admin** users. Changes here affect the entire platform and all users.

---

## Opening the section

From the main navigation menu, go to **Administration → Super Admin → Widgets**.

The interface opens with a table listing all widget definitions.

| Column | Description |
|---|---|
| Name | Human-readable name of the widget |
| Code | Unique technical identifier |
| Scope | Context in which the widget can be used |
| Status | Active or Disabled |
| Description | Optional description |

The table can be filtered by **Scope** and **Status**.

---

## Widget details

Click the **search icon (🔍)** on any row to open the widget record.

| Field | Description |
|---|---|
| Name | Display name of the widget |
| Code | Unique identifier used by the frontend to resolve the widget component |
| Scope | Context in which the widget is available |
| Status | Active or Disabled |
| Description | Optional description |

!!! note
    The **Code** field is the technical key that links this administrative record to the actual visual component in the frontend. It must match exactly the identifier used in the frontend implementation.

---

## Connections View

Click the **link icon (🔗)** on any row to open the Connections View.

| Tab | Description |
|---|---|
| Dashboards | Dashboards that include this widget, with layout properties (position, size, settings) |
| Widget Groups | Widget groups this widget belongs to |

### Dashboard placement properties

When a widget is linked to a dashboard, the association stores the widget's position and size in the dashboard grid:

| Property | Description |
|---|---|
| Index | Ordering of the widget within the dashboard |
| Width | Width in grid units |
| Height | Height in grid units |
| Grid X | Horizontal grid position |
| Grid Y | Vertical grid position |
| Settings | Widget-specific configuration payload |

---

!!! note
    To control which users can see a widget, assign it to a **Widget Group** and then assign that group to the relevant users.
    See [Widget Groups](widget_groups.md).
