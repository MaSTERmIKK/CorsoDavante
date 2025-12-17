import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Generiamo dati casuali per due variabili
np.random.seed(0)  # Impostiamo il seed per riproducibilità
x = np.random.rand(100)
y = np.random.rand(100)

# Creiamo un grafico a dispersione
plt.scatter(x, y, color='green', marker='o')
plt.title('Grafico a dispersione')
plt.xlabel('Variabile X')
plt.ylabel('Variabile Y')
plt.grid(True)
plt.show()



# Generiamo dati casuali normalmente distribuiti
data = np.random.randn(1000)

# Creiamo un istogramma con 30 bins
plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title('Istogramma di dati casuali')
plt.xlabel('Valore')
plt.ylabel('Frequenza')
plt.show()


# Generiamo una matrice 10x10 di valori casuali
data = np.random.rand(10, 10)

# Creiamo una mappa di calore (heatmap)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.title('Mappa di calore')
plt.colorbar()  # Aggiungiamo una barra dei colori per indicare la scala
plt.show()
