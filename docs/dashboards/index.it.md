# Panoramica delle Dashboard

## Accesso alla Piattaforma

### Login

Apri `portal.xautomata.com` nel browser. La pagina di login offre tre metodi di accesso:

- **Username / Password** — inserisci le credenziali e clicca **LOGIN**
- **SSO** — usa **LOGIN WITH GOOGLE**, **LOGIN WITH MICROSOFT** o **LOGIN WITH APPLE**
- **App mobile** — scansiona il QR code con l'app mobile XAUTOMATA per connetterti a questo ambiente

![Login](../images/getting_started/login.jpg)
/// caption
Fig.1 - Pagina di Login
///

### Selezione del Cliente

Dopo il login, la piattaforma mostra la schermata di selezione del cliente. Qui sono elencati tutti i clienti a cui hai accesso.

- Clicca sull'**icona ★** su una scheda cliente per aggiungerla ai **Favorites** — i clienti con la stella appaiono in cima per un accesso rapido
- Usa la barra **Search** per filtrare per nome cliente
- Passa tra **Customers** e **Virtual Domains** usando le tab nella top bar

![Customer selection](../images/getting_started/customer_selection.png)
/// caption
Fig.2 - Selezione del Cliente
///

---

## Dashboard Home

La Fig. 3 mostra la pagina che appare subito dopo aver selezionato un cliente. Questa pagina presenta una serie di menu per l'interazione:

1. Menu Home per tornare a questa schermata durante la navigazione nel portale.
2. Cliccando sul nome del cliente, accedi a una vista dedicata agli asset del cliente e a come sono organizzati logicamente in XAUTOMATA.
3. Profilo utente.
4. Crea nuove dashboard private vuote da riempire con i widget selezionati.
5. Lista dei **Personal Dashboards**. Cliccando su una delle dashboard in questa lista accedi alla dashboard specifica.
6. Lista degli **Shared Dashboards**. Dashboard che altri utenti hanno condiviso con te. Questa sezione appare solo se almeno una dashboard è stata condivisa con il tuo account.
7. Lista dei **Global Dashboards**. Cliccando su una delle dashboard globali accedi a una delle seguenti:

      1. **Support Service KPI**: Dashboard dedicato alla visualizzazione e gestione dei ticket per i vari ITSM integrati nel servizio.
      2. **Cloud Costs**: Dashboard dedicato alla visualizzazione dei costi cloud per i principali cloud provider.
      3. **Cloud Cost Analytics**: Dashboard dedicato alla contabilità analitica, dove è possibile organizzare i costi cloud in base ai loro tag.
      4. **Network**: Dashboard dedicato alla visualizzazione delle informazioni sulle reti internet.
      5. **NetFlow**: Dashboard dedicato alla visualizzazione delle informazioni NetFlow di una rete, con dati dettagliati sulla gestione del traffico.
      6. **IT Infrastructure**: Dashboard dedicato alla visualizzazione delle informazioni sull'infrastruttura IT.

8. Menu Customer/Administrator/Dispatcher.

![Dashboard Home](../images/dashboards/overview.jpg)
/// caption
Fig.3 - Dashboard Home
///

!!! note

    Non tutte le dashboard sono sempre visibili; dipende dalla visibilità che l'utente ha sui widget contenuti in ciascuna dashboard. Se nessun widget di una dashboard è visibile all'utente, la dashboard stessa non verrà mostrata nell'interfaccia. La visibilità dei widget dipende dal tipo di dati raccolti da XAUTOMATA per gestire i processi digitalizzati e dal tipo di contratto in essere.

---

## Tipi di Dashboard

| Tipo | Visibile a | Modificabile da |
|---|---|---|
| **Personal** | Solo tu | Solo tu |
| **Shared** | Tu + utenti designati | Tutti gli utenti con accesso |
| **Global** | Tutti gli utenti dell'organizzazione | Solo gli amministratori |

!!! warning

    Le dashboard condivise sono **collaborative**: le modifiche al layout sono visibili a tutti gli utenti che hanno accesso alla stessa istanza. Usa **CLONE** per creare una copia personale se vuoi lavorare in modo indipendente.

---

## Modalità di Visualizzazione della Dashboard

Quando apri una dashboard, sei in **modalità di visualizzazione**. La barra delle azioni mostra:

| Pulsante | Azione |
|---|---|
| **EDIT WIDGETS** | Entra in modalità di modifica per aggiungere, spostare, ridimensionare o rimuovere widget |
| **CLONE** | Crea una copia personale di questa dashboard |
| **SCREENSHOT** | Scarica un'immagine istantanea della vista attuale della dashboard |

Il selettore **Customer** e il filtro **Reference Month** in alto a destra si applicano a tutti i widget simultaneamente.

![Dashboard view mode](../images/dashboards/dashboard_view_mode.png)
/// caption
Fig.4 — Dashboard in modalità di visualizzazione — barra delle azioni con EDIT WIDGETS, CLONE, SCREENSHOT
///

---

## Dashboard Disponibili

- [IT Infrastructure](it_infrastructure.md) — stato e disponibilità dei sistemi IT
- [Network](network.md) — connettività e performance WAN
- [Cloud Cost](cloud_cost.md) — spesa multi-cloud (Azure, AWS, GCP)

Per la creazione e la configurazione delle dashboard consulta [Dashboard Management](management.md).
