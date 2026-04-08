# Downtimes

La sezione **Downtimes** consente di sospendere temporaneamente gli alert di monitoraggio per gli elementi infrastrutturali selezionati durante attività pianificate come manutenzioni, aggiornamenti o riconfigurazioni di rete.

!!! info
    Durante un downtime, la piattaforma **continua a raccogliere dati di monitoraggio** — vengono soppresse solo le notifiche di alert.
    Questo significa che puoi comunque consultare la cronologia delle metriche dopo la chiusura della finestra di manutenzione.

---

## Dove Gestire i Downtime

I downtime possono essere gestiti in due modi:

- **Dalla sezione Tracking** — per una vista centralizzata di tutti i downtime attivi e pianificati sull'infrastruttura.
- **Direttamente dalla gerarchia** — cliccando il pulsante di azione **Downtime** su qualsiasi elemento nella [Tree Hierarchy View](../tree_hierarchy_view.md) (gruppi, oggetti, metric type, metriche).

Entrambi i percorsi aprono lo stesso modal **Active Downtimes** per l'entità selezionata.

---

## Aprire la Sezione Downtimes

Dal menu di navigazione principale, vai su **Tracking → Downtimes**.

L'interfaccia si apre con un **dialog di pre-filter**. Compila uno o più campi per restringere la ricerca, poi clicca **APPLY**.

I campi filtro tipici includono:

| Campo filtro | Descrizione |
|---|---|
| Name | Nome della regola di downtime |
| Entity type | Tipo di entità a cui si applica il downtime (Group, Object, Metric Type, Metric) |
| Status | Active o Disabled |

![Downtimes pre-filter](../../images/tracking/downtimes/downtimes_prefilter.png)
/// caption
Fig.1 - Dialog di pre-filter Downtimes
///

---

## Tabella Downtimes

Dopo aver applicato il filtro, i risultati appaiono in una tabella dove ogni riga rappresenta un record di downtime.

![Downtimes table](../../images/tracking/downtimes/downtimes_table.png)
/// caption
Fig.2 - Tabella dei risultati Downtimes
///

---

## Creare un Downtime

Il modo più comune per creare un downtime è direttamente dalla gerarchia dell'infrastruttura:

1. Naviga all'entità che vuoi silenziare — un gruppo, oggetto, metric type o metrica — usando la [Tree Hierarchy View](../tree_hierarchy_view.md).
2. Clicca il pulsante di azione **Downtime** sulla riga target.
3. Nel modal **Active Downtimes**, clicca **NEW**.
4. Compila i dettagli del downtime (vedi campi di seguito).
5. Clicca **SAVE CHANGES**.

!!! note
    Applicare un downtime a un **gruppo** o **oggetto** silenzia gli alert per tutti gli elementi discendenti nella gerarchia. Usalo per sopprimere un'intera sezione dell'infrastruttura in una volta sola.

### Campi del Downtime

| Campo | Descrizione |
|---|---|
| Name | Nome della regola di downtime |
| Start | Data e ora di inizio del downtime |
| End | Data e ora di fine del downtime |
| Calendar | Calendario facoltativo per limitare il downtime a finestre temporali specifiche |
| Status | Active o Disabled |
| Notes | Note facoltative |

![Downtime edit dialog](../../images/tracking/downtimes/downtimes_crud.png)
/// caption
Fig.3 - Dialog di modifica downtime
///

---

## Casi d'Uso Tipici

| Scenario | Livello consigliato |
|---|---|
| Manutenzione server | Object |
| Aggiornamento dispositivo di rete | Object o Group |
| Interruzione pianificata a livello di sede | Group (livello superiore) |
| Anomalia singola metrica (rumore noto) | Metric o Metric Type |

---

## Downtime Massivo

Per applicare un downtime a più entità contemporaneamente, selezionale in qualsiasi gerarchia o vista tabella e usa **Massive Downtime**.

Questo crea una singola regola di downtime applicata a tutti gli elementi selezionati simultaneamente, risparmiando tempo durante grandi finestre di manutenzione.

---

!!! note
    Per controllare **quando** un downtime è attivo usando un programma temporale, associalo a un [Calendar](calendars.md).
    Per automatizzare le risposte operative quando scattano gli alert, consulta [Dispatchers](dispatchers.md).
