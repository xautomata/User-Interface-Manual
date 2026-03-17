# Objects

The **Objects** section manages the individual resources monitored by XAUTOMATA, such as servers, virtual machines, network devices, and applications.
Objects are the central monitoring entities of the platform — metrics are collected from them, alerts are raised on them, and automation rules act on them.

---

## Opening the Objects Section

From the main navigation menu, go to **Customers → Objects Repository → Objects**.

The interface opens with a **pre-filter dialog**. Fill in one or more fields to narrow the search, then click **APPLY**.

| Filter field | Description |
|---|---|
| Name | Name of the object |
| Description | Optional description |
| IP Address | IP address of the monitored resource |
| Profile | Object classification (see [Object Profiles](#object-profiles) below) |
| Status | Active, Disabled, or Maintenance |

By default, the pre-filter is set to show only **active** objects. Leave other fields empty and click **APPLY** to load all active objects.

![Objects pre-filter](../images/data_manager/objects/objects_prefilter.png)
/// caption
Fig.1 - Objects pre-filter dialog (screenshot pending)
///

---

## Objects Table

After applying the filter, the results appear in a table where each row represents a monitored resource.

Typical columns include:

- Name
- Description
- IP Address
- Profile
- Status

![Objects table](../images/data_manager/objects/objects_table.png)
/// caption
Fig.2 - Objects results table (screenshot pending)
///

---

## Object Profiles

Each object is classified by a **Profile** that identifies the type of infrastructure resource it represents:

| Profile | Description |
|---|---|
| Host | Physical or virtual server |
| Virtual Machine | VM managed by a hypervisor |
| Cluster | Group of nodes managed as a single resource |
| Virtual Center | Virtualization management platform |
| Resource Pool | Logical resource allocation unit |
| IT Managed Services | Generic managed service resource |
| WAN Network | Network device or WAN component |
| Cost Management | Resource used for cost tracking |
| Process Flow | Process or workflow component |
| Real Estate / Physical Security | Facility or physical security asset |

The profile determines how the object fits into the monitoring model and which types of metrics and automation rules may apply.

---

## Object Details

Click the **search icon (🔍)** on any row to open the object record.

The CRUD dialog displays the full configuration of the object:

| Field | Description |
|---|---|
| Name | Name of the monitored resource |
| Description | Optional description |
| IP Address | Network address of the resource |
| Profile | Object classification |
| Data Profile | JSON configuration for the object |
| Automata Domain | Automation scope |
| Status | Active, Disabled, or Maintenance |
| Feedback for Operator | Notes or guidance for the operator |

From this dialog you can:

- edit the object configuration
- duplicate the record
- delete the record

!!! note
    Set **Status** to **Maintenance** when the resource is undergoing planned work.
    This suspends alerts without fully disabling the object.

![Object detail dialog](../images/data_manager/objects/objects_crud.png)
/// caption
Fig.3 - Object detail dialog (screenshot pending)
///

---

## Object Structure View

Click the **link icon (🔗)** on any row to open the **Object Structure View**.

The page is divided into two areas:

- an **object information panel** on the left
- a **hierarchical navigation area** on the right

The hierarchy displays the monitoring entities associated with the object:

1. Metric Types
2. Metrics

Use this view to inspect the monitoring data collected from the object and to apply operational actions at any level of the hierarchy.

For a detailed explanation of how to use this view, see [Tree Hierarchy View](../tree_hierarchy_view.md).

![Object structure view](../images/data_manager/objects/objects_structure.png)
/// caption
Fig.4 - Object structure view (screenshot pending)
///

### Operational actions

From the hierarchy view you can apply the following actions to any element in the tree:

| Action | Description |
|---|---|
| Metric Data | Open the historical chart or table for the selected metric |
| Downtime | Temporarily suspend monitoring alerts for the selected element |
| Dispatcher | Configure an automated response triggered by a monitoring event |

Objects also support **mass operations** — select multiple elements and apply a single action to all of them at once:

- **Massive Downtime**
- **Massive Dispatcher**

---

## Connections View

From the Object Structure View, click **Connections** to switch to the **Connections View**.

This view shows the entities linked to the object:

| Tab | Description |
|---|---|
| Groups | Groups this object belongs to |
| Probes | Monitoring agents collecting data from this object |
| Metric Types | Measurement definitions associated with this object |
| Downtimes | Active maintenance windows for this object |
| Dispatchers | Active automation rules linked to this object |

![Object connections view](../images/data_manager/objects/objects_connections.png)
/// caption
Fig.5 - Object connections view (screenshot pending)
///

---

!!! note
    To manage the measurements collected from an object, see [Metric Types](metric_types.md) and [Metrics](metrics.md).
    To manage the monitoring agents associated with an object, see [Probes](../administration/probes.md).
