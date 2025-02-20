def __init__(self):
    self.ordini=[  ##ho creato dei dizionari gia pronti per testare le funzioni
        {"cliente":"Paola","prodotto":"pianta","quantita":4,"totale":47},
        {"cliente":"Simone Mastroeni","prodotto":"computer","quantita":1,"totale":564},
    ]

def aggiungi_ordine(self,nome_cliente,prodotto_aquistato,quantità,prezzo_totale):
    nuovo_ordine = {'cliente':nome_cliente, 'prodotto': prodotto_aquistato, 'quantita': quantità, 'totale': prezzo_totale}
    self.ordini.append(nuovo_ordine)
    print("ordine aggiunto!")
    print("ecco la lista vendite aggiornata:")
    for ordine in self.ordini:
        print(ordine)