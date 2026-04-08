# Access Control

Questa pagina spiega come XAUTOMATA controlla cosa ogni utente può vedere e fare nella piattaforma.
I permessi vengono configurati direttamente sui record utente tramite l'interfaccia, e possono essere raffinati con profili ACL Override.

---

## Come Funzionano i Permessi

Ogni utente ha una **configurazione ACL** — un set di scope di permesso che definisce quali operazioni può eseguire in quali aree della piattaforma.

Quando un utente tenta di eseguire un'azione (aprire una pagina, creare un record, eliminare un'entità), la piattaforma verifica la sua configurazione ACL. Se il permesso richiesto non è presente, l'azione viene bloccata o i controlli rilevanti vengono nascosti dall'interfaccia.

---

## Domini e Operazioni di Permesso

I permessi sono organizzati in tre **domini**, ciascuno dei quali copre un'area diversa della piattaforma:

| Dominio | Cosa copre |
|---|---|
| **Main** | Entità core — customers, objects, metrics, services e la maggior parte delle sezioni del Data Manager |
| **Tracking** | Calendars, downtimes e dispatchers |
| **Admin** | Sezione Administration — users, probes, notification providers e impostazioni della piattaforma |

All'interno di ogni dominio, puoi concedere le seguenti operazioni:

| Operazione | Effetto |
|---|---|
| **Read** | L'utente può visualizzare e cercare record |
| **Create** | L'utente può creare nuovi record |
| **Update** | L'utente può modificare record esistenti |
| **Delete** | L'utente può eliminare record |

Il dominio **Admin** include anche un'operazione speciale:

| Operazione | Effetto |
|---|---|
| **Super** | Accesso amministrativo completo — concede tutti i permessi su tutti i domini |

---

## Configurare i Permessi su un Utente

I permessi vengono impostati direttamente nel dialog CRUD dell'utente.

1. Vai su **Administration → Users**.
2. Apri il record utente usando l'**icona di ricerca (🔍)**.
3. Nel dialog, individua la sezione di configurazione **ACL**.
4. Abilita o disabilita gli scope di permesso necessari.
5. Clicca **SAVE CHANGES**.

L'interfaccia presenta gli scope disponibili come toggle o checkbox raggruppati per dominio e operazione. Non è necessario digitare manualmente le stringhe degli scope.

!!! note
    Un utente senza permessi concessi potrà effettuare il login ma vedrà un'interfaccia vuota senza sezioni accessibili.
    Configura sempre almeno **Main → Read** per gli account operatore standard.

---

## Tipi di Utente

La piattaforma riconosce quattro tipi di utente, determinati dalla combinazione di permessi ACL e connessioni assegnate.

### Operator

Un utente standard senza accesso amministrativo. Può navigare i dati di monitoraggio e usare i dashboard in base ai suoi permessi Main e Tracking.

Configurazione tipica:
- Main: read
- Tracking: read (facoltativamente create, update, delete per downtimes e dispatchers)
- Nessun permesso Admin

### Admin

Qualsiasi utente che ha abilitato almeno **Admin → Read**. Ottiene accesso alla sezione Administration — users, probes, notification providers e impostazioni della piattaforma.

### Tenant Admin

Un utente che agisce come **amministratore con scope limitato al cliente** — può gestire determinate risorse amministrative (come gli utenti) per i clienti di cui è responsabile, ma non ha accesso completo all'amministrazione della piattaforma.

Un Tenant Admin **non** ha bisogno di Admin → Read abilitato. Al contrario, il flag **Customer Admin** viene impostato in fondo al pannello di configurazione ACL.

Per configurare un Tenant Admin:
1. Apri il record utente.
2. Nella sezione ACL, abilita i permessi Main e Tracking desiderati se necessario.
3. Clicca il pulsante **CUSTOMER ADMIN** in fondo al pannello ACL per abilitare il flag.
4. Clicca **SAVE CHANGES**.
5. Nella Connections View, collega l'utente ai clienti specifici che amministra.

