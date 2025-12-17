# Classi di base
class Volante:
    def vola(self):
        return "Sto volando"

class Nuotante:
    def nuota(self):
        return "Sto nuotando"

# Classe derivata con ereditarietà multipla
class Anatra(Volante, Nuotante):
    def fa_quack(self):
        return "Quack Quack"

# Polimorfismo con funzione che utilizza metodi delle classi base
def mostra_abilita(animale):
    if isinstance(animale, Volante):
        print(animale.vola())
    if isinstance(animale, Nuotante):
        print(animale.nuota())

anatra = Anatra()

# Utilizzo del polimorfismo
print(anatra.fa_quack())  # Output: Quack Quack
mostra_abilita(anatra)    # Output: Sto volando \n Sto nuotando


# Classi di base
class Madre(ABC):
    def saluto(self):
        return "Ciao dalla madre"

class Padre:
    def saluto(self):
        return "Ciao dal padre"

# Classe derivata con ereditarietà multipla
class Figlio(Madre, Padre):
    def saluto(self):
        return "Ciao dal figlio"

# Polimorfismo con funzione che chiama il metodo sovrascritto
def saluta(persona):
    print(persona.saluto())

#madre = Madre() Non si può istanziare una classe astratta 
padre = Padre()
figlio = Figlio()

# Utilizzo del polimorfismo
saluta(madre)  # Output: Ciao dalla madre
saluta(padre)  # Output: Ciao dal padre
saluta(figlio) # Output: Ciao dal figlio


#-------------------------------------------------------------------------

from abc import ABC, abstractmethod

# Classi di base
class MetodoDiPagamento(ABC):
    @abstractmethod
    def paga(self, amount):
        pass

class Sconto(ABC):
    @abstractmethod
    def calcola_sconto(self, amount):
        pass

# Implementazioni specifiche
class CartaDiCredito(MetodoDiPagamento):
    def paga(self, amount):
        return f"Pagamento di {amount}€ effettuato con Carta di Credito"

class PayPal(MetodoDiPagamento):
    def paga(self, amount):
        return f"Pagamento di {amount}€ effettuato con PayPal"

class ScontoFisso(Sconto):
    def calcola_sconto(self, amount):
        sconto = 5
        return max(amount - sconto, 0)

class ScontoPercentuale(Sconto):
    def calcola_sconto(self, amount):
        sconto = amount * 0.10
        return max(amount - sconto, 0)

# Classe derivata con ereditarietà multipla
class PagamentoConSconto(CartaDiCredito, ScontoFisso):
    def paga(self, amount):
        amount_scontato = self.calcola_sconto(amount)
        return super().paga(amount_scontato)

# Funzione di utilità
def processa_pagamento(metodo_pagamento, amount):
    print(metodo_pagamento.paga(amount))

# Esempio di utilizzo
pagamento = PagamentoConSconto()

processa_pagamento(pagamento, 100)  # Output: Pagamento di 95€ effettuato con Carta di Credito

# Altri esempi con combinazioni diverse
class PagamentoConPayPalEScontoPercentuale(PayPal, ScontoPercentuale):
    def paga(self, amount):
        amount_scontato = self.calcola_sconto(amount)
        return super().paga(amount_scontato)

pagamento_paypal_sconto = PagamentoConPayPalEScontoPercentuale()
processa_pagamento(pagamento_paypal_sconto, 200)  # Output: Pagamento di 180€ effettuato con PayPal







class StrumentoMusicale:
    def suona(self):
        pass  # Metodo che verrà sovrascritto dalle classi derivate

    def descrizione(self):
        return "Questo è uno strumento musicale."

class Chitarra(StrumentoMusicale):
    def suona(self):
        return "Strimpellio di chitarra."

    def descrizione(self):
        return "Questa è una chitarra."

class Pianoforte(StrumentoMusicale):
    def suona(self):
        return "Suono di pianoforte."

    def descrizione(self):
        return "Questo è un pianoforte."

class Batteria(StrumentoMusicale):
    def suona(self):
        return "Suono di batteria."

    def descrizione(self):
        return "Questa è una batteria."

class Orchestra:
    def __init__(self):
        self.strumenti = []

    def aggiungi_strumento(self, strumento):
        if isinstance(strumento, StrumentoMusicale):
            self.strumenti.append(strumento)
        else:
            print("L'oggetto aggiunto non è uno strumento musicale!")

    def suona_tutti(self):
        suoni = [strumento.suona() for strumento in self.strumenti]
        return "\n".join(suoni)

    def descrizione_tutti(self):
        descrizioni = [strumento.descrizione() for strumento in self.strumenti]
        return "\n".join(descrizioni)

# Creazione degli oggetti delle classi derivate
chitarra = Chitarra()
pianoforte = Pianoforte()
batteria = Batteria()

# Creazione dell'orchestra e aggiunta degli strumenti
orchestra = Orchestra()
orchestra.aggiungi_strumento(chitarra)
orchestra.aggiungi_strumento(pianoforte)
orchestra.aggiungi_strumento(batteria)

# Uso dei metodi polimorfici
print(orchestra.descrizione_tutti())
# Output:
# Questa è una chitarra.
# Questo è un pianoforte.
# Questa è una batteria.

print(orchestra.suona_tutti())
# Output:
# Strimpellio di chitarra.
# Suono di pianoforte.
# Suono di batteria.
