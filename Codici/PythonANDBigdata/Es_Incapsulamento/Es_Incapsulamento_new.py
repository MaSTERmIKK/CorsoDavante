class Gestore_CartaCred ():
    def __init__(self, titolare = "placeholder", codicePin = 000):
        self.__titolare = titolare
        self.__codice_pin = codicePin
        self.__numero_utilizzi = 0
        
    @property
    def titolare(self):
        if  self.__titolare == "placeholder" :
            raise ValueError("non può accedere al dato")
        return self.__titolare 
        
    @titolare.setter
    def set_titolare(self, nuovo_titotlare):
        if nuovo_titotlare == "placeholder" and nuovo_titotlare == "":
            raise ValueError("non può essere placeholder il titolare ne vuoto")
        self.__titolare = nuovo_titotlare
        
card = Gestore_CartaCred( "mirko", 2025 )

print(card.titolare) 
        
        