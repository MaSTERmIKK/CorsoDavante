import pandas as pd # type: ignore

# Creazione di un DataFrame da un dizionario
data = {
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Età': [24, 27, 22],
    'Città': ['Milano', 'Roma', 'Torino']
}

df = pd.DataFrame(data)

# Selezione di una singola colonna
nomi = df['Nome']
eta_media = df['Età'].mean()

# Aggiunta di una nuova colonna calcolata
df['Anni Fino a 30'] = 30 - df['Età']

# Filtraggio delle righe dove l'età è maggiore di 23
filtrato = df[df['Età'] > 23]

print(df)
print(filtrato)
