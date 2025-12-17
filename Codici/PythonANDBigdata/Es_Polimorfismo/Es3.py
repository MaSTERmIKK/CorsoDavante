# Esempio 1: Polimorfismo con moduli di terze parti (usando il modulo 'abc')

from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def paga(self, amount):
        pass

class PagamentoConCarta(Pagamento):
    def paga(self, amount):
        return f"Pagamento di {amount}€ effettuato con carta di credito"

class PagamentoConPayPal(Pagamento):
    def paga(self, amount):
        return f"Pagamento di {amount}€ effettuato con PayPal"

# Utilizzo del polimorfismo
def processa_pagamento(metodo_pagamento, amount):
    print(metodo_pagamento.paga(amount))

carta = PagamentoConCarta()
paypal = PagamentoConPayPal()

processa_pagamento(carta, 100)  # Output: Pagamento di 100€ effettuato con carta di credito
processa_pagamento(paypal, 200)  # Output: Pagamento di 200€ effettuato con PayPal

# Esempio 2: Polimorfismo con funzioni generiche

class Alunno(ABC):
    def __init__(self, nome, voto):
        self.nome = nome
        self.voto = voto

    def __str__(self):
        return f"Alunno: {self.nome}, Voto: {self.voto}"

class Insegnante(ABC):
    def __init__(self, nome, materia):
        self.nome = nome
        self.materia = materia

    def __str__(self):
        return f"Insegnante: {self.nome}, Materia: {self.materia}"

# Funzione generica
def stampa_dettagli(persona):
    print(persona)

alunno = Alunno("Giulia", 9.5)
insegnante = Insegnante("Marco", "Matematica")

stampa_dettagli(alunno)     # Output: Alunno: Giulia, Voto: 9.5
stampa_dettagli(insegnante) # Output: Insegnante: Marco, Materia: Matematica


class Persona (Insegnante, Alunno):

    def __init__(self, Insegnante ):
        self.nome = Insegnante.nome
        self.materia = Insegnante.materia

    def __init__(self, Studente ):
        self.nome = Studente.nome
        self.voto = Studente.voto

    def __init__(self):
        print("hai sbagliato")

persona3 = Persona()