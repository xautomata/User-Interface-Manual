# Widget Groups

La sezione **Widget Groups** gestisce le raccolte logiche di widget.
Un widget group raggruppa widget correlati e controlla quali utenti possono accedervi — assegnare un gruppo a un utente concede la visibilità di tutti i widget in quel gruppo.

!!! warning
    Questa sezione è riservata agli utenti **Super Admin**. Le modifiche qui influenzano la visibilità dei widget per tutti gli utenti assegnati.

---

## Aprire la Sezione

Dal menu di navigazione principale, vai su **Administration → Super Admin → Widget Groups**.

L'interfaccia si apre con una tabella che elenca tutti i widget group.

| Colonna | Descrizione |
|---|---|
| Name | Nome leggibile del gruppo |
| Code | Identificatore univoco |
| Status | Active o Disabled |
| Description | Descrizione facoltativa |

---

## Dettagli del Widget Group

Clicca sull'**icona di ricerca (🔍)** su qualsiasi riga per aprire il record del widget group.

| Campo | Descrizione |
|---|---|
| Name | Nome visualizzato del gruppo |
| Code | Identificatore univoco usato internamente dalla piattaforma |
| Status | Active o Disabled |
| Description | Descrizione facoltativa |

Da questo dialog puoi modificare, duplicare o eliminare il gruppo.

---

## Connections View

Clicca sull'**icona link (🔗)** su qualsiasi riga per aprire la Connections View.

| Tab | Descrizione |
|---|---|
| Widgets | Definizioni di widget incluse in questo gruppo |
| Users | Utenti assegnati a questo widget group |

### Tab Widgets

Mostra tutte le definizioni di widget collegate a questo gruppo. Usa questa tab per aggiungere o rimuovere widget dal gruppo.

### Tab Users

Mostra tutti gli utenti a cui è stato assegnato questo widget group. Gli utenti collegati qui acquisiscono la visibilità di tutti i widget nel gruppo.

!!! note
    L'assegnazione dei widget group è gestibile anche dal lato utente — consulta la tab **Widget Groups** nella Connections View di [Users](../administration/users.md).

---

## Come Funziona la Visibilità dei Widget

```
Widget Group → contiene Widgets
Widget Group → assegnato a Users
↓
L'utente vede i Widgets nei suoi gruppi assegnati
```

Quando un utente apre una dashboard, nel catalogo dei widget appaiono solo i widget appartenenti ai widget group a lui assegnati. Se un widget group è inattivo o non assegnato all'utente, i suoi widget non sono visibili.

---

!!! note
    Per gestire a quali dashboard un utente può accedere (separato dalla visibilità dei widget), consulta [Users](../administration/users.md) e [Dashboards](dashboards.md).
