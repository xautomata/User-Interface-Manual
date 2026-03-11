# Dashboard Management

Dashboards are the main workspace used to visualize and analyze operational data within XAUTOMATA.

After logging into the platform, users first select a **customer**.
Once a customer is selected, the platform displays the dashboards available for that customer.

Dashboards allow users to assemble visual components called **widgets** into a configurable layout, enabling operational monitoring, analytics, and reporting.

---

# Accessing Dashboards

The dashboard workflow typically follows these steps:

1. The user logs into the platform.
2. The user selects a **customer** from the list of available customers.
3. The platform loads the dashboards available for that customer.

Dashboards are presented in three categories depending on ownership and visibility.

---

# Dashboard Categories

## Personal Dashboards

Personal dashboards are created and owned by the current user.

These dashboards are visible only to the user who created them unless they are explicitly shared with other users or customers.

Users can:

* create new personal dashboards
* edit their dashboards
* share them
* delete them

---

## Shared Dashboards

Shared dashboards are dashboards created by another user and shared with the current user.

When a dashboard is shared:

* the same dashboard instance is visible to all users with access
* changes made to layout or widgets affect the shared dashboard for all users

This means shared dashboards behave as **collaborative dashboards** rather than read-only views.

Some operations, such as deletion, may be restricted for users who are not the dashboard owner.

---

## Global Dashboards

Global dashboards are dashboards defined at platform or organizational level.

They are typically maintained by administrators and provide standardized operational views.

Examples include dashboards for:

* IT Infrastructure
* Network Monitoring
* Cloud Cost Analysis

Global dashboards are usually visible to multiple users within the same organization or customer context.

---

# Creating a Personal Dashboard

Users can create a new personal dashboard from the **Personal Dashboards** section.

The creation dialog allows configuration of basic dashboard properties such as:

* dashboard name
* description
* refresh interval

After creation, the new dashboard appears in the list of personal dashboards and can be opened for editing.

---

# Sharing Dashboards

Personal dashboards can be shared with other users or customers.

The **Share Dashboard** dialog allows two sharing modes:

### Share with Users

The dashboard becomes visible to specific users.

### Share with Customers

The dashboard becomes visible to users associated with a selected customer.

Sharing does not create a copy of the dashboard.
Instead, it grants access to the same dashboard instance.

All users accessing the dashboard will see the same layout and widgets.

---

# Opening a Dashboard

Selecting a dashboard opens the dashboard workspace.

The dashboard page provides several actions:

* add widgets
* edit dashboard settings
* save layout changes
* delete the dashboard

In addition, dashboards may expose shared filters such as:

* customer
* reference month
* date range

These filters can affect multiple widgets simultaneously.

---

# Dashboard Editing Mode

To modify the layout or content of a dashboard, the user enters **editing mode**.

In editing mode the following actions become available:

* add widgets
* reposition widgets
* resize widgets
* configure widget settings
* modify dashboard properties

Changes are saved explicitly using the **Save Changes** action.

---

# Adding Widgets

Widgets can be added to a dashboard using the **Add Widget** action.

This opens the **Widgets Catalog**, a sidebar listing the widgets available to the user.

Widgets are organized into **widget groups** representing functional domains, for example:

* Analytical Accounting
* IT Infrastructure
* Cloud Cost
* Network Analytics

Only widgets belonging to groups enabled for the user are visible in the catalog.

Selecting a widget adds it to the dashboard layout.

---

# Dashboard Layout

Dashboards use a grid-based layout system.

Each widget occupies a rectangular area within the grid and can be moved or resized interactively.

The layout configuration is stored using the following parameters:

* `grid_x` – horizontal grid position
* `grid_y` – vertical grid position
* `width` – widget width in grid units
* `height` – widget height in grid units
* `index` – ordering index within the dashboard

Users can drag widgets to reposition them or resize them directly within the dashboard.

Layout changes are persisted when the user saves the dashboard.

---

# Widget Settings

Some widgets require configuration before displaying data.

If a widget requires configuration, a message indicates that settings must be defined.

Opening the widget settings dialog allows users to configure parameters required by the widget.

Examples of widget settings include:

* selecting a cost view
* selecting metrics or entities
* defining time ranges or filters

The structure of the settings dialog is defined by the widget configuration.

---

# Customer-Specific Settings

