from abc import ABC, abstractmethod

class DispositivoElettronico(ABC):
    @abstractmethod
    def accendi(self):
        pass

    @abstractmethod
    def spegni(self):
        pass

class ConnettivitaBluetooth(ABC):
    @abstractmethod
    def connetti_bluetooth(self):
        pass

class Smartphone(DispositivoElettronico, ConnettivitaBluetooth):
    def accendi(self):
        print("Smartphone acceso.")

    def spegni(self):
        print("Smartphone spento.")

    def connetti_bluetooth(self):
        print("Connessione Bluetooth attivata sullo smartphone.")

class Laptop(DispositivoElettronico, ConnettivitaBluetooth):
    def accendi(self):
        print("Laptop acceso.")

    def spegni(self):
        print("Laptop spento.")

    def connetti_bluetooth(self):
        print("Connessione Bluetooth attivata sul laptop.")

# Uso delle classi
smartphone = Smartphone()
laptop = Laptop()

smartphone.accendi()
smartphone.connetti_bluetooth()
smartphone.spegni()

laptop.accendi()
laptop.connetti_bluetooth()
laptop.spegni()







from abc import ABC, abstractmethod

class CanaleNotifica(ABC):
    @abstractmethod
    def invia_notifica(self, messaggio):
        pass

class NotificaEmail(CanaleNotifica):
    def invia_notifica(self, messaggio):
        print(f"Invio email: {messaggio}")

class NotificaSMS(CanaleNotifica):
    def invia_notifica(self, messaggio):
        print(f"Invio SMS: {messaggio}")

class NotificaApp(CanaleNotifica):
    def invia_notifica(self, messaggio):
        print(f"Invio notifica app: {messaggio}")

class GestoreNotifiche:
    def __init__(self, canali):
        self.canali = canali

    def invia_tutti(self, messaggio):
        for canale in self.canali:
            canale.invia_notifica(messaggio)

# Uso del sistema di notifiche
canali = [NotificaEmail(), NotificaSMS(), NotificaApp()]
gestore = GestoreNotifiche(canali)
gestore.invia_tutti("Benvenuto al nostro servizio!")

