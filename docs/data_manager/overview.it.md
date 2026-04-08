# Panoramica del Data Manager

Il **Data Manager** è l'area di configurazione della piattaforma.
Qui definisci e gestisci tutte le entità che rappresentano l'ambiente monitorato — organizzazioni, risorse infrastrutturali, servizi e metriche.

Tutto ciò che viene visualizzato nei dashboard e nei widget ha origine dai dati configurati in questa sezione.

---

## Come è Organizzato

Il Data Manager è accessibile dalla **left sidebar** sotto la sezione **Customers**.
È suddiviso in due repository e un'area di tracking:

| Area | Contenuto | Scopo |
|---|---|---|
| **Client Repository** | Customers, Sites, Contacts | Struttura organizzativa degli ambienti monitorati |
| **Objects Repository** | Groups, Objects, Metric Types, Metrics, Services | Infrastruttura tecnica e dati di monitoraggio |
| **Tracking** | Calendars, Downtimes, Dispatchers | Gestione degli eventi operativi |

---

## Client Repository

Il Client Repository contiene le informazioni organizzative utilizzate per associare l'infrastruttura a entità reali.

- **Customers** — le organizzazioni monitorate dalla piattaforma
- **Sites** — le sedi fisiche o logiche dell'infrastruttura
- **Contacts** — le persone associate ai clienti e alle sedi

Consulta [Customers](customers/customers.md), [Sites](customers/sites.md), [Contacts](customers/contacts.md).

---

## Objects Repository

L'Objects Repository descrive l'infrastruttura tecnica monitorata.

- **Groups** — contenitori logici che organizzano gli oggetti per sede e dominio operativo
- **Objects** — le singole risorse monitorate (server, dispositivi, applicazioni)
- **Metric Types** — le definizioni di cosa viene misurato su ciascun oggetto
- **Metrics** — i dati effettivi di serie temporali raccolti dagli oggetti
- **Services** — aggregazioni logiche di livello superiore dei dati di monitoraggio

Consulta [Groups](objects/groups.md), [Objects](objects/objects.md), [Metric Types](objects/metric_types.md), [Metrics](objects/metrics.md), [Services](objects/services.md).

---

## Tracking

L'area Tracking fornisce strumenti per gestire gli eventi operativi che influenzano il comportamento del monitoraggio.

- **Calendars** — definisce i programmi temporali utilizzati da downtimes e dispatcher
- **Downtimes** — sospende temporaneamente gli alert durante le finestre di manutenzione
- **Dispatchers** — configura le azioni automatiche attivate dagli eventi di monitoraggio

Consulta [Calendars](monitoring/calendars.md), [Downtimes](monitoring/downtimes.md), [Dispatchers](monitoring/dispatchers.md).

---

## Modello di Interazione Comune

Tutte le sezioni entità nel Data Manager seguono lo stesso schema di interazione: pre-filter → tabella dei risultati → dialog CRUD → vista Connections.

Se sei nuovo sulla piattaforma, leggi [Working with Entities](working_with_entities.md) prima di esplorare le singole sezioni — renderà ogni sezione immediatamente familiare.

Per le entità con struttura gerarchica (Customers, Groups, Objects), la [Tree Hierarchy View](tree_hierarchy_view.md) ti consente di navigare da un'entità radice fino alle singole metriche in un'unica vista espandibile.
