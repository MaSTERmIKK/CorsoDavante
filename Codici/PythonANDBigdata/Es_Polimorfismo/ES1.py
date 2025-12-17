# Esempio 1: Polimorfismo con interfacce

class Forma:
    def area(self):
        pass

class Rettangolo(Forma):
    def __init__(self, larghezza, altezza):
        self.larghezza = larghezza
        self.altezza = altezza
    
    def area(self):
        return self.larghezza * self.altezza

class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio
    
    def area(self):
        return 3.14 * (self.raggio ** 2)

# Utilizzo del polimorfismo
def calcola_area(forma):
    print(f"L'area è: {forma.area()}")

rettangolo = Rettangolo(5, 3)
cerchio = Cerchio(4)

calcola_area(rettangolo)  # Output: L'area è: 15
calcola_area(cerchio)     # Output: L'area è: 50.24







# Esempio 2: Polimorfismo con operatori sovraccaricati

class Vettore:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, altro):
        return Vettore(self.x + altro.x, self.y + altro.y)
    
    def __str__(self):
        return f"Vettore({self.x}, {self.y})"

v1 = Vettore(2, 3)
v2 = Vettore(1, 5)

# Utilizzo del polimorfismo con l'operatore +
v3 = v1 + v2

print(v3)  # Output: Vettore(3, 8)






# Esempio 1: Polimorfismo con classi e metodi

class Animale:
    def suono(self):
        pass

class Cane(Animale):
    def suono(self):
        return "Bau Bau"

class Gatto(Animale):
    def suono(self):
        return "Miao Miao"

# Utilizzo del polimorfismo
def fai_suono(animale):
    print(animale.suono())

cane = Cane()
gatto = Gatto()

fai_suono(cane)  # Output: Bau Bau
fai_suono(gatto)  # Output: Miao Miao

# Esempio 2: Polimorfismo con funzioni

def add(a, b):
    return a + b

# Polimorfismo con interi
print(add(5, 3))  # Output: 8

# Polimorfismo con stringhe
print(add("Ciao ", "Mondo"))  # Output: Ciao Mondo

# Polimorfismo con liste
print(add([1, 2], [3, 4]))  # Output: [1, 2, 3, 4]



