from abc import ABC, abstractmethod

class AlgoritmoRicerca(ABC):
    @abstractmethod
    def cerca(self, lista, elemento):
        """ Cerca un elemento nella lista e ritorna l'indice. """
        pass

class RicercaLineare(AlgoritmoRicerca):
    def cerca(self, lista, elemento):
        for i, val in enumerate(lista):
            if val == elemento:
                return i
        return -1

class RicercaBinaria(AlgoritmoRicerca):
    def cerca(self, lista, elemento):
        basso, alto = 0, len(lista) - 1
        while basso <= alto:
            medio = (basso + alto) // 2
            if lista[medio] < elemento:
                basso = medio + 1
            elif lista[medio] > elemento:
                alto = medio - 1
            else:
                return medio
        return -1

# Uso delle classi
lista_numeri = [1, 3, 5, 7, 9, 11]
ricerca_lineare = RicercaLineare()
print(ricerca_lineare.cerca(lista_numeri, 7))

ricerca_binaria = RicercaBinaria()
print(ricerca_binaria.cerca(lista_numeri, 7))



from abc import ABC, abstractmethod

class GestoreEventi(ABC):
    @abstractmethod
    def gestisci_evento(self, evento):
        """ Gestisce un evento specifico. """
        pass

class GestoreClick(GestoreEventi):
    def gestisci_evento(self, evento):
        print(f"Gestendo evento di click: {evento}")

class GestoreMovimento(GestoreEventi):
    def gestisci_evento(self, evento):
        print(f"Gestendo evento di movimento: {evento}")

# Uso delle classi
gestore_click = GestoreClick()
gestore_click.gestisci_evento('Click su bottone Salva')

gestore_movimento = GestoreMovimento()
gestore_movimento.gestisci_evento('Movimento del mouse su schermo')

