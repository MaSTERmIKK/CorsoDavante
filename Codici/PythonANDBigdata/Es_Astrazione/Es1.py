from abc import ABC, abstractmethod

class Veicolo(ABC):
    @abstractmethod
    def muovi(self):
       pass

class Auto(Veicolo):
    def muovi(self):
        print("L'auto si muove su quattro ruote.")

class Bicicletta(Veicolo):
    def muovi(self):
        print("La bicicletta si muove su due ruote.")

# Uso delle classi
auto = Auto()
auto.muovi()

bicicletta = Bicicletta()
bicicletta.muovi()







from abc import ABC, abstractmethod

class Notificatore(ABC):
    @abstractmethod
    def invia_notifica(self, messaggio):
        """ Invia una notifica con un messaggio. """
        pass

    def mirko(self):
        print("mirko")

    def __init__(self, nome, cognome) -> None:
        pass

class EmailNotificatore(Notificatore):


    def invia_notifica(self, messaggio):
        print(f"Inviando email con il messaggio: {messaggio}")

class SMSNotificatore(Notificatore):
    def invia_notifica(self, messaggio):
        print(f"Inviando SMS con il messaggio: {messaggio}")

def messaggiote(notificatoreo):
    notificatoreo.invia_notifica()


# Uso delle classi
notificatore_email = EmailNotificatore()
notificatore_email.invia_notifica('Ciao!')

notificatore_sms = SMSNotificatore()
notificatore_sms.invia_notifica('Buongiorno!')

messaggiote(notificatore_email)
messaggiote(notificatore_sms)