Certain widget settings can be marked as **Defined per Customer**.

When this option is enabled:

* each customer can have a different configuration for the same dashboard
* the dashboard layout remains the same
* widget data sources or parameters can vary by customer

This feature is useful in multi-tenant environments where dashboards are reused across multiple customers but reference customer-specific data.

---

# Editing Dashboard Properties

The **Dashboard Settings** action opens the dashboard configuration dialog.

This dialog allows modification of dashboard metadata such as:

* name
* description
* type (personal or global)
* associated user
* refresh interval
* ordering priority
* thumbnail image

These properties correspond to the underlying dashboard entity managed by the platform.

---

# Deleting Dashboards

Users can delete dashboards they own.

Deleting a dashboard removes it from all users who have access to it.

Users accessing a dashboard through sharing may not be able to delete the dashboard itself.

In such cases, removing access typically removes the dashboard from their shared dashboards list without affecting the original dashboard.

---

# Notes on Permissions

Dashboard behavior depends on user permissions and access control rules.

Administrative users may have extended capabilities such as:

* editing global dashboards
* modifying dashboards owned by other users
* managing dashboard visibility

Exact permissions depend on the platform's access control configuration.


---

# Dashboard Architecture

The dashboard system is implemented as a modular frontend architecture designed to support dynamic widget composition.

A dashboard does not directly contain widget implementations.
Instead, it renders widgets dynamically based on their configuration and type.

The main components involved in rendering dashboards are:

* `DashboardView`
* `WidgetsGrid`
* `WidgetCard`
* `WidgetDispatcher`

Together, these components manage layout, widget lifecycle, and rendering.

---

# Rendering Flow

When a dashboard is opened, the platform loads the dashboard configuration and the associated widgets.

The rendering flow follows this sequence:

```
DashboardView
      ↓
WidgetsGrid
      ↓
WidgetCard
      ↓
WidgetDispatcher
      ↓
Widget Component
```

Each component has a specific responsibility in the dashboard system.

---

# DashboardView

`DashboardView` is the main container for the dashboard page.

Its responsibilities include:

* loading the dashboard configuration
* retrieving associated widgets
* managing editing mode
* coordinating save operations
* providing global filters (such as customer or reference month)

The dashboard view initializes the widget grid and passes the widget configuration to the layout system.

---

# WidgetsGrid

`WidgetsGrid` manages the **layout engine** of the dashboard.

It is responsible for:

* rendering the widget grid
* positioning widgets according to their layout configuration
* enabling drag-and-drop positioning
* enabling widget resizing

Each widget's layout is defined using the following properties:

* `grid_x`
* `grid_y`
* `width`
* `height`
* `index`

These values determine the widget's position and size within the dashboard grid.

When users move or resize widgets, the grid component updates these values and stores them until the dashboard is saved.

---

# WidgetCard

`WidgetCard` represents the visual container for a widget inside the dashboard.

It provides the user interface for:

* widget title and header
* widget actions (filters, settings, removal)
* loading states
* layout boundaries

The card acts as a wrapper around the actual widget implementation.

---

# WidgetDispatcher

`WidgetDispatcher` dynamically resolves and loads the correct widget implementation.

Instead of hardcoding widget components, the dispatcher selects the correct component based on the widget configuration.

This mechanism allows the platform to support many different widget types without modifying the dashboard layout system.

In simplified terms:

```
widget.code → widget component
```

The dispatcher maps the widget identifier to the correct frontend component.

This design allows the platform to extend the widget system without changing the dashboard infrastructure.

---

# Widget Components

Each widget type is implemented as a dedicated Vue component.

Examples include:

* chart widgets
* tables
* analytical accounting widgets
* infrastructure monitoring widgets

Widget components are responsible for:

* retrieving their own data
* rendering visual elements
* managing internal filters
* handling widget-specific settings

Widgets may also expose configuration dialogs that allow users to customize their behavior.

---

# Widget Plugin Model

The dashboard system effectively implements a **plugin architecture**.

The dashboard layout system is independent of the widget implementations.

This separation allows new widgets to be added by:

1. registering a widget in the backend
2. creating the corresponding frontend component
3. connecting the widget code to the component in the widget dispatcher

Because the layout system remains unchanged, new widgets can be introduced without modifying the dashboard core.

This design ensures scalability and flexibility as the number of widgets grows.
