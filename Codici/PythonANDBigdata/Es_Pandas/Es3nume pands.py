import pandas as pd # type: ignore
import numpy as np # type: ignore

# Creazione di un DataFrame con dati casuali utilizzando NumPy
np.random.seed(42)  # Per ottenere sempre lo stesso risultato casuale
data = np.random.randint(1, 100, size=(5, 3))

# Conversione in DataFrame Pandas
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# Applicazione di una funzione NumPy al DataFrame
df['Somma'] = np.sum(df, axis=1)  # Somma per riga
df['Media'] = np.mean(df[['A', 'B', 'C']], axis=1)  # Media delle colonne A, B, C

print(df)


import pandas as pd # type: ignore

# Creazione di due DataFrame
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Nome': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Età': [24, 27, 35]
})

# Merge (join) dei DataFrame sulla colonna 'ID'
df_merged = pd.merge(df1, df2, on='ID', how='inner')

print(df_merged)
