# Esempio 1: Polimorfismo con classi astratte

from abc import ABC, abstractmethod

class Veicolo(ABC):
    @abstractmethod
    def avvia(self):
        pass
    
    @abstractmethod
    def ferma(self):
        pass

class Auto(Veicolo):
    def avvia(self):
        return "L'auto è partita"
    
    def ferma(self):
        return "L'auto si è fermata"

class Bicicletta(Veicolo):
    def avvia(self):
        return "La bicicletta è partita"
    
    def ferma(self):
        return "La bicicletta si è fermata"

# Utilizzo del polimorfismo
def usa_veicolo(veicolo):
    print(veicolo.avvia())
    print(veicolo.ferma())

auto = Auto()
bicicletta = Bicicletta()

usa_veicolo(auto)        # Output: L'auto è partita \n L'auto si è fermata
usa_veicolo(bicicletta)  # Output: La bicicletta è partita \n La bicicletta si è fermata

# Esempio 2: Polimorfismo con metodi magici

class ContoBancario:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def __eq__(self, altro):
        return self.saldo == altro.saldo
    
    def __lt__(self, altro):
        return self.saldo < altro.saldo
    
    def __str__(self):
        return f"Saldo: {self.saldo}€"

conto1 = ContoBancario(1000)
conto2 = ContoBancario(1500)
conto3 = ContoBancario(1000)

# Utilizzo del polimorfismo con metodi magici
print(conto1 == conto2)  # Output: False
print(conto1 == conto3)  # Output: True
print(conto1 < conto2)   # Output: True
print(conto2 < conto1)   # Output: False

# Stampa leggibile degli oggetti
print(conto1)  # Output: Saldo: 1000€
print(conto2)  # Output: Saldo: 1500€

