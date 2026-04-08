# Cloud Cost Registration

La sezione **Cloud Cost Registration** consente di connettere XAUTOMATA ai tuoi account cloud provider in modo che i dati di fatturazione possano essere importati automaticamente.

Ogni registrazione collega un account cloud provider a un cliente specifico. Il processo segue una **procedura guidata a più step** che ti guida attraverso la selezione del cliente e la configurazione del provider.

!!! info
    La Cloud Cost Registration viene tipicamente configurata durante l'onboarding dal team di delivery XAUTOMATA.
    Questa sezione viene principalmente utilizzata per consultare le registrazioni esistenti o aggiungere nuovi account provider.

---

## Aprire la Sezione

Dal menu di navigazione principale, vai su **Administration → Cloud Cost Registration**.

Seleziona il provider che vuoi configurare:

| Provider | Descrizione |
|---|---|
| **Azure CSP** | Account Azure Cloud Solution Provider |
| **Azure** | Subscription Azure standard |
| **AWS** | Account Amazon Web Services |
| **Google Cloud** | Account di fatturazione Google Cloud Platform |

Ogni provider apre lo stesso flusso guidato, adattato ai campi specifici richiesti da quel provider.

---

## Step 1 — Seleziona o Crea un Cliente

Il primo step associa la registrazione a un cliente in XAUTOMATA.

![Registration step 1 — customer selection](../images/cost_management/cloud_cost_registration/registration_step1.png)
/// caption
Fig.1 - Step 1 — seleziona un cliente esistente o creane uno nuovo
///

Puoi:

- **Selezionare un cliente esistente** — usa il menu a tendina per cercare e selezionare un cliente già presente nella piattaforma
- **Aggiungere un nuovo cliente** — compila i dettagli del cliente direttamente nel form

Campi per un nuovo cliente:

| Campo | Descrizione |
|---|---|
| Company Name | Nome completo dell'organizzazione |
| Code | Codice contabile interno |
| VAT | Partita IVA |
| Address | Indirizzo stradale |
| ZIP | Codice postale |
| City | Città |
| State Province | Stato o provincia |
| Country | Codice paese (es. IT, GB) |
| Status | Active o Disabled |
| Currency | Valuta di fatturazione |
| Notes | Note facoltative |

Clicca **NEXT** per procedere.

---

## Step 2 — Configura l'Account Provider

Il secondo step raccoglie la configurazione e le credenziali specifiche del provider.

![Registration step 2 — provider configuration](../images/cost_management/cloud_cost_registration/registration_step2.png)
/// caption
Fig.2 - Step 2 — configurazione account provider (esempio Azure)
///

Per **Azure**, i campi includono:

| Campo | Descrizione |
|---|---|
| Azure Customer Name | Nome dell'account cliente Azure |
| Azure Customer Accounting Code | Riferimento contabile interno |
| Virtual Domain | Virtual domain da associare a questa registrazione |
| Address, ZIP, City, State Province, Country | Dettagli di localizzazione |
| Base Margin | Margine base applicato ai dati di fatturazione |
| Reserved Margin | Margine riservato applicato ai dati di fatturazione |

Per gli altri provider (AWS, Google Cloud), i campi variano in base alle credenziali e alla configurazione richieste dall'API di quel provider.

---

## Step 3 — Aggiungi Subscription

Nella parte inferiore della pagina di configurazione del provider, una sezione **Subscriptions List** consente di aggiungere una o più subscription collegate all'account provider.

Clicca **+ NEW SUBSCRIPTION** per aprire il dialog Add New Subscription.

![Add New Subscription dialog](../images/cost_management/cloud_cost_registration/registration_subscription_dialog.png)
/// caption
Fig.3 - Dialog Add New Subscription (esempio Azure)
///

Per **Azure**, i campi della subscription sono:

| Campo | Descrizione |
|---|---|
| Subscription ID | Identificatore della subscription Azure |
| Password | Credenziale di autenticazione |
| App ID | ID dell'applicazione Azure (service principal) |
| Tenant ID | Identificatore del tenant Azure |
| Expiry Date | Data di scadenza della credenziale |

Dopo aver compilato i campi, clicca **OK** per aggiungere la subscription all'elenco.

Puoi aggiungere più subscription. Ogni riga nella Subscriptions List mostra i valori configurati e fornisce le icone **modifica** ed **elimina** sulla destra.

![Registration with subscription list](../images/cost_management/cloud_cost_registration/registration_step2_subscriptions.png)
/// caption
Fig.4 - Configurazione provider con una subscription aggiunta all'elenco
///

---

## Inviare la Registrazione

Una volta completate la configurazione del provider e le subscription, clicca **SUBMIT** per salvare la registrazione.

XAUTOMATA utilizzerà le credenziali configurate per connettersi all'API del provider e inizierà a importare i dati di fatturazione.

!!! warning
    Le credenziali della subscription (Subscription ID, Password, App ID, Tenant ID) sono sensibili. Assicurati che siano sempre aggiornate — credenziali scadute bloccheranno l'importazione dei dati di fatturazione.
    Controlla regolarmente il campo **Expiry Date** e aggiorna le credenziali prima della scadenza.

---

## Cosa Succede Dopo la Registrazione

Una volta che una registrazione è attiva, XAUTOMATA recupera periodicamente i dati di fatturazione dal provider e li rende disponibili in:

- il **dashboard Cloud Cost** — analisi diretta dei dati di fatturazione grezzi
- i **widget Cloud Cost** — trend, suddivisioni, previsioni, anomalie
- i **widget Analytical Accounting** — quando i costi sono organizzati tramite [Cost Views](cost_views.md)
