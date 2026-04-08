# Dashboards

La sezione **Dashboards** in Super Admin gestisce le definizioni di dashboard disponibili su tutta la piattaforma.
Usa questa sezione per creare, configurare e organizzare le dashboard — definendo tipo, scope, layout e associazioni con i widget.

!!! warning
    Questa sezione è riservata agli utenti **Super Admin**. Le modifiche qui influenzano le dashboard visibili a tutti gli utenti della piattaforma.

---

## Aprire la Sezione

Dal menu di navigazione principale, vai su **Administration → Super Admin → Dashboards**.

L'interfaccia si apre con una tabella che elenca tutte le definizioni di dashboard.

| Colonna | Descrizione |
|---|---|
| Name | Nome della dashboard |
| Description | Descrizione facoltativa |
| Type | Global o Personal |
| Scope | Customers o Virtual Domains |
| User | Utente associato (per le dashboard Personal) |
| Order | Priorità di ordinamento nell'interfaccia |
| Refresh Interval | Intervallo di aggiornamento automatico in millisecondi |

---

## Dettagli della Dashboard

Clicca sull'**icona di ricerca (🔍)** su qualsiasi riga per aprire il record della dashboard.

| Campo | Descrizione |
|---|---|
| Name | Nome visualizzato della dashboard |
| Description | Descrizione facoltativa |
| Type | Global o Personal |
| Scope | Customers o Virtual Domains |
| User | Utente associato (solo per dashboard Personal) |
| Order | Priorità di ordinamento |
| Refresh Interval (ms) | Con quale frequenza la dashboard si aggiorna automaticamente |
| Thumbnail | Riferimento immagine facoltativo per la scheda della dashboard |

### Tipi di Dashboard

| Tipo | Descrizione |
|---|---|
| **Global** | Dashboard condiviso disponibile per più utenti e contesti |
| **Personal** | Dashboard associato a un account utente specifico |

### Scope della Dashboard

| Scope | Descrizione |
|---|---|
| **Customers** | La dashboard è disponibile nei contesti cliente |
| **Virtual Domains** | La dashboard è disponibile nei contesti virtual domain |

---

## Connections View

Clicca sull'**icona link (🔗)** su qualsiasi riga per aprire la Connections View.

| Tab | Descrizione |
|---|---|
| Widgets | Widget presenti in questa dashboard, con proprietà di layout |
| Users | Utenti che hanno accesso a questa dashboard |
| Customers | Clienti a cui questa dashboard è associata |

### Tab Widgets

Questa è la relazione più importante per una dashboard. Ogni associazione di widget memorizza non solo quale widget è incluso, ma anche la sua **posizione e dimensione** nella griglia della dashboard:

| Proprietà | Descrizione |
|---|---|
| Index | Ordinamento del widget all'interno della dashboard |
| Width | Larghezza in unità della griglia |
| Height | Altezza in unità della griglia |
| Grid X | Posizione orizzontale |
| Grid Y | Posizione verticale |
| Settings | Payload di configurazione specifico del widget |

### Tab Users

Mostra gli utenti che hanno accesso a questa dashboard. Usa questa tab per concedere o revocare l'accesso alla dashboard per utenti specifici.

### Tab Customers

Mostra i clienti a cui questa dashboard è associata. Rilevante per le dashboard visualizzate in contesti specifici del cliente.

---

!!! note
    Il layout della dashboard e la configurazione dei widget possono essere gestiti anche in modo interattivo dall'interfaccia della dashboard stessa.
    Consulta [Dashboard Management](../dashboards/management.md) per il flusso dell'utente finale.
