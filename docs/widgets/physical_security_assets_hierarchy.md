# Assets Hierarchy

The Assets Hierarchy widget presents all physical branches (*asset immobiliari*) as a navigable list. Each branch entry shows a severity indicator derived from the firmware update status of the security devices it contains, and expands to reveal the device groups associated with that site.

The widget is designed to work in conjunction with the **Asset Map**: selecting a branch in the hierarchy automatically focuses the map on that location.

---

## Reading the list

Each row represents a branch, identified by its **SOA/UOP code** and description. The colored severity indicator reflects the most critical firmware update status among the devices at that branch:

| Color | Meaning |
|---|---|
| Green | All devices are up to date |
| Yellow | At least one device has a recommended update available |
| Red | At least one device has a critical update pending |
| Grey | No firmware status data available |

![Assets Hierarchy list](../images/widgets/physical_security/assets_hierarchy.png)
/// caption
Fig.1 — Assets Hierarchy — branch list with severity indicators
///

---

## Navigating a branch

Click a branch row to select it. The view expands to show the **device groups** associated with that site (e.g. security cameras, ATMs, control units). Selecting a group displays the individual devices it contains.

When a branch is selected, the **Asset Map** widget simultaneously zooms to center on that location.

![Branch detail](../images/widgets/physical_security/assets_hierarchy_detail.png)
/// caption
Fig.2 — Branch detail — device groups and individual device list
///

---

## ATM devices

When the **ATM** device group is selected, a **Show ATMs** toggle appears. Activating it overlays the ATM positions on the Asset Map for the selected branch — including ATMs located outside the branch premises (e.g. in external locations such as supermarkets).

---

## Device detail — Report Ciclo di Vita

Click an individual device to open the **Report Ciclo di Vita** dialog.

The dialog displays the full device record:

| Field | Description |
|---|---|
| Codice Filiale | Branch code |
| Descrizione Filiale | Branch name |
| Marca | Device brand |
| Modello | Device model |
| Codice Seriale | Serial number |
| Indirizzo IP | IP address |
| Stato | Current firmware update status |
| Versione Firmware | Currently installed firmware version |
| Data Attivazione | Device activation date |
| Ultima Rilevazione | Timestamp of the last status check |

Below the device details, the **Tabella Attività** lists past maintenance operations with date, description, status, period, and notes.

The **Dismissione Securizzata** button initiates the secure disposal procedure for the selected device.

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

All filters are also exposed as **Global Filters** on the dashboard and are shared with the Asset Map widget.

---

## Data export

Click the download icon to export an Excel file for the currently selected branch. The file contains one sheet per device group, with the full data record for each device. The filename includes the branch code and a timestamp.
