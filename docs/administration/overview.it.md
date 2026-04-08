# Panoramica dell'Administration

La sezione **Administration** fornisce gli strumenti per configurare e gestire la piattaforma stessa — accesso degli utenti, agenti di monitoraggio, canali di notifica e policy di sicurezza.

Mentre il **Data Manager** si concentra su cosa viene monitorato, la sezione Administration si concentra su **chi può accedere alla piattaforma** e **come la piattaforma comunica con il mondo esterno**.

---

## Cosa Puoi Fare Qui

| Area | Scopo |
|---|---|
| [Users](users.md) | Crea e gestisce gli account utente, configura i permessi |
| [Access Control](access_control.md) | Comprendi e configura il modello di permessi ACL |
| [Virtual Domains](virtual_domains.md) | Organizza utenti, gruppi e probe in scope logici |
| [Probes](probes.md) | Gestisce gli agenti di monitoraggio e diagnostica i problemi di raccolta |
| [Probe Types](probe_types.md) | Visualizza i tipi di integrazione di monitoraggio disponibili |
| [Messages](messages.md) | Configura i template per il contenuto delle notifiche |
| [Notification Providers](notification_providers.md) | Configura i canali di consegna esterni (email, webhook, ticketing) |
| [Notification Provider Types](notification_provider_types.md) | Visualizza i tipi di integrazione di notifica disponibili |

---

## Due Responsabilità Principali

### Gestione degli Accessi

Gli account utente controllano chi può accedere alla piattaforma e cosa può vedere e fare.
I permessi vengono configurati tramite il **modello ACL** direttamente su ogni record utente.
Per ambienti che richiedono un controllo granulare, i profili **ACL Override** (gestiti in Super Admin) possono limitare operazioni o campi specifici per gruppi di utenti.

Consulta [Users](users.md) e [Access Control](access_control.md).

### Notifiche e Consegna delle Automazioni

Quando un evento di monitoraggio attiva un Dispatcher, la piattaforma deve sapere cosa inviare e dove inviarlo.

- **Messages** definisce i template per il contenuto delle notifiche.
- **Notification Providers** definisce i canali di consegna.
- **Notification Provider Types** definisce i modelli di integrazione disponibili.

Queste tre entità lavorano insieme come strato di comunicazione in uscita della piattaforma.

Consulta [Messages](messages.md), [Notification Providers](notification_providers.md) e [Dispatchers](../data_manager/monitoring/dispatchers.md).

---

!!! note
    Probes e Probe Types vengono gestiti qui, ma sono tipicamente configurati durante l'onboarding dal team di delivery XAUTOMATA.
    La sezione Administration viene usata principalmente nella quotidianità per la gestione di utenti e notifiche.
