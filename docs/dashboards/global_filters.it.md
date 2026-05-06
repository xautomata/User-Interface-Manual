# Global Filters

I Global Filters permettono di applicare un filtro a tutti i widget compatibili di una dashboard in un'unica operazione, senza dover configurare ogni widget separatamente.

---

## Come funzionano i Global Filters

Ogni widget può esporre uno o più dei propri filtri come **globali**. Questo viene definito nella configurazione del widget.

Quando una dashboard viene caricata, esamina tutti i widget presenti, raccoglie i filtri marcati come globali e li presenta in un pannello unificato — il **pannello Global Filters** — accessibile dalla barra delle azioni della dashboard.

L'elenco dei filtri globali disponibili dipende quindi da quali widget sono presenti sulla dashboard: aggiungere o rimuovere un widget può modificare i filtri disponibili nel pannello.

---

## Applicare un Global Filter

Apri il pannello **Global Filters** dalla barra delle azioni della dashboard e imposta i valori desiderati.

Quando applichi un filtro globale:

- Viene applicato **solo ai widget che supportano quel filtro** — i widget che non riconoscono il filtro non vengono influenzati.
- Il corrispondente filtro individuale all'interno di ogni widget interessato viene **bloccato**: non può essere modificato a livello di widget finché il filtro globale è attivo. Un messaggio nel pannello filtri del widget indica che il filtro è sotto il controllo dei Global Filters.

Questo significa che due widget sulla stessa dashboard possono condividere un filtro globale comune (ad esempio un selettore di regione o di sito) mentre ciascun widget può comunque avere i propri filtri individuali aggiuntivi per una selezione dei dati più specifica.

---

## Combinare Global Filters e filtri individuali

I Global Filters e i filtri individuali del widget possono coesistere:

1. Imposta un filtro globale per restringere l'ambito dell'intera dashboard (ad esempio mostra solo i dati per la *Lombardia*).
2. Apri il pannello filtri di un singolo widget per aggiungere ulteriori restrizioni in aggiunta all'ambito globale (ad esempio mostra solo i dispositivi in stato *Warning* in quella regione).

I filtri già controllati dal pannello Global Filters appaiono disabilitati nel pannello del widget e non possono essere sovrascritti da lì.

---

## Esempio

Una dashboard contiene tre widget, ognuno dei quali espone un filtro **Regione** come globale.

| Azione | Risultato |
|---|---|
| Imposta **Regione = Lombardia** nel pannello Global Filters | Tutti e tre i widget si aggiornano e mostrano solo i dati della Lombardia |
| Apri il pannello filtri individuale del widget A | Il filtro **Regione** è bloccato — controllato dal pannello globale |
| Aggiungi il filtro **Stato = Warning** al widget A | Il widget A mostra solo gli elementi in stato Warning in Lombardia; i widget B e C rimangono invariati |
| Rimuovi il filtro Regione globale | Tutti e tre i widget tornano all'ambito predefinito (senza filtri); Regione torna modificabile in ogni widget |
