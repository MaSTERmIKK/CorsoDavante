# Classe base
class Animale:
    def __init__(self, nome):
        self._nome = nome  # Attributo protetto

    def _mangia(self):
        print("L'animale sta mangiando.")

    def emettere_suono(self):
        raise NotImplementedError("Metodo non implementato nella classe base")

# Sottoclasse che eredita da Animale
class Cane(Animale):
    def __init__(self, nome, razza):
        super().__init__(nome)  # Richiamo il costruttore della classe base
        self._razza = razza  # Attributo protetto

    def _mangia(self):
        print("Il cane sta mangiando.")

    def emettere_suono(self):
        print("Woof!")
        
class Cagnolone (Cane) :      
      def __init__(self, nome, razza, livello):
        super().__init__(nome,razza)
        self.livello = livello  
    
      def _mangia(self):
          super()._mangia(self) 
          print("mangia tanto!")
          
          
# Sottoclasse che eredita da Animale
class Gatto(Animale):
    def __init__(self, nome, colore):
        super().__init__(nome)  # Richiamo il costruttore della classe base
        self._colore = colore  # Attributo protetto

    def _mangia(self):
        print("Il gatto sta mangiando.")

    def emettere_suono(self):
        print("Meow!")
        
    def emettere_suono(self, versostrano = ""):
        print("Meow!" + versostrano)

# Funzione che utilizza il polimorfismo
def interagisci_con_animale(animale):
    animale.emettere_suono()  # Chiamata polimorfica al metodo emettere_suono

# Creazione di istanze delle sottoclassi
cane = Cane("Fido", "Labrador")
gatto = Gatto("Whiskers", "Arancione")
cagnone = Cagnolone("pippo", "cagnolone", True )

# Chiamata a metodi incapsulati tramite le sottoclassi
cane._mangia()
gatto._mangia()

gatto.emettere_suono()
gatto.emettere_suono("coffe")

# Chiamata a metodi polimorfici tramite la funzione interagisci_con_animale
interagisci_con_animale(cane)
interagisci_con_animale(gatto)
interagisci_con_animale(cagnone)




#---------------------------------------  Rifare il contesto sopra con due figli per figlio e due metodi genralizati "poliformici" per entrambi


















# Classe base
class Veicolo:
    def __init__(self, marca, modello):
        self._marca = marca  # Attributo protetto
        self._modello = modello  # Attributo protetto

    def accelerare(self):
        raise NotImplementedError("Metodo non implementato nella classe base")

# Sottoclassi che ereditano da Veicolo
class Auto(Veicolo):
    def accelerare(self):
        print("L'auto accelera rapidamente!")

class Moto(Veicolo):
    def accelerare(self):
        print("La moto accelera velocemente!")

# Funzione che utilizza il polimorfismo
def accelerazione_veicolo(veicolo):
    veicolo.accelerare()

# Creazione di istanze delle sottoclassi
auto = Auto("Fiat", "Punto")
moto = Moto("Honda", "CBR")

# Chiamata al metodo incapsulato attraverso le sottoclassi
auto.accelerare()
moto.accelerare()

# Chiamata al metodo polimorfico tramite la funzione accelerazione_veicolo
accelerazione_veicolo(auto)
accelerazione_veicolo(moto)