### Super User

Un utente **senza clienti collegati** nella Connections View. Il backend imposta automaticamente un flag `super=true` per questi utenti, concedendo visibilità su **tutti i clienti** nella piattaforma.

!!! warning
    Lo status di Super User viene derivato automaticamente — non è un toggle nell'interfaccia.
    Un utente diventa Super User quando non ha connessioni a clienti. Collegare anche un solo cliente rimuove la visibilità super e limita lo scope a quel cliente soltanto.
    Verifica sempre la Connections View quando risolvi problemi di visibilità dei dati inattesa per gli account amministrativi.

---

## ACL Override

Oltre ai permessi di dominio base, a un utente può essere assegnato un profilo **ACL Override**.

Un override è una configurazione riutilizzabile che applica regole aggiuntive e più specifiche sopra i permessi base dell'utente. Può:

- limitare operazioni specifiche per singole sezioni (es. disabilitare delete sugli objects)
- rendere specifici campi del form in sola lettura o nascosti
- applicare valori predefiniti a determinati campi automaticamente

### Come Funzionano gli Override con i Permessi Base

La piattaforma valuta i permessi in questo ordine:

1. Verifica se all'utente è assegnato un ACL override per l'endpoint richiesto.
2. Se sì — applica le regole dell'override. I permessi base vengono sostituiti per quell'endpoint.
3. Se no — applica i permessi di dominio base.

Questo significa che un override può sia **limitare** un permesso che l'utente avrebbe altrimenti, sia (in teoria) **concedere** accesso a endpoint specifici anche se i permessi base non lo consentirebbero.

### Assegnare un Override a un Utente

1. Vai su **Administration → Users**.
2. Apri il record utente usando l'**icona di ricerca (🔍)**.
3. Nel campo **ACL Override**, seleziona il profilo override da applicare.
4. Clicca **SAVE CHANGES**.

I profili override vengono creati e gestiti in **Super Admin → ACL Overrides**.

### Restrizioni a Livello di Campo

Gli override possono anche limitare singoli campi all'interno di un form, indipendentemente dai permessi a livello di operazione.

| Restrizione | Effetto nell'interfaccia |
|---|---|
| `disabled` | Il campo è visibile ma non può essere modificato |
| `hidden` | Il campo non viene mostrato nel form |
| `default` | Un valore predefinito viene applicato automaticamente |

Questo consente agli amministratori di impedire la modifica di campi sensibili (ad esempio il `name` di un oggetto) anche per utenti che hanno permessi generali di update.

---

## Esempi Pratici

**Operatore standard** — può navigare i dati di monitoraggio, non può modificare la configurazione:
- Main: read
- Tracking: read

**Membro del team operativo** — può anche gestire downtimes e dispatchers:
- Main: read
- Tracking: read, create, update, delete

**Admin** — può accedere alla sezione Administration:
- Main: read, create, update, delete
- Tracking: read, create, update, delete
- Admin: read (minimo)

**Tenant Admin** — amministra clienti specifici senza accesso completo alla piattaforma:
- Main: read, create, update, delete
- Tracking: read, create, update, delete
- Flag Customer Admin: ✓ abilitato
- Connections: collegato ai clienti specifici che gestisce

**Super User** — visibilità completa su tutti i clienti, nessun collegamento a clienti:
- Main: read, create, update, delete
- Tracking: read, create, update, delete
- Admin: read, create, update, delete
- Connections → Customers: nessuno (attiva automaticamente `super=true`)

**Utente in sola lettura con restrizioni sui campi** — permessi read standard più un ACL override che nasconde i campi di configurazione sensibili da tutti i form.

---

!!! note
    I profili ACL Override vengono gestiti in **Super Admin → ACL Overrides**, accessibile solo agli utenti Super Admin.
    Consulta [Users](users.md) per il flusso completo di gestione degli utenti.
