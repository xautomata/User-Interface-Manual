# Probes

La sezione **Probes** gestisce gli agenti di monitoraggio che raccolgono dati dalle risorse infrastrutturali e li inviano a XAUTOMATA.
Ogni probe è il ponte operativo tra una risorsa monitorata e la piattaforma — senza probe, non vengono raccolte metriche.

---

## Aprire la Sezione Probes

Dal menu di navigazione principale, vai su **Administration → Probes**.

L'interfaccia si apre con un **dialog di pre-filter**. Compila uno o più campi per restringere la ricerca, poi clicca **APPLY**.

| Campo filtro | Descrizione |
|---|---|
| Name | Nome della probe |
| Description | Descrizione facoltativa |
| Probe Type | Tipo di integrazione di monitoraggio |
| Object | Risorsa infrastrutturale monitorata dalla probe |
| Virtual Domain | Dominio amministrativo a cui appartiene la probe |
| Status | Active, Disabled o Maintenance |

![Probes pre-filter](../images/administration/probes/probes_prefilter.png)
/// caption
Fig.1 - Dialog di pre-filter Probes
///

---

## Tabella Probes

Dopo aver applicato il filtro, i risultati appaiono in una tabella dove ogni riga rappresenta una probe.

Oltre ai campi standard, la tabella mostra indicatori chiave di salute:

| Colonna | Descrizione |
|---|---|
| Severity | Condizione operativa attuale della probe |
| Last Seen | Timestamp dell'ultima comunicazione con la piattaforma |
| Ingest Frequency | Intervallo atteso tra un aggiornamento dei dati e il successivo |

Usa **Severity** e **Last Seen** per identificare rapidamente le probe che potrebbero essere offline o avere problemi.

!!! warning
    Se il timestamp **Last Seen** di una probe è significativamente più vecchio della sua **Ingest Frequency**, la probe potrebbe aver smesso di raccogliere dati.
    Verifica la connettività, la configurazione o lo stato della risorsa monitorata.

![Probes table](../images/administration/probes/probes_table.png)
/// caption
Fig.2 - Tabella dei risultati Probes
///

---

## Dettagli della Probe

Clicca sull'**icona di ricerca (🔍)** su qualsiasi riga per aprire il record della probe.

| Campo | Descrizione |
|---|---|
| Name | Nome della probe |
| Description | Descrizione facoltativa |
| Probe Type | Tipo di integrazione di monitoraggio utilizzato |
| Object | Risorsa infrastrutturale monitorata |
| Virtual Domain | Dominio amministrativo |
| Data Profile | Configurazione JSON per il comportamento della probe |
| Status | Active, Disabled o Maintenance |
| Notes | Note facoltative |

Da questo dialog puoi:

- modificare la configurazione della probe
- duplicare il record
- eliminare il record

!!! note
    Il campo **Data Profile** contiene la configurazione tecnica necessaria per il funzionamento della probe. Non modificarlo se non indicato dal team di delivery XAUTOMATA.

![Probe detail dialog](../images/administration/probes/probes_crud.png)
/// caption
Fig.3 - Dialog dettaglio probe
///

---

## Log della Probe

Ogni probe fornisce accesso a una vista **Logs** che registra gli eventi operativi e i messaggi generati dalla probe.

Per aprire i log, clicca il pulsante di azione **Logs** sulla riga della probe.

Usa i log per diagnosticare problemi come:

- problemi di connettività tra la probe e la risorsa monitorata
- errori di configurazione
- errori di acquisizione dati

![Probe logs](../images/administration/probes/probes_logs.png)
/// caption
Fig.4 - Vista log della probe
///

---

## Connections View

Clicca sull'**icona link (🔗)** su qualsiasi riga per aprire la **Connections View** per quella probe.

| Tab | Descrizione |
|---|---|
| Objects | Risorse infrastrutturali associate a questa probe |

Usa questa vista per collegare una probe a oggetti aggiuntivi o per rimuovere associazioni esistenti.

---

!!! note
    I probe type definiscono la tecnologia di monitoraggio utilizzata da una probe. Consulta [Probe Types](probe_types.md) per i dettagli.
    Per capire come le probe si inseriscono nell'architettura di monitoraggio, consulta [Objects](../data_manager/objects/objects.md).
