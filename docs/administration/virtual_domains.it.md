# Virtual Domains

La sezione **Virtual Domains** gestisce le partizioni logiche utilizzate per organizzare utenti, gruppi e probe all'interno di XAUTOMATA.
I virtual domain fungono da confini amministrativi — utili in deployment multi-cliente o multi-ambiente dove diversi scope devono essere chiaramente separati.

---

## Aprire la Sezione Virtual Domains

Dal menu di navigazione principale, vai su **Administration → Virtual Domains**.

A differenza della maggior parte delle sezioni, Virtual Domains si apre **direttamente in una vista tabella** — non è presente un dialog di pre-filter.
Usa i controlli di ricerca nell'intestazione della tabella per filtrare i record direttamente.

![Virtual Domains table](../images/administration/virtual_domains/virtual_domains_table.png)
/// caption
Fig.1 - Tabella Virtual Domains
///

---

## Dettagli del Virtual Domain

Clicca sull'**icona di ricerca (🔍)** su qualsiasi riga per aprire il record del virtual domain.

| Campo | Descrizione |
|---|---|
| Code | Identificatore univoco del virtual domain |
| Description | Nome descrittivo o etichetta |

Da questo dialog puoi:

- modificare il virtual domain
- duplicare il record
- eliminare il record

---

## Connections View

Clicca sull'**icona link (🔗)** su qualsiasi riga per aprire la **Connections View**.

Questa è la principale vista operativa per i virtual domain. Mostra le entità associate al dominio selezionato:

| Tab | Descrizione |
|---|---|
| Users | Account utente appartenenti a questo virtual domain |
| Groups | Gruppi infrastrutturali in scope per questo virtual domain |
| Probes | Probe di monitoraggio associate a questo virtual domain |

### Tab Users

Mostra tutti gli utenti collegati al virtual domain. Le colonne includono User, Email, Phone, Status.

### Tab Groups

Mostra i gruppi infrastrutturali associati al virtual domain. Le colonne includono Name, Description, Type, Site, Status.

### Tab Probes

Mostra le probe di monitoraggio associate al virtual domain. Le colonne includono Severity, Name, Probe Type, Object, Status.

![Virtual Domain connections view](../images/administration/virtual_domains/virtual_domains_connections.png)
/// caption
Fig.2 - Connections view del Virtual Domain
///

---

!!! note
    I virtual domain sono contenitori leggeri. Il loro valore risiede nelle relazioni che contengono — gli utenti, i gruppi e le probe ad essi associati.
    Per gestire gli account utente, consulta [Users](users.md). Per gestire gli agenti di monitoraggio, consulta [Probes](probes.md).
