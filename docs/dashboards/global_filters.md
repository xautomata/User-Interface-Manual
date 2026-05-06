# Global Filters

Global Filters let you apply a single filter simultaneously to all compatible widgets on a dashboard, without having to configure each widget separately.

---

## How Global Filters work

Every widget can expose one or more of its filters as **global**. This is defined in the widget's configuration.

When a dashboard loads, it scans all the widgets it contains, collects every filter marked as global, and presents them in a unified **Global Filters** panel — accessible from the dashboard action bar.

The list of available global filters therefore depends on which widgets are present on the dashboard: adding or removing a widget may change the filters available in the panel.

---

## Applying a Global Filter

Open the **Global Filters** panel from the dashboard action bar and set the desired values.

When you apply a global filter:

- It is applied **only to widgets that support that filter** — widgets that do not recognise the filter are unaffected.
- The corresponding individual filter inside each affected widget is **locked**: it cannot be changed at the widget level as long as the global filter is active. A message in the widget's filter panel indicates that the filter is under global control.

This means that two widgets on the same dashboard may share a common global filter (e.g. a region or site selector) while each widget may still have its own additional individual filters for more specific data scoping.

---

## Combining Global and individual filters

Global filters and individual widget filters can coexist:

1. Set a global filter to narrow the scope for the whole dashboard (e.g. show only data for *Lombardia*).
2. Open a single widget's filter panel to add further refinements on top of the global scope (e.g. show only devices in *Warning* state within that region).

Filters already controlled by the Global Filter panel are greyed out in the individual widget panel and cannot be overridden there.

---

## Example

A dashboard contains three widgets, each exposing a **Region** filter as global.

| Action | Result |
|---|---|
| Set **Region = Lombardia** in the Global Filters panel | All three widgets refresh and show only data for Lombardia |
| Open widget A's individual filter panel | **Region** filter is locked — controlled by the global panel |
| Add a **Status = Warning** filter to widget A | Widget A now shows only Warning-state items in Lombardia; widgets B and C are unchanged |
| Remove the global Region filter | All three widgets return to their default (unfiltered) scope; Region becomes editable again in each widget |
