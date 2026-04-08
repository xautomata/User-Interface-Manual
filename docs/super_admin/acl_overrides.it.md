# ACL Overrides

La sezione **ACL Overrides** gestisce i profili di permesso riutilizzabili che possono essere applicati agli utenti per limitare o modificare il loro comportamento di accesso predefinito.

Un ACL override definisce regole specifiche per endpoint che hanno precedenza sui permessi base di un utente — limitando operazioni, nascondendo campi o applicando valori predefiniti su sezioni specifiche della piattaforma.

!!! warning
    Questa sezione è riservata agli utenti **Super Admin**. Gli ACL override influenzano l'esperienza dell'interfaccia e le azioni disponibili per tutti gli utenti a cui sono assegnati.

---

## Aprire la Sezione

Dal menu di navigazione principale, vai su **Administration → Super Admin → ACL Overrides**.

L'interfaccia si apre con una tabella che elenca tutti i profili override definiti.

| Colonna | Descrizione |
|---|---|
| Code | Identificatore univoco del profilo override |

---

## Dettagli dell'Override

Clicca sull'**icona di ricerca (🔍)** su qualsiasi riga per aprire il record dell'override.

| Campo | Descrizione |
|---|---|
| Code | Identificatore univoco del profilo |
| Override Rules | Configurazione JSON che definisce le regole di permesso |

Il campo **Override Rules** contiene la configurazione effettiva dei permessi come struttura JSON. Ogni chiave nel JSON punta a uno specifico endpoint API, e i valori associati definiscono i permessi e le restrizioni dei campi per quell'endpoint.

### Struttura delle Override Rules

```json
{
  "/objects/": {
    "acl": {
      "read": true,
      "create": false,
      "delete": false,
      "update": true
    },
    "fields": [
      {
        "key": "name",
        "editable": false
      },
      {
        "key": "description",
        "editable": false
      }
    ]
  }
}
```

In questo esempio, per l'endpoint `/objects/`:
- read e update sono consentiti
- create e delete sono disabilitati
- i campi `name` e `description` sono visibili ma non modificabili

### Restrizioni a Livello di Campo

| Restrizione | Effetto nell'interfaccia |
|---|---|
| `editable: false` | Il campo è visibile ma non può essere modificato |
| `hidden: true` | Il campo non viene visualizzato nel form |
| `default` | Un valore predefinito viene applicato automaticamente |

---

## Connections View

Clicca sull'**icona link (🔗)** su qualsiasi riga per aprire la Connections View.

| Tab | Descrizione |
|---|---|
| Users | Utenti a cui questo profilo override è attualmente assegnato |

Usa questa tab per vedere quali utenti sono interessati dall'override selezionato, o per assegnarlo a utenti aggiuntivi.

!!! note
    Un profilo override può essere assegnato anche direttamente dal record utente.
    Consulta il campo **ACL Override** in [Users](../administration/users.md).

---

## Come gli Override Interagiscono con i Permessi Base

Quando un utente tenta di eseguire un'azione, la piattaforma valuta i permessi in questo ordine:

1. Verifica se all'utente è assegnato un ACL override per l'endpoint richiesto.
2. Se sì — applica le regole dell'override. I permessi base dell'utente vengono sostituiti per quell'endpoint.
3. Se no — applica i permessi di dominio base dell'utente.

Questo significa che un override può limitare l'accesso che l'utente avrebbe altrimenti in base ai soli permessi di dominio.

Per il modello di permessi completo, consulta [Access Control](../administration/access_control.md).
