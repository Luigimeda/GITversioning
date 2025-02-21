## Introduzione
In questa fase del file andremo a visualizzare come funzionano i punti 2 e 3, ossia le funzioni
    - mostra_ordini
    - ordine_massimoeminimo

# Descrizione
La funzione mostra_ordini è progettata per visualizzare un elenco di ordini:

  1. Verifica se ci sono ordini: La funzione inizia controllando se la lista self.ordini contiene almeno un ordine. Questo viene fatto usando la funzione any(). Se la lista è vuota, any() restituirà False.
  2. Stampa gli ordini: Se ci sono ordini nella lista, la funzione stampa un messaggio che indica che sta per mostrare l'elenco degli ordini.
  3. Gestione degli ordini mancanti: Se non ci sono ordini nella lista, la funzione stampa un messaggio che indica che non ci sono ordini registrati.

La funzione ordine_massimoeminimo è progettata per trovare e visualizzare gli ordini che rientrano in un intervallo di prezzo specificato dall'utente:

 1. Riceve i limiti di prezzo: La funzione accetta due argomenti, massimo e minimo, che rappresentano il prezzo massimo e minimo dell'intervallo da cercare.
 2. Confronto dei prezzi: Per ogni ordine, la funzione controlla se il prezzo totale dell'ordine (ordine.prezzo_totale) è compreso tra il prezzo minimo e il prezzo massimo specificati dall'utente.
 3. Stampa gli ordini corrispondenti: Se il prezzo totale dell'ordine rientra nell'intervallo stabilito dal cliente quindi la funzione stamperà le informazioni dell'ordine.

# Conclusione
In sostanza, la funzione mostra_ordini è una funzione di base per visualizzare un elenco di ordini.
La funzione ordine_massimoeminimo è una funzione più specifica per trovare e visualizzare gli ordini che soddisfano un criterio di prezzo specifico.
