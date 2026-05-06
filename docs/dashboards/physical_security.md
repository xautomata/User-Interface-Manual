# Physical Security Dashboards

The Physical Security dashboards are a set of three dedicated dashboards for monitoring the security device infrastructure. They display the firmware update status of physical security devices — cameras, DVRs, sensors, ATMs, and control units — distributed across the branch network.

All three dashboards support **Global Filters**, allowing you to restrict the displayed data to a specific region, province, city, branch code, or organisational unit (Polo) in a single operation across all widgets simultaneously. See [Global Filters](global_filters.md) for details on how they work.

---

## Physical Security — Capacity Management

This dashboard provides a statistical overview of the firmware update status across the entire device fleet.

It contains four chart widgets, each grouping the same device dataset by a different dimension:

- **Asset Physical Security per Stato** — distribution by update status (up to date / minor update / major update)
- **Asset Physical Security per Tipo** — count by device type
- **Asset Physical Security per Modello** — count by device model
- **Asset Physical Security per Firmware** — count by installed firmware version

Clicking any chart element opens the **Asset Physical Security Drilldown Analyzer**, which lets you inspect the individual devices behind a data point and switch between chart views within the same dialog.

→ See [Physical Security — Capacity Management](../widgets/physical_security_capacity_management.md) for full widget documentation.

---

## Physical Security — Dashboard Service

This dashboard gives a geographic and hierarchical view of the branch network and its associated devices.

It contains two tightly coupled widgets:

- **Assets Hierarchy** — a navigable list of branches, expandable to show device groups and individual assets
- **Asset Map** — an interactive map showing the geographic position of each branch

Selecting a branch in the Assets Hierarchy automatically focuses the Asset Map on that location. When the ATM device group is selected within a branch, the map can also display the positions of ATMs associated with that site.

Both widgets share the same set of Global Filters (branch code, address, city, province, region, Polo), so applying a filter from the dashboard panel narrows both views simultaneously.

→ See [Assets Hierarchy](../widgets/physical_security_assets_hierarchy.md) and [Asset Map](../widgets/physical_security_asset_map.md) for full widget documentation.

---

## Physical Security — Dashboard Dispositivo

This dashboard is the operational tool for managing firmware update scheduling across the device fleet.

It contains one widget:

- **Firmware Updates Scheduler** — a table listing all monitored devices with their current firmware status and any already-scheduled maintenance window

From this dashboard you can select devices and schedule a firmware update maintenance window. The scheduling creates or updates a downtime entry for each selected device, which is then picked up by the automated update processes.

→ See [Firmware Updates Scheduler](../widgets/physical_security_firmware_scheduler.md) for full widget documentation.
