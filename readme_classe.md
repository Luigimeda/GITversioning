# Descrizione del file Python con la classe Ordini

## Introduzione
In questa fase del file andremo a visualizzare la parte della creazione della classe `Ordini` . 
Il file Python definisce una classe chiamata `Ordini`, utilizzata per rappresentare un ordine effettuato da un cliente. La classe memorizza informazioni essenziali relative all'acquisto di un prodotto e definisce gli attributi di ogni ordine. 


## Struttura della classe `Ordini` e descrizione 
La classe `Ordini` possiede un metodo costruttore (`__init__`), il quale inizializza i quattro attributi della classe :

- `nome_cliente`: Contiene il nome del cliente che ha effettuato l'ordine.
- `prodotto_acquistato`: Memorizza il nome del prodotto acquistato.
- `quantità`: Indica il numero di unità acquistate del prodotto.
- `prezzo_totale`: Memorizza il costo complessivo dell'ordine.

## Metodo `__str__()` nella classe `Ordini`
__str__() è un metodo speciale in Python che viene chiamato automaticamente quando si tenta di ottenere una rappresentazione in formato stringa di un oggetto della classe. Il metodo usa una f-string (f"") per costruire una stringa che include i valori degli attributi dell'oggetto (self.nome_cliente, self.prodotto_acquistato, self.quantità, self.prezzo_totale).


