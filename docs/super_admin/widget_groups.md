# Widget Groups

The **Widget Groups** section manages logical collections of widgets.
A widget group bundles related widgets together and controls which users can access them — assigning a group to a user grants visibility of all widgets in that group.

!!! warning
    This section is reserved for **Super Admin** users. Changes here affect widget visibility for all assigned users.

---

## Opening the section

From the main navigation menu, go to **Administration → Super Admin → Widget Groups**.

The interface opens with a table listing all widget groups.

| Column | Description |
|---|---|
| Name | Human-readable name of the group |
| Code | Unique identifier |
| Status | Active or Disabled |
| Description | Optional description |

---

## Widget group details

Click the **search icon (🔍)** on any row to open the widget group record.

| Field | Description |
|---|---|
| Name | Display name of the group |
| Code | Unique identifier used internally by the platform |
| Status | Active or Disabled |
| Description | Optional description |

From this dialog you can edit, duplicate, or delete the group.

---

## Connections View

Click the **link icon (🔗)** on any row to open the Connections View.

| Tab | Description |
|---|---|
| Widgets | Widget definitions included in this group |
| Users | Users assigned to this widget group |

### Widgets tab

Shows all widget definitions linked to this group. Use this tab to add or remove widgets from the group.

### Users tab

Shows all users who have been assigned this widget group. Users linked here gain visibility of all widgets in the group.

!!! note
    Widget group assignment is also manageable from the user side — see the **Widget Groups** tab in the [Users](../administration/users.md) Connections View.

---

## How widget visibility works

```
Widget Group → contains Widgets
Widget Group → assigned to Users
↓
User sees Widgets in their assigned groups
```

When a user opens a dashboard, only widgets belonging to their assigned widget groups appear in the widget catalog. If a widget group is inactive or not assigned to the user, its widgets are not visible.

---

!!! note
    To manage which dashboards a user can access (separate from widget visibility), see [Users](../administration/users.md) and [Dashboards](dashboards.md).
