# Dashboards

La sezione **Dashboards** in Super Admin gestisce le definizioni di dashboard disponibili su tutta la piattaforma.
Usa questa sezione per creare, configurare e organizzare i dashboard — definendo tipo, scope, layout e associazioni con i widget.

!!! warning
    Questa sezione è riservata agli utenti **Super Admin**. Le modifiche qui influenzano i dashboard visibili a tutti gli utenti della piattaforma.

---

## Aprire la Sezione

Dal menu di navigazione principale, vai su **Administration → Super Admin → Dashboards**.

L'interfaccia si apre con una tabella che elenca tutte le definizioni di dashboard.

| Colonna | Descrizione |
|---|---|
| Name | Nome del dashboard |
| Description | Descrizione facoltativa |
| Type | Global o Personal |
| Scope | Customers o Virtual Domains |
| User | Utente associato (per i dashboard Personal) |
| Order | Priorità di ordinamento nell'interfaccia |
| Refresh Interval | Intervallo di aggiornamento automatico in millisecondi |

---

## Dettagli del Dashboard

Clicca sull'**icona di ricerca (🔍)** su qualsiasi riga per aprire il record del dashboard.

| Campo | Descrizione |
|---|---|
| Name | Nome visualizzato del dashboard |
| Description | Descrizione facoltativa |
| Type | Global o Personal |
| Scope | Customers o Virtual Domains |
| User | Utente associato (solo per dashboard Personal) |
| Order | Priorità di ordinamento |
| Refresh Interval (ms) | Con quale frequenza il dashboard si aggiorna automaticamente |
| Thumbnail | Riferimento immagine facoltativo per la scheda del dashboard |

### Tipi di Dashboard

| Tipo | Descrizione |
|---|---|
| **Global** | Dashboard condiviso disponibile per più utenti e contesti |
| **Personal** | Dashboard associato a un account utente specifico |

### Scope del Dashboard

| Scope | Descrizione |
|---|---|
| **Customers** | Il dashboard è disponibile nei contesti cliente |
| **Virtual Domains** | Il dashboard è disponibile nei contesti virtual domain |

---

## Connections View

Clicca sull'**icona link (🔗)** su qualsiasi riga per aprire la Connections View.

| Tab | Descrizione |
|---|---|
| Widgets | Widget presenti in questo dashboard, con proprietà di layout |
| Users | Utenti che hanno accesso a questo dashboard |
| Customers | Clienti a cui questo dashboard è associato |

### Tab Widgets

Questa è la relazione più importante per un dashboard. Ogni associazione di widget memorizza non solo quale widget è incluso, ma anche la sua **posizione e dimensione** nella griglia del dashboard:

| Proprietà | Descrizione |
|---|---|
| Index | Ordinamento del widget all'interno del dashboard |
| Width | Larghezza in unità della griglia |
| Height | Altezza in unità della griglia |
| Grid X | Posizione orizzontale |
| Grid Y | Posizione verticale |
| Settings | Payload di configurazione specifico del widget |

### Tab Users

Mostra gli utenti che hanno accesso a questo dashboard. Usa questa tab per concedere o revocare l'accesso al dashboard per utenti specifici.

### Tab Customers

Mostra i clienti a cui questo dashboard è associato. Rilevante per i dashboard visualizzati in contesti specifici del cliente.

---

!!! note
    Il layout del dashboard e la configurazione dei widget possono essere gestiti anche in modo interattivo dall'interfaccia del dashboard stesso.
    Consulta [Dashboard Management](../dashboards/management.md) per il flusso dell'utente finale.
