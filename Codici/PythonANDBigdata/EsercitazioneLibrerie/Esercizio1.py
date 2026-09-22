import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creazione dell'array NumPy con le temperature
lista_temperature = [18, 20, 22, 21, 25, 24, 19]
temperature = np.array(lista_temperature)  #([18, 20, 22, 21, 25, 24, 19]) è la stessa cosa

# Creazione dei giorni della settimana
giorni = [
    "Lunedì",
    "Martedì",
    "Mercoledì",
    "Giovedì",
    "Venerdì",
    "Sabato",
    "Domenica"
]

# Creazione del DataFrame Pandas
dizionario_temp= {
    "Giorno": giorni,
    "Temperatura": temperature
}

df = pd.DataFrame( dizionario_temp )

# Calcolo della temperatura media
media = df["Temperatura"].mean()

# Calcolo della temperatura minima
minima = df["Temperatura"].min()

# Calcolo della temperatura massima
massima = df["Temperatura"].max()

# Stampa del DataFrame
print(df)

# Stampa dei risultati
print("Temperatura media:", media)
print("Temperatura minima:", minima)
print("Temperatura massima:", massima)

# Creazione del grafico a linee
plt.plot(
    df["Giorno"],
    df["Temperatura"],
    marker="o"
)

# Titolo del grafico
plt.title("Temperature settimanali")

# Nome degli assi
plt.xlabel("Giorno")
plt.ylabel("Temperatura")

# Rotazione dei nomi dei giorni
plt.xticks(rotation=45)

# Sistemazione automatica degli spazi
plt.tight_layout()

# Visualizzazione del grafico
plt.show()