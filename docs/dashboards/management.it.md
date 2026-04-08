# Gestione dei Dashboard

Questa sezione spiega come creare, configurare e gestire i dashboard. È rivolta principalmente agli **utenti avanzati e agli amministratori**.

---

## Entrare in Modalità di Modifica

Da qualsiasi dashboard in modalità di visualizzazione, clicca **EDIT WIDGETS** nella barra delle azioni.

La barra delle azioni cambia mostrando il set completo dei controlli di modifica:

| Pulsante | Azione |
|---|---|
| **+ ADD WIDGET** | Apre il Widgets Catalog per aggiungere un nuovo widget |
| **DASHBOARD SETTINGS** | Modifica i metadati del dashboard (nome, descrizione, intervallo di aggiornamento, ecc.) |
| **SAVE CHANGES** | Salva tutte le modifiche al layout e ai widget |
| **CANCEL** | Esce dalla modalità di modifica scartando le modifiche non salvate |
| **DELETE DASHBOARD** | Elimina definitivamente questo dashboard |

![Dashboard edit mode](../images/dashboards/management/dashboard-edit-mode.png)
/// caption
Fig.1 — Dashboard in modalità di modifica — barra delle azioni completa
///

---

## Aggiungere Widget

In modalità di modifica, clicca **+ ADD WIDGET**. Si apre il **Widgets Catalog** come overlay a pannello intero.

![Widgets catalog](../images/dashboards/management/dashboard-widget-catalog.png)
/// caption
Fig.2 — Widgets Catalog — ricercabile, organizzato per dominio funzionale, con anteprima visiva di ogni widget
///

Il catalog offre:

- Una **barra di ricerca** per filtrare per nome widget, gruppo o descrizione
- Widget organizzati per **gruppo funzionale** (es. Analytical Accounting, Cloud Costs, IT Infrastructure, Network…)
- Un'**anteprima visiva** e una breve descrizione per ogni widget
- Un **badge con il conteggio** su ogni gruppo che mostra quanti widget contiene — clicca sull'intestazione del gruppo per espanderlo o comprimerlo

Clicca su un widget per aggiungerlo alla griglia del dashboard. Il catalog si chiude e il widget appare sulla griglia con il prompt **"Drag the widget to move it"**.

---

## Spostare e Ridimensionare i Widget

Una volta che un widget è sulla griglia:

| Azione | Come |
|---|---|
| **Sposta** | Trascina il widget dalla sua barra del titolo in qualsiasi posizione della griglia |
| **Ridimensiona** | Trascina il punto di ridimensionamento nell'angolo in basso a destra del widget |
| **Rimuovi** | Clicca il pulsante **Remove** che appare nell'angolo in alto a destra del widget in modalità di modifica |

---

## Salvare le Modifiche

Quando hai finito di modificare, clicca **SAVE CHANGES** nella barra delle azioni. Appare una finestra di conferma:

![Save changes dialog](../images/dashboards/management/dashboard-save-changes.png)
/// caption
Fig.3 — Dialog di conferma Save Changes
///

Clicca **Yes** per salvare tutte le modifiche al layout. Clicca **No** per tornare alla modifica senza salvare.

---

## Configurare le Impostazioni del Widget

Dopo aver aggiunto un widget, potrebbe mostrare:

> *⚙ Settings are required for this widget.*

![Widget settings required](../images/dashboards/management/widget-settings-required.png)
/// caption
Fig.4 — Widget che richiede configurazione prima di poter visualizzare i dati
///

Significa che il widget ha bisogno di parametri specifici per sapere quali dati mostrare. Per configurarlo:

1. Clicca sull'**icona ⚙** nell'angolo in alto a destra del widget
2. Si apre il dialog **Widget Settings**

![Widget settings dialog](../images/dashboards/management/widget-settings-dialog.png)
/// caption
Fig.5 — Dialog Widget Settings — seleziona i parametri richiesti e abilita facoltativamente "Defined per Customer"
///

3. Compila i campi obbligatori (es. un selettore **Cost View**, una metrica, un intervallo di date)
4. Attiva facoltativamente **Defined per Customer** (vedi sotto)
5. Clicca **SAVE**

### Defined per Customer

Quando questo toggle è abilitato:

- Il layout del dashboard rimane lo stesso per tutti i clienti
- Ogni cliente può avere parametri widget diversi (es. una cost view o una sorgente dati diversa)
- Utile per dashboard globali o condivisi riutilizzati su più clienti

!!! info

    Questa funzionalità è particolarmente utile in ambienti multi-tenant dove lo stesso template di dashboard viene distribuito a più clienti, ognuno dei quali deve vedere i propri dati.

---

## Clonare un Dashboard

In modalità di visualizzazione, clicca **CLONE** per creare una copia personale di qualsiasi dashboard — inclusi quelli globali e condivisi.

Il clone viene aggiunto ai tuoi **Personal Dashboards** e può essere modificato liberamente senza influenzare l'originale.

!!! info

    Il cloning è l'approccio consigliato quando vuoi personalizzare un dashboard Global o Shared senza impattare gli altri utenti.

---

## Creare un Nuovo Dashboard Personale

1. Nella pagina home dei dashboard, clicca il pulsante **+** accanto al titolo della sezione **Personal Dashboards**
2. Compila: **Name**, **Description** (facoltativo), **Refresh interval**
3. Conferma — il nuovo dashboard vuoto si apre in **modalità di modifica**, pronto per ricevere widget

---

## Modificare le Proprietà del Dashboard

In modalità di modifica, clicca **DASHBOARD SETTINGS** per modificare:

- Nome e descrizione
- Tipo (personal / global)
- Utente proprietario
- Intervallo di aggiornamento
- Priorità di ordinamento nella lista
- Immagine di anteprima

---

## Eliminare un Dashboard

In modalità di modifica, clicca **DELETE DASHBOARD** (mostrato in rosso nella barra delle azioni).

!!! warning

    - Puoi eliminare solo i dashboard di cui sei **proprietario**
    - Eliminare un dashboard lo rimuove per **tutti gli utenti** che vi avevano accesso
    - Se hai accesso a un dashboard condiviso di cui non sei proprietario, il pulsante di eliminazione non è disponibile — puoi solo rimuoverlo dalla tua lista personale senza influenzare l'originale

---

## Riferimento Permessi

| Ruolo | Capacità |
|---|---|
| **Utente standard** | Crea / modifica / elimina dashboard personali; modifica dashboard condivisi; clona qualsiasi dashboard |
| **Amministratore** | Tutto quanto sopra + gestione dei dashboard globali e dei dashboard di altri utenti |

Per la configurazione dei permessi consulta [Access Control](../administration/access_control.md).
