class Ordini:
    def __init__(self, nome_cliente, prodotto_aquistato, quantità, prezzo_totale):
        self.nome_cliente = nome_cliente
        self.prodotto_aquistato = prodotto_aquistato
        self.quantità = quantità
        self.prezzo_totale = prezzo_totale


    def __str__(self):
        return f"Cliente: {self.nome_cliente}, Prodotto aquistato: {self.prodotto_aquistato}, Quantità: {self.quantità}, Prezzo totale:{self.prezzo_totale}"




class E_commerce:

    def __init__(self):
        self.ordini = []   ## i dizionari non servono piu visto che adotteremo la classe Ordini

    def aggiungi_ordine(self, nome_cliente, prodotto_aquistato, quantità, prezzo_totale):
        nuovo_ordine = Ordini(nome_cliente, prodotto_aquistato, quantità, prezzo_totale)  ## creiamo un nuovo ordine utilizando gli alttributi della classe ordini
        self.ordini.append(nuovo_ordine)
        print("ordine aggiunto!")
        print("ecco la lista vendite aggiornata:") 
        for ordine in self.ordini:
            print(ordine)    
    
   
    def mostra_ordini(self):
        print("_____________________")
        if any (self.ordini):
            print("Ecco la lista totale delle vendite registrate:")
            for ordine in self.ordini:
                print(ordine)
        else:
            print("Non risultano attualmente ordini registrati.")

    def ordine_massimoemassimo(self, massimo, minimo):
        print("______________________")
        print("Ecco i risultati della tua ricerca:")
        for ordine in self.ordini:
            if minimo < ordine.prezzo_totale < massimo:
                print(ordine)
   
    def totale_ordini(self):
        valore = sum(ordine.prezzo_totale for ordine in self.ordini)
        print("il totale delle vendite registrate e':", valore)

   
    
funzioni = E_commerce()

funzioni.aggiungi_ordine("Mario Rossi", "lampada", 1, 1500)  ## ordini di esempio per il funzionamento dei metodi 
funzioni.aggiungi_ordine("Maria Bianchi", "diario", 1, 1500)
