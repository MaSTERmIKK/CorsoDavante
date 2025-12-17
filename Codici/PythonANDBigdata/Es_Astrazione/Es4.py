from abc import ABC, abstractmethod

class Animale(ABC):
    @abstractmethod
    def muovi(self):
        pass

class EmettitoreSuoni(ABC):
    @abstractmethod
    def suona(self):
        pass

class Cane(Animale, EmettitoreSuoni):
    def muovi(self):
        print("Il cane corre.")

    def suona(self):
        print("Il cane abbaia.")

# Creazione e uso dell'oggetto Cane
cane = Cane()
cane.muovi()
cane.suona()

from abc import ABC, abstractmethod

class Animale(ABC):
    @abstractmethod
    def mangia(self):
        pass

class AnimaleDomestico(Animale):
    @abstractmethod
    def gioca(self):
        pass

class Gatto(AnimaleDomestico):
    def mangia(self):
        print("Il gatto mangia crocchette.")

    def gioca(self):
        print("Il gatto gioca con la palla di lana.")

# Creazione e uso dell'oggetto Gatto
gatto = Gatto()
gatto.mangia()
gatto.gioca()





