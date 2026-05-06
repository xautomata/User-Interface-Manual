# Dashboard Physical Security

Le dashboard Physical Security sono un insieme di tre dashboard dedicate al monitoraggio dell'infrastruttura dei dispositivi di sicurezza. Mostrano lo stato degli aggiornamenti firmware dei dispositivi di sicurezza fisica — telecamere, DVR, sensori, ATM e centraline — distribuiti nella rete di filiali.

Tutte e tre le dashboard supportano i **Global Filters**, che permettono di restringere i dati visualizzati a una specifica regione, provincia, città, codice filiale o unità organizzativa (Polo) in un'unica operazione su tutti i widget contemporaneamente. Consulta [Global Filters](global_filters.md) per i dettagli sul loro funzionamento.

---

## Physical Security — Capacity Management

Questa dashboard offre una panoramica statistica dello stato degli aggiornamenti firmware sull'intera flotta di dispositivi.

Contiene quattro widget grafici, ciascuno dei quali raggruppa lo stesso dataset di dispositivi secondo una dimensione diversa:

- **Asset Physical Security per Stato** — distribuzione per stato dell'aggiornamento (aggiornato / aggiornamento minore / aggiornamento maggiore)
- **Asset Physical Security per Tipo** — conteggio per tipo di dispositivo
- **Asset Physical Security per Modello** — conteggio per modello di dispositivo
- **Asset Physical Security per Firmware** — conteggio per versione firmware installata

Cliccando su qualsiasi elemento di un grafico si apre l'**Asset Physical Security Drilldown Analyzer**, che permette di esaminare i singoli dispositivi dietro un dato e passare tra le viste grafiche all'interno della stessa dialog.

→ Consulta [Physical Security — Capacity Management](../widgets/physical_security_capacity_management.md) per la documentazione completa dei widget.

---

## Physical Security — Dashboard Service

Questa dashboard offre una vista geografica e gerarchica della rete di filiali e dei dispositivi associati.

Contiene due widget strettamente integrati:

- **Assets Hierarchy** — un elenco navigabile di filiali, espandibile per mostrare i gruppi di dispositivi e i singoli asset
- **Asset Map** — una mappa interattiva che mostra la posizione geografica di ogni filiale

Selezionando una filiale nell'Assets Hierarchy, l'Asset Map si centra automaticamente su quella posizione. Quando è selezionato il gruppo di dispositivi ATM all'interno di una filiale, la mappa può mostrare anche le posizioni degli ATM associati a quel sito.

Entrambi i widget condividono lo stesso insieme di Global Filters (codice filiale, indirizzo, comune, provincia, regione, Polo): applicare un filtro dal pannello della dashboard restringe contemporaneamente entrambe le viste.

→ Consulta [Assets Hierarchy](../widgets/physical_security_assets_hierarchy.md) e [Asset Map](../widgets/physical_security_asset_map.md) per la documentazione completa dei widget.

---

## Physical Security — Dashboard Dispositivo

Questa dashboard è lo strumento operativo per la gestione della pianificazione degli aggiornamenti firmware sull'intera flotta di dispositivi.

Contiene un widget:

- **Firmware Updates Scheduler** — una tabella che elenca tutti i dispositivi monitorati con il loro stato firmware attuale e l'eventuale finestra di manutenzione già pianificata

Da questa dashboard puoi selezionare i dispositivi e pianificare una finestra di manutenzione per l'aggiornamento firmware. La pianificazione crea o aggiorna una voce di downtime per ogni dispositivo selezionato, che viene poi gestita dai processi automatizzati di aggiornamento.

→ Consulta [Firmware Updates Scheduler](../widgets/physical_security_firmware_scheduler.md) per la documentazione completa del widget.
