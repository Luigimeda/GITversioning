def totale_ordini(self):
    valore = sum(ordine.prezzo_totale for ordine in self.ordini)
    print("il totale delle vendite registrate e':", valore)