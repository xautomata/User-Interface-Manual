# Services

La sezione **Services** gestisce le definizioni logiche di servizio utilizzate per rappresentare e monitorare i servizi business o operativi all'interno di XAUTOMATA.
I servizi si collocano al di sopra del livello infrastrutturale — aggregano metriche dagli oggetti e forniscono una vista a livello di servizio dei dati di monitoraggio.

!!! info
    I servizi rappresentano un livello di monitoraggio logico. A differenza degli oggetti, non corrispondono direttamente a una risorsa fisica — raggruppano e interpretano i dati di monitoraggio in termini di servizio o funzione di business.

---

## Aprire la Sezione Services

Dal menu di navigazione principale, vai su **Customers → Objects Repository → Services**.

L'interfaccia si apre con un **dialog di pre-filter**. Compila uno o più campi per restringere la ricerca, poi clicca **APPLY**.

| Campo filtro | Descrizione |
|---|---|
| Name | Nome del servizio |
| Description | Descrizione facoltativa |
| Profile | Classificazione del servizio |
| Customer | Cliente a cui appartiene il servizio |
| Service Parent | Servizio padre, per servizi gerarchici |
| Status | Active, Disabled o Maintenance |

Per impostazione predefinita, il pre-filter è configurato per mostrare solo i servizi **attivi**. Lascia gli altri campi vuoti e clicca **APPLY** per caricare tutti i servizi attivi.

![Services pre-filter](../../images/data_manager/services/services_prefilter.png)
/// caption
Fig.1 - Dialog di pre-filter Services
///

---

## Tabella Services

Dopo aver applicato il filtro, i risultati appaiono in una tabella dove ogni riga rappresenta un servizio.

Le colonne tipiche includono:

- Name
- Description
- Profile
- Status

La tabella supporta la selezione multipla, che abilita operazioni massive su più servizi contemporaneamente.

![Services table](../../images/data_manager/services/services_table.png)
/// caption
Fig.2 - Tabella dei risultati Services
///

---

## Dettagli del Servizio

Clicca sull'**icona di ricerca (🔍)** su qualsiasi riga per aprire il record del servizio.

Il dialog CRUD mostra la configurazione completa del servizio:

| Campo | Descrizione |
|---|---|
| Name | Nome del servizio |
| Description | Descrizione facoltativa |
| Profile | Classificazione del servizio |
| Customer | Cliente a cui è associato il servizio |
| Service Parent | Servizio padre, se si tratta di un servizio figlio |
| Status | Active, Disabled o Maintenance |
| Rule | Configurazione JSON utilizzata dalla logica del servizio |
| Automata | Configurazione JSON relativa all'automazione del servizio |

Da questo dialog puoi:

- modificare la configurazione del servizio
- duplicare il record
- eliminare il record

!!! note
    I campi **Rule** e **Automata** contengono configurazioni JSON gestite dal team di delivery XAUTOMATA. Non modificarli se non espressamente indicato.

![Service detail dialog](../../images/data_manager/services/services_crud.png)
/// caption
Fig.3 - Dialog dettaglio servizio
///

---

## Dati del Servizio

Per ispezionare i dati di monitoraggio associati a un servizio, clicca **Show Service Data** sulla riga del servizio.

Si apre una vista dedicata che mostra le analisi a livello di servizio per il servizio selezionato.

Quando sono selezionati più servizi nella tabella, usa **Multi-services data** per confrontare i dati tra servizi in parallelo.

![Service Data view](../../images/data_manager/services/services_data.png)
/// caption
Fig.4 - Vista Service Data
///

---

## Connections View

Clicca sull'**icona link (🔗)** su qualsiasi riga per aprire la **Connections View** per quel servizio.

Questa è la pagina strutturale principale per un servizio. Mostra un pannello informativo a sinistra e un'area a tab a destra con le seguenti tab:

| Tab | Descrizione |
|---|---|
| Metrics | Metriche associate a questo servizio |
| Services | Servizi figlio annidati sotto questo servizio |
| Downtimes | Finestre di manutenzione attive per questo servizio |
| Dispatchers | Regole di automazione attive collegate a questo servizio |

### Tab Metrics

Mostra le metriche collegate al servizio. Per ogni metrica puoi aprire **Metric Data** direttamente da questo contesto per ispezionare i valori storici.

### Tab Services

Mostra i servizi figlio annidati sotto questo servizio. Puoi creare nuovi servizi figlio direttamente da questa tab — la relazione padre viene precompilata automaticamente.

![Service connections view](../../images/data_manager/services/services_connections.png)
/// caption
Fig.5 - Connections view del servizio
///

---

## Vista Gerarchia Servizi

Dalla Connections View, clicca **Tree Hierarchy** per passare alla **Service Hierarchy View**.

Questa vista mostra il servizio selezionato espanso attraverso i suoi servizi figlio, consentendo di navigare strutture di servizio a più livelli.

!!! note
    A differenza della gerarchia infrastrutturale (Group → Object → Metric Type → Metric), la gerarchia dei servizi si espande solo attraverso i **servizi figlio**, non direttamente attraverso oggetti o metriche.

Per ulteriori dettagli sulla Tree Hierarchy View, consulta [Tree Hierarchy View](../tree_hierarchy_view.md).

---

## Azioni Operative

Dalla tabella dei servizi o dalla vista gerarchica puoi applicare le seguenti azioni:

| Azione | Descrizione |
|---|---|
| Show Service Data | Apre la vista delle analisi a livello di servizio |
| Downtime | Sospende temporaneamente gli alert di monitoraggio per questo servizio |
| Dispatcher | Configura una risposta automatica attivata dalle condizioni di questo servizio |

Per più servizi, usa le operazioni massive:

- **Massive Downtime**
- **Massive Dispatcher**
- **Multi-services data**

---

!!! note
    Per collegare metriche a un servizio, usa la tab **Metrics** nella Connections View.
    Per gestire gli oggetti infrastrutturali sottostanti, consulta [Objects](objects.md) e [Metrics](metrics.md).
