# Panoramica del Cost Management

La sezione **Cost Management** fornisce strumenti per connettere XAUTOMATA ai cloud provider, importare i dati di fatturazione e organizzare i costi per l'analisi.

---

## Come Funziona

La gestione dei costi in XAUTOMATA segue tre passaggi:

1. **Registra un cloud provider** — configura le credenziali che consentono a XAUTOMATA di recuperare i dati di fatturazione da Azure, AWS o Google Cloud.
2. **Importa i dati di fatturazione** — la piattaforma interroga periodicamente le API del provider e archivia i dati di costo grezzi.
3. **Organizza e analizza** — usa i dati importati direttamente tramite i dashboard Cloud Cost, oppure riorganizzali in strutture personalizzate usando le Cost Views per la contabilità analitica.

---

## Due Prospettive di Analisi

Una volta importati i dati, possono essere analizzati in due modi:

| Prospettiva | Strumento | Ideale per |
|---|---|---|
| **Dati di fatturazione grezzi** | Widget e dashboard Cloud Cost | Monitorare i trend di spesa, suddivisioni per categoria, subscription o resource group — così come riportati dal provider |
| **Struttura di costo personalizzata** | Widget Analytical Accounting + Cost Views | Organizzare i costi per dipartimento, progetto o centro di costo — secondo il modello contabile interno |

Queste due prospettive sono complementari. La maggior parte delle organizzazioni le usa entrambe.

---

## Contenuto della Sezione

| Pagina | Scopo |
|---|---|
| [Cloud Cost Registration](cloud_cost_registration.md) | Configura le connessioni ai cloud provider |
| [Cost Views](cost_views.md) | Costruisce gerarchie di costo personalizzate per la contabilità analitica |

---

!!! note
    La Cloud Cost Registration viene tipicamente configurata durante l'onboarding dal team di delivery XAUTOMATA.
    Le Cost Views vengono create e mantenute dagli amministratori in base alle esigenze contabili dell'organizzazione.
