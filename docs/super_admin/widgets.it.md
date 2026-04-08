# Widgets

La sezione **Widgets** gestisce il catalogo delle definizioni di widget disponibili nella piattaforma.
Ogni definizione di widget è il record amministrativo che corrisponde a un componente visivo visualizzato nei dashboard.

!!! warning
    Questa sezione è riservata agli utenti **Super Admin**. Le modifiche qui hanno effetto sull'intera piattaforma e su tutti gli utenti.

---

## Aprire la Sezione

Dal menu di navigazione principale, vai su **Administration → Super Admin → Widgets**.

L'interfaccia si apre con una tabella che elenca tutte le definizioni di widget.

| Colonna | Descrizione |
|---|---|
| Name | Nome leggibile del widget |
| Code | Identificatore tecnico univoco |
| Scope | Contesto in cui il widget può essere utilizzato |
| Status | Active o Disabled |
| Description | Descrizione facoltativa |

La tabella può essere filtrata per **Scope** e **Status**.

---

## Dettagli del Widget

Clicca sull'**icona di ricerca (🔍)** su qualsiasi riga per aprire il record del widget.

| Campo | Descrizione |
|---|---|
| Name | Nome visualizzato del widget |
| Code | Identificatore univoco usato dal frontend per risolvere il componente widget |
| Scope | Contesto in cui il widget è disponibile |
| Status | Active o Disabled |
| Description | Descrizione facoltativa |

!!! note
    Il campo **Code** è la chiave tecnica che collega questo record amministrativo al componente visivo effettivo nel frontend. Deve corrispondere esattamente all'identificatore usato nell'implementazione frontend.

---

## Connections View

Clicca sull'**icona link (🔗)** su qualsiasi riga per aprire la Connections View.

| Tab | Descrizione |
|---|---|
| Dashboards | Dashboard che includono questo widget, con proprietà di layout (posizione, dimensione, impostazioni) |
| Widget Groups | Gruppi di widget a cui appartiene questo widget |

### Proprietà di Posizionamento nel Dashboard

Quando un widget è collegato a una dashboard, l'associazione memorizza la posizione e le dimensioni del widget nella griglia della dashboard:

| Proprietà | Descrizione |
|---|---|
| Index | Ordinamento del widget all'interno della dashboard |
| Width | Larghezza in unità della griglia |
| Height | Altezza in unità della griglia |
| Grid X | Posizione orizzontale nella griglia |
| Grid Y | Posizione verticale nella griglia |
| Settings | Payload di configurazione specifico del widget |

---

!!! note
    Per controllare quali utenti possono vedere un widget, assegnalo a un **Widget Group** e poi assegna quel gruppo agli utenti rilevanti.
    Consulta [Widget Groups](widget_groups.md).
