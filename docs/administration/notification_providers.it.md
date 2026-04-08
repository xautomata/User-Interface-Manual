# Notification Providers

La sezione **Notification Providers** gestisce i canali di comunicazione esterni utilizzati da XAUTOMATA per consegnare alert e azioni automatizzate.
Un notification provider memorizza i dettagli effettivi di connessione per un'integrazione specifica — ad esempio un gateway email, un endpoint webhook o una piattaforma di ticketing.

---

## Aprire la Sezione Notification Providers

Dal menu di navigazione principale, vai su **Administration → Notification Providers**.

L'interfaccia si apre con una tabella che elenca tutti i notification provider configurati.

![Notification Providers table](../images/administration/notification_providers/notification_providers_table.png)
/// caption
Fig.1 - Tabella Notification Providers
///

---

## Dettagli del Notification Provider

Clicca sull'**icona di ricerca (🔍)** su qualsiasi riga per aprire il record del provider.

| Campo | Descrizione |
|---|---|
| Application Name | Nome leggibile del provider |
| Notification Provider Type | Il tipo di provider usato come template di configurazione |
| Endpoint | Configurazione JSON con i parametri di connessione effettivi |

Il campo **Endpoint** contiene i dettagli di connessione specifici per l'integrazione — indirizzi server, URL API, token di autenticazione o altri parametri richiesti. La sua struttura esatta dipende dal tipo di provider selezionato.

Da questo dialog puoi:

- modificare la configurazione del provider
- duplicare il record
- eliminare il record

!!! note
    La configurazione **Endpoint** viene tipicamente impostata dal team di delivery XAUTOMATA durante l'onboarding.
    Contatta il team di delivery prima di modificare i parametri di connessione.

![Notification Provider detail dialog](../images/administration/notification_providers/notification_providers_crud.png)
/// caption
Fig.2 - Dialog dettaglio Notification Provider
///

---

## Connections View

Clicca sull'**icona link (🔗)** su qualsiasi riga per aprire la **Connections View**.

| Tab | Descrizione |
|---|---|
| Dispatchers | Regole di automazione che usano questo notification provider |

Usa questa vista per vedere quali dispatcher stanno attualmente usando un provider prima di apportare modifiche alla sua configurazione.

Quando si crea un nuovo dispatcher da questo contesto, il riferimento al provider viene precompilato automaticamente.

---

## Come i Notification Provider si Inseriscono nel Flusso di Notifica

```
Dispatcher attivato → Messaggio generato → Notification Provider consegna al Sistema Esterno
```

- Il **Dispatcher** definisce quando agire e quale messaggio usare.
- Il **Message** definisce il contenuto.
- Il **Notification Provider** definisce come e dove il contenuto viene consegnato.

I target di consegna tipici includono sistemi email, piattaforme di ticketing, endpoint webhook e API esterne.

---

!!! note
    I notification provider si basano sui **Notification Provider Types**, che definiscono lo schema di configurazione.
    Consulta [Notification Provider Types](notification_provider_types.md) per i dettagli.
    Per configurare le regole di automazione, consulta [Dispatchers](../data_manager/monitoring/dispatchers.md).
