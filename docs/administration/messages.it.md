# Messages

La sezione **Messages** gestisce i template di notifica utilizzati da XAUTOMATA per generare il contenuto degli alert e dei payload di comunicazione esterna.

!!! info
    I Messages definiscono *cosa* viene inviato — non inviano nulla da soli.
    Un messaggio viene sempre attivato da un [Dispatcher](../data_manager/monitoring/dispatchers.md), che determina *quando* e *dove* viene consegnato.

---

## Aprire la Sezione Messages

Dal menu di navigazione principale, vai su **Administration → Messages**.

L'interfaccia si apre con una tabella che elenca tutti i template di messaggio disponibili.

![Messages table](../images/administration/messages/messages_table.png)
/// caption
Fig.1 - Tabella Messages
///

---

## Dettagli del Messaggio

Clicca sull'**icona di ricerca (🔍)** su qualsiasi riga per aprire il record del messaggio.

| Campo | Descrizione |
|---|---|
| Code | Identificatore univoco del template di messaggio |
| Description | Descrizione leggibile dello scopo del template |
| Mask Mime Type | Formato del corpo principale del messaggio (HTML, JSON o Text) |
| Mask | Template principale del messaggio con placeholder dinamici |
| Additional Mask Mime Type | Formato del payload secondario facoltativo |
| Additional Mask | Payload secondario facoltativo (usato per integrazioni con sistemi esterni) |

Da questo dialog puoi:

- modificare il template di messaggio
- duplicare il record
- eliminare il record

![Message detail dialog](../images/administration/messages/messages_crud.png)
/// caption
Fig.2 - Dialog dettaglio messaggio
///

---

## Template di Messaggio e Variabili Dinamiche

Il campo **Mask** è il contenuto principale della notifica. Può includere placeholder dinamici che la piattaforma sostituisce a runtime con valori dal contesto di monitoraggio.

Esempio di mask HTML:

```html
<b>Issue on:</b> {{object_name}}
Last alarm: {{last_value_timestamp_CET}}
Description: <<automaton_wildcard::description>>
```

La **Additional Mask** è un payload secondario facoltativo usato quando si integra con sistemi esterni come piattaforme di ticketing. È tipicamente formattata come JSON:

```json
{
  "customerCode": "042781",
  "shortDescription": "[CHECKMK] {{object_name}}"
}
```

### Scope delle Variabili Disponibili

Quando si modifica una mask, le variabili dinamiche possono provenire dai seguenti scope:

| Scope | Descrizione |
|---|---|
| Customer | Informazioni a livello di cliente |
| Site | Informazioni a livello di sede |
| Group | Informazioni a livello di gruppo |
| Virtual Domain | Informazioni sul virtual domain |
| Object | Informazioni a livello di oggetto |

!!! note
    I nomi specifici delle variabili disponibili dipendono dallo scope e dalla configurazione della piattaforma.
    Contatta il team di delivery XAUTOMATA per l'elenco completo dei placeholder disponibili.

---

## Come i Messages si Inseriscono nel Flusso di Notifica

```
Evento di monitoraggio → Dispatcher attivato → Messaggio generato → Notification Provider consegna
```

1. Si verifica una condizione di monitoraggio.
2. Il motore di automazione della piattaforma attiva un **Dispatcher**.
3. Il dispatcher usa questo template **Message** per generare il contenuto della notifica.
4. Il messaggio generato viene consegnato tramite un **Notification Provider**.

Lo stesso template di messaggio può essere riutilizzato su più dispatcher, garantendo contenuto di notifica coerente tra diverse regole di automazione.

---

!!! note
    Per configurare il canale di consegna, consulta [Notification Providers](notification_providers.md).
    Per configurare la regola di automazione che attiva questo messaggio, consulta [Dispatchers](../data_manager/monitoring/dispatchers.md).
