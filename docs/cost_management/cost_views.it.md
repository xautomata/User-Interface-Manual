# Cost Views

La sezione **Cost Views** consente di costruire strutture personalizzate per organizzare i costi cloud secondo il modello interno della tua organizzazione — per ambiente, dipartimento, progetto o qualsiasi altro raggruppamento che rifletta le tue esigenze contabili.

Le Cost Views sono il collegamento tra i dati di fatturazione grezzi del provider e i **widget Analytical Accounting**, che mostrano i costi organizzati secondo la struttura che definisci qui.

---

## Aprire la Sezione

Dal menu di navigazione principale, vai su **Administration → Analytical Accounting → Cost Views**.

L'interfaccia si apre direttamente in una tabella — senza pre-filter. Ogni riga rappresenta una Cost View.

| Colonna | Descrizione |
|---|---|
| Name | Nome della Cost View |
| Description | Descrizione facoltativa |
| Customer | Cliente a cui appartiene la Cost View |
| Type | `Nodes Tree` o `Azure Tags` |

![Cost Views table](../images/cost_management/cost_views/cost_views_table.png)
/// caption
Fig.1 - Tabella Cost Views
///

---

## Tipi di Cost View

XAUTOMATA supporta due tipi di Cost View:

| Tipo | Stato | Descrizione |
|---|---|---|
| **Nodes Tree** | Disponibile | Una struttura ad albero completamente configurabile costruita manualmente. I nodi raggruppano le risorse cloud tramite filtri basati su query. |
| **Azure Tags** | Coming soon | Una vista basata sui tag delle risorse Azure. L'interfaccia di configurazione è attualmente in sviluppo. |

Il resto di questa pagina tratta il tipo **Nodes Tree**, che è l'interfaccia attualmente disponibile.

---

## Nodes Tree — Panoramica

Una Cost View di tipo Nodes Tree è una gerarchia visiva di **nodi di costo**. Ogni nodo rappresenta una categoria di raggruppamento nel tuo modello contabile (ad esempio: un ambiente, un workload, un tipo di risorsa).

Le risorse di fatturazione cloud vengono assegnate ai nodi tramite **query** — regole di filtro che selezionano quali risorse appartengono a ciascun nodo. Un nodo può avere più query, e ogni query può usare tag o identificatori di risorse come criteri di selezione.

I nodi figlio possono suddividere ulteriormente le risorse del nodo padre.

![Nodes Tree editor](../images/cost_management/cost_views/cost_views_tree.png)
/// caption
Fig.2 - Editor Nodes Tree — ROOT con nodi figlio e livelli annidati
///

---

## Aprire una Cost View

Clicca sull'**icona link (↗)** su qualsiasi riga nella tabella Cost Views per aprire l'editor ad albero per quella Cost View.

L'editor mostra la gerarchia completa dei nodi a partire dal nodo **ROOT**. Ogni nodo mostra:

- il suo **nome** (in grassetto) e un'**etichetta** sottostante (ad esempio: environment, virtual machine, type)
- un'**icona ⚙️ configura** — apre il pannello Node Configuration
- un'**icona 🌿 aggiungi figlio** — aggiunge un nodo figlio sotto questo nodo

---

## Configurare un Nodo

Clicca sull'**icona ⚙️** su qualsiasi nodo per aprire il pannello **Node Configuration** sulla destra.

![Node Configuration panel](../images/cost_management/cost_views/cost_views_node_config.png)
/// caption
Fig.3 - Pannello Node Configuration con Cost Resources e pulsante Resources Definition
///

| Campo | Descrizione |
|---|---|
| Code | Identificatore breve del nodo |
| Description | Etichetta mostrata sotto il nome del nodo nell'albero |
| Actual Cost | Sola lettura — somma dei costi delle risorse assegnate |
| Budget | Target di budget facoltativo per questo nodo |

Il pannello mostra anche una tabella **Cost Resources** che elenca le risorse attualmente assegnate a questo nodo con i loro costi individuali. Clicca **Show All Resources** per vedere l'elenco completo.

Clicca **RESOURCES DEFINITION** per gestire le regole di query che determinano quali risorse vengono assegnate a questo nodo.

---

## Definire le Risorse con le Query

Cliccando **RESOURCES DEFINITION** si apre la **Resource Query List** — un elenco di query che insieme definiscono quali risorse di fatturazione appartengono al nodo.

Clicca **+ ADD NEW QUERY** per creare una nuova query. Si apre il **Query Constructor**.

![Resource Query List](../images/cost_management/cost_views/cost_views_query_list.png)
/// caption
Fig.4 - Resource Query List — aggiungi e gestisci le query per il nodo
///

### Query Constructor

Il Query Constructor offre due modalità di query:

| Modalità | Descrizione |
|---|---|
| **Tags Query** | Seleziona le risorse in base ai loro tag cloud. Seleziona prima una Tags View, poi definisci i filtri per tag. |
| **Resource Query** | Seleziona le risorse tramite identificatore di risorsa — per una selezione esplicita e manuale. |

!!! note
    Ogni query può essere solo di un tipo — Tags o Resource. Per creare una selezione di risorse più complessa, aggiungi più query allo stesso nodo.

![Query Constructor](../images/cost_management/cost_views/cost_views_query_constructor.png)
/// caption
Fig.5 - Query Constructor — modalità Tags Query e Resource Query
///

Una volta definita la query, clicca **ADD QUERY** per salvarla e tornare alla Resource Query List. Clicca **SAVE QUERIES** quando tutte le query per il nodo sono complete.

---

## Aggiungere Nodi Figlio

Clicca sull'**icona 🌿** su qualsiasi nodo per aggiungere un nodo figlio sotto di esso.

I nodi figlio consentono di suddividere le risorse di un nodo padre in raggruppamenti più granulari. Un nodo figlio può definire le proprie query per filtrare tra le risorse del suo nodo padre.

---

## Relazione con i Widget Analytical Accounting

Le Cost Views alimentano i widget **Analytical Accounting** nei dashboard:

- **Cost Nodes Tree** — mostra la gerarchia completa dei nodi con i costi effettivi e di budget per nodo
- **Cost Resources by Tag** — mostra le risorse filtrate per combinazioni di tag

Quando configuri un widget Analytical Accounting, selezioni quale Cost View deve usare come riferimento. Il widget mostra quindi i costi secondo la struttura di quella vista.

!!! note
    Il tipo di Cost View **Azure Tags** è attualmente in sviluppo. Le viste di questo tipo appaiono nella tabella ma la loro interfaccia di configurazione mostra `Coming soon`.

    I tag vengono importati automaticamente dal cloud provider durante l'acquisizione dei dati di fatturazione — XAUTOMATA li scarica direttamente dall'API del provider. Non è necessaria alcuna configurazione manuale sul lato XAUTOMATA per renderli disponibili. I tag che vedi riflettono le convenzioni di tagging usate nel tuo ambiente cloud a livello di provider.
