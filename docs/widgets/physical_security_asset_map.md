# Asset Map

The Asset Map widget displays all physical branches on an interactive geographic map. Each branch is represented by a color-coded marker that reflects the firmware update status of the security devices at that location.

The widget is designed to work in conjunction with the **Assets Hierarchy**: selecting a branch in the hierarchy list automatically centers and zooms the map on that site.

---

## Reading the map

Each marker on the map represents one branch. The marker color matches the site's overall severity:

| Color | Meaning |
|---|---|
| Green | All devices are up to date |
| Yellow | At least one device has a recommended update available |
| Red | At least one device has a critical update pending |
| Grey | No firmware status data available |

When multiple nearby branches are grouped into a cluster, the cluster marker takes the color of the most critical status among the grouped sites.

![Asset Map](../images/widgets/physical_security/asset_map.png)
/// caption
Fig.1 — Asset Map — geographic distribution of branches with severity-colored markers
///

---

## Interacting with the map

- **Zoom in / zoom out** — use the map controls or scroll to navigate.
- **Click a cluster** — expands the cluster to show the individual branch markers.
- **Click a branch marker** — opens a summary panel for that branch.

---

## Synchronisation with Assets Hierarchy

When the **Assets Hierarchy** widget is on the same dashboard, selecting a branch in the list triggers the map to focus on and zoom into that specific branch. This link works in one direction: the hierarchy drives the map focus, not the other way around.

When the **Show ATMs** toggle is activated in the Assets Hierarchy, the map also overlays the ATM positions for the selected branch — displayed as distinct markers separate from the main branch marker.

---

## Filters

| Filter | Description |
|---|---|
| Codice SOA/UOP | Branch code |
| Indirizzo | Branch address |
| Comune | City |
| Provincia | Province (autocomplete) |
| Regione | Region (select) |
| Polo | Virtual domain / polo (select) |

All filters are also exposed as **Global Filters** on the dashboard and are shared with the Assets Hierarchy widget.

!!! note
    Because both widgets share the same set of global filters, any filter applied from the dashboard Global Filters panel affects both the map and the hierarchy list simultaneously.
