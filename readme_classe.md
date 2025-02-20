# Descrizione del file Python con la classe Ordini

## Introduzione
Il file Python definisce una classe chiamata `Ordini`, utilizzata per rappresentare un ordine effettuato da un cliente. La classe memorizza informazioni essenziali relative all'acquisto di un prodotto e definisce gli attributi di ogni ordine. 


## Struttura della classe `Ordini`
La classe `Ordini` possiede un metodo costruttore (`__init__`), il quale inizializza i quattro attributi della classe :

- `nome_cliente`: Contiene il nome del cliente che ha effettuato l'ordine.
- `prodotto_acquistato`: Memorizza il nome del prodotto acquistato.
- `quantità`: Indica il numero di unità acquistate del prodotto.
- `prezzo_totale`: Memorizza il costo complessivo dell'ordine.


### Esempio di utilizzo
```python
# Creazione di un oggetto Ordini
ordine1 = Ordini("Mario Rossi", "Laptop", 2, 2500.00)

# Accesso agli attributi dell'ordine
print("Cliente:", ordine1.nome_cliente)
print("Prodotto acquistato:", ordine1.prodotto_acquistato)
print("Quantità:", ordine1.quantità)
print("Prezzo totale:", ordine1.prezzo_totale)
