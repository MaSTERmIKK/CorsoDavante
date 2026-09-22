import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creazione degli array NumPy con le vendite
prodotto_a = np.array([120, 150, 135, 170, 190, 210])
prodotto_b = np.array([100, 110, 140, 130, 160, 180])
prodotto_c = np.array([80, 120, 115, 150, 145, 170])

# Creazione dei mesi
mesi = [
    "Gennaio",
    "Febbraio",
    "Marzo",
    "Aprile",
    "Maggio",
    "Giugno"
]

# Creazione del DataFrame
df = pd.DataFrame({
    "Prodotto A": prodotto_a,
    "Prodotto B": prodotto_b,
    "Prodotto C": prodotto_c
}, index=mesi)

# Calcolo del totale delle vendite per prodotto
totali_prodotti = df.sum()

# Calcolo della media delle vendite per prodotto
medie_prodotti = df.mean()

# Ricerca del prodotto con il totale maggiore
prodotto_migliore = totali_prodotti.idxmax()

# Aggiunta del totale mensile
df["Totale_Mese"] = df[
    ["Prodotto A", "Prodotto B", "Prodotto C"]
].sum(axis=1)

# Stampa del DataFrame
print(df)

# Stampa dei totali
print("\nTotali per prodotto:")
print(totali_prodotti)

# Stampa delle medie
print("\nMedie per prodotto:")
print(medie_prodotti)

# Stampa del prodotto con più vendite
print("\nProdotto con più vendite:", prodotto_migliore)

# Grafico a linee del Prodotto A
plt.plot(
    mesi,
    prodotto_a,
    marker="o",
    label="Prodotto A"
)

# Grafico a linee del Prodotto B
plt.plot(
    mesi,
    prodotto_b,
    marker="o",
    label="Prodotto B"
)

# Grafico a linee del Prodotto C
plt.plot(
    mesi,
    prodotto_c,
    marker="o",
    label="Prodotto C"
)

# Titolo e assi
plt.title("Andamento mensile delle vendite")
plt.xlabel("Mese")
plt.ylabel("Vendite")

# Visualizzazione della legenda
plt.legend()

# Rotazione dei mesi
plt.xticks(rotation=45)

# Sistemazione degli spazi
plt.tight_layout()

# Visualizzazione del grafico
plt.show()

# Creazione del grafico a barre
totali_prodotti.plot(kind="bar")

# Titolo e assi
plt.title("Vendite totali per prodotto")
plt.xlabel("Prodotto")
plt.ylabel("Vendite totali")

# Sistemazione degli spazi
plt.tight_layout()

# Visualizzazione del grafico
plt.show()