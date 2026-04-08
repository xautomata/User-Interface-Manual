# Metric Types

La sezione **Metric Types** definisce le misure raccolte dagli oggetti monitorati.
Ogni metric type rappresenta una dimensione di monitoraggio specifica — ad esempio utilizzo CPU, latenza di rete o disponibilità del servizio — e funge da template da cui vengono registrati nel tempo i valori effettivi delle metriche.

!!! info
    Un metric type definisce *cosa* viene misurato. I valori misurati effettivi sono memorizzati come [Metrics](metrics.md).

---

## Aprire la Sezione Metric Types

Dal menu di navigazione principale, vai su **Customers → Objects Repository → Metric Types**.

L'interfaccia si apre con un **dialog di pre-filter**. Compila uno o più campi per restringere la ricerca, poi clicca **APPLY**.

| Campo filtro | Descrizione |
|---|---|
| Name | Nome del metric type |
| Description | Descrizione facoltativa |
| Profile | Classificazione della misura |
| Object | Oggetto a cui appartiene il metric type |
| Status | Active o Disabled |

Per impostazione predefinita, il pre-filter è configurato per mostrare solo i metric type **attivi**. Lascia gli altri campi vuoti e clicca **APPLY** per caricare tutti i metric type attivi.

![Metric Types pre-filter](../../images/data_manager/metric_types/metric_types_prefilter.png)
/// caption
Fig.1 - Dialog di pre-filter Metric Types
///

---

## Tabella Metric Types

Dopo aver applicato il filtro, i risultati appaiono in una tabella dove ogni riga rappresenta un metric type.

Le colonne tipiche includono:

- Name
- Description
- Profile
- Object
- Status

![Metric Types table](../../images/data_manager/metric_types/metric_types_table.png)
/// caption
Fig.2 - Tabella dei risultati Metric Types
///

---

## Dettagli del Metric Type

Clicca sull'**icona di ricerca (🔍)** su qualsiasi riga per aprire il record del metric type.

Il dialog CRUD mostra la configurazione completa:

| Campo | Descrizione |
|---|---|
| Name | Nome del metric type |
| Description | Descrizione facoltativa |
| Profile | Classificazione della misura |
| Object | Oggetto a cui è associato questo metric type |
| Data Profile | Configurazione JSON per il metric type |
| Automata Domain | Ambito di automazione |
| Status | Active o Disabled |
| Feedback for Operator | Note o indicazioni per l'operatore |

Da questo dialog puoi:

- modificare la configurazione del metric type
- duplicare il record
- eliminare il record

![Metric Type detail dialog](../../images/data_manager/metric_types/metric_types_crud.png)
/// caption
Fig.3 - Dialog dettaglio Metric Type
///

---

## Vista Struttura Metric Type

Clicca sull'**icona link (🔗)** su qualsiasi riga per aprire la **Metric Type Structure View**.

La pagina è divisa in due aree:

- un **pannello informazioni metric type** a sinistra
- un'**area di navigazione gerarchica** a destra

La gerarchia mostra le metriche associate a questo metric type — i valori effettivi di serie temporali raccolti dall'oggetto monitorato.

Usa questa vista per ispezionare i singoli record di metrica e applicare azioni operative direttamente dalla gerarchia.

Per una spiegazione dettagliata di come usare questa vista, consulta [Tree Hierarchy View](../tree_hierarchy_view.md).

![Metric Type structure view](../../images/data_manager/metric_types/metric_types_structure.png)
/// caption
Fig.4 - Vista struttura Metric Type
///

### Azioni Operative

Dalla vista gerarchica puoi applicare le seguenti azioni alle metriche:

| Azione | Descrizione |
|---|---|
| Metric Data | Apre il grafico storico o la tabella per la metrica selezionata |
| Downtime | Sospende temporaneamente gli alert di monitoraggio per la metrica selezionata |
| Dispatcher | Configura una risposta automatica attivata da un evento di monitoraggio |

I metric type supportano anche **operazioni massive** — seleziona più metriche nell'albero e applica una singola azione a tutte:

- **Massive Downtime**
- **Massive Dispatcher**

---

## Connections View

Dalla Metric Type Structure View, clicca **Connections** per passare alla **Connections View**.

Questa vista mostra le entità collegate al metric type:

| Tab | Descrizione |
|---|---|
| Metrics | Record di serie temporali associati a questo metric type |
| Downtimes | Finestre di manutenzione attive per questo metric type |
| Dispatchers | Regole di automazione attive collegate a questo metric type |

![Metric Type connections view](../../images/data_manager/metric_types/metric_types_connections.png)
/// caption
Fig.5 - Connections view del Metric Type
///

---

!!! note
    Per visualizzare i valori di serie temporali raccolti sotto un metric type, consulta [Metrics](metrics.md).
    Per gestire l'oggetto a cui appartiene questo metric type, consulta [Objects](objects.md).
