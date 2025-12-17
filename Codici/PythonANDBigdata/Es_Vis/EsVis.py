import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Generiamo 100 punti lineari tra 0 e 2π
x = np.linspace(0, 2 * np.pi, 100)
# Calcoliamo il seno di ogni punto
y = np.sin(x)

# Creiamo il grafico della sinusoide
plt.plot(x, y)
plt.title('Grafico di una sinusoide')
plt.xlabel('Angolo [radiani]')
plt.ylabel('Ampiezza')
plt.grid(True)
plt.show()



# Definiamo le categorie e i valori associati
categorie = ['A', 'B', 'C', 'D']
valori = [10, 15, 7, 12]

# Creiamo un grafico a barre
plt.bar(categorie, valori, color='skyblue')
plt.title('Grafico a barre')
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.show()




# Definiamo le etichette e le dimensioni per ogni sezione
etichette = ['Mele', 'Banane', 'Ciliegie', 'Arance']
dimensioni = [30, 25, 20, 25]

# Creiamo un grafico a torta
plt.pie(dimensioni, labels=etichette, autopct='%1.1f%%', startangle=90)
plt.title('Distribuzione della frutta')
plt.axis('equal')  # Assicura che il grafico sia un cerchio
plt.show()
