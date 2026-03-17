# Customers

The **Customers** section lists the organizations monitored and managed through XAUTOMATA.
Each customer is the root of the operational structure that groups sites, contacts, and infrastructure objects.

!!! info
    Customers are provisioned during onboarding by the XAUTOMATA delivery team.
    This section is primarily used for consultation — you will not normally create or delete customer records from the interface.

---

## Opening the Customers Section

From the main navigation menu, go to **Customers → Client Repository → Customers**.

The interface opens directly with the **results table**, without a pre-filter step.

![Customers table](../images/data_manager/customers/customers_table.png)
/// caption
Fig.1 - Customers table (screenshot pending)
///

Each row represents a customer. Use the search bar at the top of the table to filter records by name or code.

---

## Customer Details

Click the **search icon (🔍)** on any row to open the customer record.

The detail view shows the main information associated with the customer:

| Field | Description |
|---|---|
| Code | Unique identifier of the customer |
| Description | Full name or label of the organization |
| Status | Active or Disabled |

![Customer detail dialog](../images/data_manager/customers/customers_crud.png)
/// caption
Fig.2 - Customer detail dialog (screenshot pending)
///

---

## Customer Structure View

Click the **link icon (🔗)** on a customer row to open the **Customer Structure View**.

This is the main operational view for a customer. The page is divided into two areas:

- a **customer information panel** on the left
- a **hierarchical navigation area** on the right

The hierarchical area has two tabs.

### Sites tab

Displays the infrastructure hierarchy under the customer, organized by site.

The structure descends through:

1. Sites
2. Groups
3. Objects
4. Metric Types
5. Metrics

Use this tab to navigate the monitored infrastructure associated with the customer.

For a detailed explanation of how to navigate this view, see [Tree Hierarchy View](../tree_hierarchy_view.md).

![Customer structure — Sites tab](../images/data_manager/customers/customers_structure_sites.png)
/// caption
Fig.3 - Customer structure view, Sites tab (screenshot pending)
///

### Service Profiles tab

Displays the hierarchy of services and service profiles associated with the customer.

Use this tab to navigate the logical service organization.

---

## Connections View

From the Customer Structure View, click **Connections** to switch to the **Connections View**.

This view shows the entities linked to the customer:

| Tab | Description |
|---|---|
| Contacts | People associated with this customer |
| Users | Platform users who have access to this customer |
| Dashboards | Dashboards associated with this customer |
| Services | Services monitored under this customer |
| Sites | Sites belonging to this customer |

Use this view to verify which users and dashboards are associated with the customer, or to link new entities.

![Customer connections view](../images/data_manager/customers/customers_connections.png)
/// caption
Fig.4 - Customer connections view (screenshot pending)
///

---

!!! note
    To manage the people associated with a customer, see [Contacts](contacts.md).
    To manage physical or logical locations, see [Sites](sites.md).
