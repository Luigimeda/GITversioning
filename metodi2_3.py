def mostra_ordini(self):
    print("______________________")
    if any (self.ordini):
        print("Ecco la lista totale delle vendite registrate:")
        for ordine in self.ordini:
            print(ordine)
    else:
        print("Non risultano attualmente ordini registrati.")

def ordine_massimoeminimo(self, massimo, minimo):
    print("______________________")
    print("Ecco i risultati della tua ricerca:")
    for ordine in self.ordini:
        if minimo < ordine.prezzo_totale < massimo:
            print(ordine)
