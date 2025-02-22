
from ecommerce import funzioni

funzioni.aggiungi_ordine("Mario Rossi", "lampada", 1, 1500)
funzioni.aggiungi_ordine("Maria Bianchi", "diario", 1, 1500)

print("--- MENU ---")
print("1. Aggiungi un nuovo ordine")
print("2. Mostra tutti gli ordini")
print("3. Filtra ordini per importo minimo o massimo")
print("4. Calcola il totale di tutti gli ordini")
print("6. Esci")
scelta = int(input("effettua la tua scelta:"))

if scelta == 1:
    nome_cliente = input("inserisci il nome del cliente:")
    prodotto_acquistato = input("inserisci il prodotto acquistato:")
    quantità_prodotto = int(input("inserisci la quantità:"))
    prezzo_totale = int(input("inserisci il prezzo totale:"))
    funzioni.aggiungi_ordine(nome_cliente, prodotto_acquistato, quantità_prodotto, prezzo_totale)
elif scelta == 2:
    funzioni.mostra_ordini()
elif scelta == 3:
    massimo = int(input("inserisci il valore massimo:"))
    minimo = int(input("inserisci il valore minimo:"))
    funzioni.ordine_massimoemassimo(massimo, minimo)
elif scelta == 4:
    funzioni.totale_ordini()
elif scelta == 6:
    print("Grazie per aver usato questo programma!")
        
