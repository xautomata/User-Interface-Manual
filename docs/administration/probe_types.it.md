# Probe Types

La sezione **Probe Types** elenca le tecnologie di integrazione di monitoraggio disponibili in XAUTOMATA.
Ogni probe type definisce come un agente di monitoraggio raccoglie i dati — ad esempio un agente di monitoraggio di sistema, una probe di rete o un'integrazione cloud.

!!! info
    I probe type sono configurazioni di riferimento gestite dal team di delivery XAUTOMATA.
    Questa sezione è principalmente informativa — normalmente non creerai né eliminerai probe type dall'interfaccia.

---

## Aprire la Sezione Probe Types

Dal menu di navigazione principale, vai su **Administration → Probe Types**.

L'interfaccia si apre con una tabella che elenca tutti i probe type disponibili.

![Probe Types table](../images/administration/probe_types/probe_types_table.png)
/// caption
Fig.1 - Tabella Probe Types
///

---

## Dettagli del Probe Type

Clicca sull'**icona di ricerca (🔍)** su qualsiasi riga per aprire il record del probe type.

| Campo | Descrizione |
|---|---|
| Code | Identificatore breve del probe type |
| Name | Nome descrittivo dell'integrazione di monitoraggio |
| Endpoint | Configurazione JSON che definisce i parametri di comunicazione |

Il campo **Endpoint** contiene i parametri tecnici utilizzati dalla piattaforma per interagire con le probe di questo tipo. È gestito dal team di delivery.

---

## Connections View

Clicca sull'**icona link (🔗)** su qualsiasi riga per aprire la **Connections View**.

Questa vista mostra tutte le **Probes** che utilizzano il probe type selezionato — utile per capire lo scope di un'integrazione prima di apportare modifiche.

---

!!! note
    Per gestire gli agenti di monitoraggio basati su un probe type, consulta [Probes](probes.md).
