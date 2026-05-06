# Physical Security — Capacity Management

The four Capacity Management widgets display the firmware update status of all physical security devices monitored on the platform. Each widget groups the same dataset by a different dimension — update status, device type, model, or firmware version — providing complementary views of the same information.

Clicking any chart element opens the **Asset Physical Security Drilldown Analyzer**, a shared detail dialog that lets you inspect the underlying devices and switch between groupings without leaving the dialog.

---

## Asset Physical Security per Stato

Displays the distribution of devices by firmware update status as a donut chart.

| Status | Meaning |
|---|---|
| Green | Firmware is up to date — no action required |
| Yellow | A minor update is available — update recommended |
| Red | A major update is available — update strongly recommended |

Click a segment to open the Drilldown Analyzer filtered by that status.

![Asset Physical Security per Stato](../images/widgets/physical_security/fmw_by_status.png)
/// caption
Fig.1 — Asset Physical Security per Stato — device distribution by firmware update status
///

---

## Asset Physical Security per Tipo

Displays device counts grouped by **device type** (e.g. DVR, centrali, telecamere) as a treemap. Each tile is proportional to the number of devices of that type.

Click a tile to open the Drilldown Analyzer filtered by that device type.

![Asset Physical Security per Tipo](../images/widgets/physical_security/fmw_by_type.png)
/// caption
Fig.2 — Asset Physical Security per Tipo — device count by type
///

---

## Asset Physical Security per Modello

Displays device counts grouped by **device model** as a treemap. Each tile is proportional to the number of devices of that model.

Click a tile to open the Drilldown Analyzer filtered by that model.

![Asset Physical Security per Modello](../images/widgets/physical_security/fmw_by_model.png)
/// caption
Fig.3 — Asset Physical Security per Modello — device count by model
///

---

## Asset Physical Security per Firmware

Displays device counts grouped by **installed firmware version** as a donut chart.

Click a segment to open the Drilldown Analyzer filtered by that firmware version.

![Asset Physical Security per Firmware](../images/widgets/physical_security/fmw_by_firmware.png)
/// caption
Fig.4 — Asset Physical Security per Firmware — device count by firmware version
///

---

## Drilldown Analyzer

Clicking any element on any of the four charts opens the **Asset Physical Security Drilldown Analyzer** dialog.

The dialog shows a table of the individual devices matching the selected filter:

| Column | Description |
|---|---|
| Status | Firmware update status indicator (green / yellow / red) |
| Firmware | Firmware version currently installed on the device |
| Type | Device type |
| Model | Device model |

A **chart switcher** at the top of the dialog lets you view any of the four groupings — by Stato, Tipo, Modello, or Firmware — without closing the dialog. Clicking a different segment or tile in the embedded chart updates the device table accordingly.

![Drilldown Analyzer](../images/widgets/physical_security/drilldown_analyzer.png)
/// caption
Fig.5 — Asset Physical Security Drilldown Analyzer — device table with chart switcher
///

---

## Data export

All four widgets support data download. Click the download icon to export an Excel file with the grouped data (label and count) for that widget.
