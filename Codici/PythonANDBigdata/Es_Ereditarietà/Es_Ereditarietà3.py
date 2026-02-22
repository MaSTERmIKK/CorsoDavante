class Schedamadre():
    
    core = 4
    
    def __init__(self, nomeSchedamadre):
        self.nomeSchedamadre = nomeSchedamadre
        
    def saluta(self, saluto):
        return ("ti dico ", saluto," e ho questo nome: ", self.nomeSchedamadre)
           
        
class Processore(Schedamadre):
    
    def __init__(self, nomeSchedamadre, nomeProcessore):
        super().__init__(nomeSchedamadre)
        self.nomeProcessore = nomeProcessore
        
    def processora(self):
        print ("sto processando")
        
    def saluta(self, saluto):
        frase = super().saluta(saluto)    
        frase2 = " io ho anche " + self.nomeProcessore
        return (frase, frase2 )
    
    
intel4 = Processore("gold 6", "pippoprocessor")

intel4.processora()
print("--------------------------------")
print(intel4.saluta("heila"))
print("--------------------------------")


class Nonno():
    def __init__(self):
        pass


class Padre1 (Nonno):
    
    def __init__(self):
        pass
    
    def saluta1 (self):
        print(1)
    
class Padre2 (Nonno):
    
    def __init__(self):
        pass
    
    def saluta2 (self):
        print(2)
        
        

class FiglioCongiunto (Padre1, Padre2):
    
    def __init__(self):
        Padre1.__init__(self)
        Padre2.__init__(self)
        
    def salutoUnitario(self):
        super().saluta1()
        super().saluta2()
        
Gianni = FiglioCongiunto()

Gianni.salutoUnitario()


class BaseComponenti():
    def __init__(self):
        pass
    
    def saluta( self, saluto ):
        print(saluto)

class Componente1(BaseComponenti):
    def __init__(self):
        pass
    
class Componente2(BaseComponenti):
    def __init__(self):
        pass
    
class Componente3(BaseComponenti):
    def __init__(self):
        pass
    
class OggettoComposito():
    
    def __init__(self, Componente3, Componente2, Componente1):
        self.Componente3 = Componente3
        self.Componente2 = Componente2
        self.Componente1 = Componente1
        
    def saluta(self, saluto):
        self.Componente1.saluta(saluto)
        
x1 = Componente1()
x2 = Componente2()
x3 = Componente3()

oggComp = OggettoComposito(x3,x2,x1)

oggComp.saluta("ciao")