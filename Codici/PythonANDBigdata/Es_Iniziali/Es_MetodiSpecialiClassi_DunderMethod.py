# Classe che rappresenta un videogioco
class Videogioco:

    # __init__ viene eseguito automaticamente quando creo un nuovo oggetto
    def __init__(self, titolo, genere, prezzo, voti):
        self.titolo = titolo
        self.genere = genere
        self.prezzo = prezzo
        self.voti = voti

    # __str__ viene usato quando stampo l'oggetto con print()
    def __str__(self):
        return self.titolo + " - " + self.genere + " - " + str(self.prezzo) + " euro"

    # __repr__ restituisce una rappresentazione più tecnica dell'oggetto
    def __repr__(self):
        return "Videogioco('" + self.titolo + "', '" + self.genere + "', " + str(self.prezzo) + ")"

    # __len__ viene usato quando chiamo len() sull'oggetto
    def __len__(self):
        return len(self.voti)

    # __eq__ viene usato con l'operatore ==
    def __eq__(self, altro):
        return self.titolo == altro.titolo and self.prezzo == altro.prezzo

    # __lt__ viene usato con l'operatore <
    def __lt__(self, altro):
        return self.prezzo < altro.prezzo

    # __add__ viene usato con l'operatore +
    def __add__(self, altro):
        return self.prezzo + altro.prezzo

    # __contains__ viene usato con l'operatore in
    def __contains__(self, voto):
        return voto in self.voti

    # __getitem__ permette di usare le parentesi quadre per leggere un elemento
    def __getitem__(self, indice):
        return self.voti[indice]

    # __setitem__ permette di usare le parentesi quadre per modificare un elemento
    def __setitem__(self, indice, valore):
        self.voti[indice] = valore

    # __call__ permette di usare l'oggetto come se fosse una funzione
    def __call__(self):
        somma = 0

        for voto in self.voti:
            somma += voto

        return somma / len(self.voti)

    # __bool__ stabilisce quando l'oggetto vale True o False
    def __bool__(self):
        return self.prezzo > 0


# Creo alcuni oggetti della classe Videogioco
gioco1 = Videogioco("Dark Quest", "RPG", 30, [8, 9, 7])
gioco2 = Videogioco("Space War", "Azione", 50, [6, 7, 8])
gioco3 = Videogioco("Dark Quest", "RPG", 30, [10, 9, 8])


# __str__
print(gioco1)


# __repr__
print(repr(gioco1))


# __len__
print(len(gioco1))


# __eq__
print(gioco1 == gioco3)


# __lt__
print(gioco1 < gioco2)


# __add__
print(gioco1 + gioco2)


# __contains__
print(9 in gioco1)


# __getitem__
print(gioco1[0])


# __setitem__
gioco1[0] = 10
print(gioco1[0])


# __call__
print(gioco1())


# __bool__
if gioco1:
    print("Il videogioco ha un prezzo valido")
