# Analytical Accounting

Il gruppo di widget **Analytical Accounting** mostra i costi cloud organizzati secondo le strutture gerarchiche definite nelle **Cost Views**.

A differenza dei widget Cloud Cost — che mostrano i dati di fatturazione grezzi forniti dal vendor cloud — questi widget riflettono il modello di costo interno della tua organizzazione.

!!! note
    Quando configuri un widget Analytical Accounting per la prima volta, devi selezionare la **Cost View** che il widget utilizzerà come struttura di riferimento. Un singolo cliente può avere più Cost Views, ognuna delle quali rappresenta una prospettiva organizzativa diversa.

---

## Cost Nodes Tree

Mostra la gerarchia completa dei nodi di costo per la Cost View selezionata, con i costi effettivi aggregati per nodo.

![cost_nodes_tree](../images/provisional/cost_nodes_tree.png)

Cliccando su una riga di nodo si esegue il **drill-down** verso i nodi figlio, restringendo progressivamente la vista ai sotto-nodi. Puoi risalire nella gerarchia usando il breadcrumb nella parte superiore del widget.

Questo widget è lo strumento principale per esplorare i costi secondo la struttura interna della tua organizzazione — ad esempio navigando da un livello di ambiente fino ai singoli workload o tipi di risorsa.

---

## Cost Resources by Tag

Mostra tutte le risorse di costo per la Cost View selezionata nel mese di riferimento, filtrabili per tag cloud.

![cost_resources_by_tag](../images/provisional/cost_resources_by_tag.png)

### Filtri per Tag

Clicca sull'**icona del filtro** per aprire il dialog **Filters**.

| Filtro | Descrizione |
|---|---|
| **Selected Tags** | Tag che la risorsa deve avere per essere inclusa nei risultati |
| **Excluded Tags** | Tag che, se presenti, escludono la risorsa dai risultati |

Per ciascun filtro puoi scegliere l'operatore logico applicato ai tag selezionati:

| Operatore | Comportamento |
|---|---|
| **OR (Union)** | La risorsa corrisponde se ha **almeno uno** dei tag selezionati |
| **AND (Intersection)** | La risorsa corrisponde solo se ha **tutti** i tag selezionati |

I due filtri si combinano come:

```
risultati = risorse corrispondenti ai Selected Tags  MENO  risorse corrispondenti agli Excluded Tags
```

Questo consente query come:
- mostra tutte le risorse con tag `environment=PROD` **o** `environment=DR`, **escludendo** quelle con tag `type=VPN`
- mostra solo le risorse con **entrambi** i tag `virtual machine=eakdmsAPI` **e** `environment=PROD`

Abilita **Save Filters** per salvare la configurazione dei filtri corrente tra una sessione e l'altra.

!!! note
    I tag vengono importati automaticamente dal cloud provider durante l'acquisizione dei dati di fatturazione — riflettono le convenzioni di tagging utilizzate nel tuo ambiente cloud. Perché un tag sia disponibile come filtro, deve essere presente nei dati di fatturazione del provider per il mese di riferimento selezionato.
