from abc import ABC, abstractmethod

class computer(ABC):
    pass

class DispositivoInput(computer):
    @abstractmethod
    def leggi_input(self):
        """ Legge l'input dal dispositivo. """
        pass



class Tastiera(DispositivoInput):
    def leggi_input(self):
        print("Input dalla tastiera.")

class Mouse(DispositivoInput):
    def leggi_input(self):
        print("Click del mouse.")

# Uso delle classi
tastiera = Tastiera()
tastiera.leggi_input()

mouse = Mouse()
mouse.leggi_input()




from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def renderizza(self, oggetto):
        """ Renderizza un oggetto grafico. """
        pass

class Renderer2D(Renderer):
    def renderizza(self, oggetto):
        print(f"Renderizza {oggetto} in 2D.")

class Renderer3D(Renderer):
    def renderizza(self, oggetto):
        print(f"Renderizza {oggetto} in 3D.")

# Uso delle classi
renderer_2d = Renderer2D()
renderer_2d.renderizza('cerchio')

renderer_3d = Renderer3D()
renderer_3d.renderizza('cubo')



from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def paga(self, importo):
        """ Effettua un pagamento. """
        pass

class CartaCredito(MetodoPagamento):
    def paga(self, importo):
        print(f"Pagato {importo} con carta di credito.")

class PayPal(MetodoPagamento):
    def paga(self, importo):
        print(f"Pagato {importo} via PayPal.")

# Uso delle classi
carta = CartaCredito()
carta.paga(100)

paypal = PayPal()
paypal.paga(150)



