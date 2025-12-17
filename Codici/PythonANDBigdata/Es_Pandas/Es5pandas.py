import pandas as pd # type: ignore
import numpy as np # type: ignore

# Creazione di un DataFrame
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
    'Materia': ['Matematica', 'Fisica', 'Matematica', 'Fisica', 'Matematica'],
    'Voto': [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)

# Raggruppamento dei dati per Nome e Materia
gruppo = df.groupby(['Nome', 'Materia']).mean()  # Calcolo della media dei voti

# Resetta l'indice per ottenere un DataFrame pulito
gruppo_reset = gruppo.reset_index()

print(gruppo_reset)



# Creazione di un DataFrame con valori NaN (dati mancanti)
data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
}

df = pd.DataFrame(data)

# Riempire i valori NaN con la media della colonna (usando NumPy)
df['A'].fillna(np.mean(df['A']), inplace=True)
df['B'].fillna(np.mean(df['B']), inplace=True)

# Eliminare le righe che contengono ancora valori mancanti
df_clean = df.dropna()

print(df)
print(df_clean)