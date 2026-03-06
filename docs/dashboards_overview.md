# Dashboard Overview

Dashboards provide visual access to the operational and analytical data managed by XAUTOMATA.

Each dashboard is composed of multiple **widgets**, arranged in a configurable layout.  
Widgets retrieve data from the platform and display it using charts, tables, grids, or custom visual components.

## Dashboard Structure

A dashboard is made up of:

- a name and description
- a scope and type
- a refresh interval
- a set of widget associations

Each widget in the dashboard has its own:

- position
- size
- order
- settings

This allows dashboards to be configured to match different operational needs.

## Dashboard Filters

Dashboards may provide shared filters that affect multiple widgets at the same time.

Typical examples include:

- customer
- date range
- reference month
- operational scope

Widgets can also define their own local filters and selectors, depending on their configuration.

## Widgets in Dashboards

Widgets are the main building blocks of dashboards.

A widget can display data using different visual formats, such as:

- charts
- tables
- maps
- custom views

Each widget is configured to retrieve its own data and render it according to its specific purpose.

## Typical Dashboard Usage

Dashboards are typically used to:

- monitor infrastructure and service status
- analyze trends and time series
- investigate anomalies
- review network and cloud cost metrics
- export data for further analysis

## Main Dashboard Domains

The platform currently includes dashboards for different operational domains, including:

- IT Infrastructure
- Network
- Cloud Cost

Each dashboard groups together widgets relevant to the same functional area.

## Relationship with the Data Manager

Dashboards depend on the data configured in the **Data Manager**.

For example:

- metrics and services feed infrastructure dashboards
- cost registrations feed cloud cost dashboards
- cost views enrich analytical accounting widgets

Without the underlying entity configuration, dashboards would not have meaningful data to display.