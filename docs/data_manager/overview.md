# Data Manager Overview

The **Data Manager** is the configuration area of the platform.
Here you define and manage all the entities that represent the monitored environment — organizations, infrastructure resources, services, and metrics.

Everything displayed in dashboards and widgets originates from the data configured in this section.

---

## How it is organized

The Data Manager is accessible from the **left sidebar** under the **Customers** section.
It is divided into two repositories and a tracking area:

| Area | Contents | Purpose |
|---|---|---|
| **Client Repository** | Customers, Sites, Contacts | Organizational structure of monitored environments |
| **Objects Repository** | Groups, Objects, Metric Types, Metrics, Services | Technical infrastructure and monitoring data |
| **Tracking** | Calendars, Downtimes, Dispatchers | Operational event management |

---

## Client Repository

The Client Repository holds the organizational information used to associate infrastructure with real-world entities.

- **Customers** — the organizations monitored by the platform
- **Sites** — physical or logical locations of the infrastructure
- **Contacts** — people associated with customers and sites

See [Customers](customers/customers.md), [Sites](customers/sites.md), [Contacts](customers/contacts.md).

---

## Objects Repository

The Objects Repository describes the technical infrastructure being monitored.

- **Groups** — logical containers that organize objects by site and operational domain
- **Objects** — individual monitored resources (servers, devices, applications)
- **Metric Types** — definitions of what is measured on each object
- **Metrics** — the actual time-series data collected from objects
- **Services** — higher-level logical aggregations of monitoring data

See [Groups](objects/groups.md), [Objects](objects/objects.md), [Metric Types](objects/metric_types.md), [Metrics](objects/metrics.md), [Services](objects/services.md).

---

## Tracking

The Tracking area provides tools to manage operational events that affect monitoring behavior.

- **Calendars** — define time schedules used by downtimes and dispatchers
- **Downtimes** — temporarily suppress alerts during maintenance windows
- **Dispatchers** — configure automated actions triggered by monitoring events

See [Calendars](../tracking/calendars.md), [Downtimes](../tracking/downtimes.md), [Dispatchers](../tracking/dispatchers.md).

---

## Common interaction model

All entity sections in the Data Manager follow the same interaction pattern: pre-filter → results table → CRUD dialog → Connections view.

If you are new to the platform, read [Working with Entities](working_with_entities.md) before exploring individual sections — it will make every section immediately familiar.

For entities that have a hierarchical structure (Customers, Groups, Objects), the [Tree Hierarchy View](tree_hierarchy_view.md) lets you navigate from a root entity down to individual metrics in a single expandable view.
