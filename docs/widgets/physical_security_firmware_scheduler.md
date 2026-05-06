# Firmware Updates Scheduler

The Firmware Updates Scheduler displays the full list of monitored security devices and their current firmware update status. It allows you to select one or more devices and schedule a firmware update maintenance window by creating a downtime entry.

---

## Reading the table

Each row in the table represents one monitored device. The table is sorted by branch code by default.

| Column | Description |
|---|---|
| Status | Firmware update status indicator: green (up to date), yellow (minor update available), red (major update pending) |
| Sede | Branch code (SOA/UOP) |
| Marca | Device brand |
| Modello | Device model |
| IP | Device IP address |
| Firmware | Currently installed firmware version |
| Nuovo Firmware | Latest available firmware version, color-coded by update urgency |
| Ultimo Aggiornamento | Timestamp of the last firmware status check |
| Aggiornamento Pianificato | Date of the already-scheduled maintenance window, if any |

![Firmware Updates Scheduler](../images/widgets/physical_security/firmware_scheduler.png)
/// caption
Fig.1 — Firmware Updates Scheduler — device list with update status and scheduled dates
///

---

## Scheduling a firmware update

1. Select one or more rows using the row checkboxes.
2. Click **Pianifica Aggiornamento** — the button appears in the table header once at least one row is selected.
3. The **Schedule Firmware Update** dialog opens.

### Choosing a date

The dialog presents two options:

- **Existing schedules** — if maintenance windows are already planned, each is shown as a toggle button displaying the date and the number of updates already scheduled on that date (e.g. *15/05/2026 — 12 scheduled updates*). Click a toggle to select that date.
- **Custom Date** — use the date picker to enter a different date. Only future dates (from tomorrow onwards) are selectable.

![Schedule Firmware Update dialog](../images/widgets/physical_security/firmware_scheduler_dialog.png)
/// caption
Fig.2 — Schedule Firmware Update dialog — existing schedules and custom date picker
///

4. Click **Confirm Schedule** to apply.

### What happens on confirmation

For each selected device:

- If the device has **no existing maintenance window**, a new downtime is created with code `PHY-MAINTENANCE-firmware-{timestamp}`.
- If the device already has **a scheduled maintenance window**, the existing downtime is updated with the new date.

The **Aggiornamento Pianificato** column in the table updates to reflect the new schedule.

!!! note
    Scheduling an update does not trigger the firmware update itself. The scheduled downtime is a planning record — the actual update operation is handled separately by automated processes that monitor the downtime calendar.

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
| Status | Firmware update status (severity selector) |

The first six filters are also exposed as **Global Filters** on the dashboard.

---

## Data export

Click the download icon to export an Excel file of the full device list. The exported columns are: Sede, Marca, Modello, Stato, IP, Firmware, Nuovo Firmware, Ultimo Aggiornamento, Aggiornamento Programmato. The filename includes a timestamp.
