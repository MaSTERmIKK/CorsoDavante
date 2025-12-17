

class Persona :
   
    tipo = "umano"                     # attributi 
    
    # Metodi
    
    def __init__(self, Nome, Eta):     # costruttore 
        self.Nome = Nome
        self.Eta = Eta
    
    def MasterD(self):                 # Metodo della classe
        print( " ciao sono " + self.Nome + " " + self.tipo)
        


X = Persona("Mirko", 99)
X.MasterD()

class Alievo(Persona):
    
    def __init__(self, Nome, Eta, grado):
        super().__init__(Nome, Eta)
        self.grado = grado
    
    tipo = "gatto"
    
    def MasterD(self):                 # Metodo della classe
        print( " ciao sono " + self.Nome + " " + self.tipo + " " + self.grado)

Y = Alievo("Marius", 23, "TERZO DAN")
Y.MasterD()
