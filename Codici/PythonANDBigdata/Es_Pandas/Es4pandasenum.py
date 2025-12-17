import numpy as np # type: ignore

# Creazione di un array 2D
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Selezione di un sotto-array
sotto_array = matrix[0:2, 1:3]  # Prende le prime due righe e le colonne 1 e 2

# Somma degli elementi per riga
somma_per_riga = np.sum(matrix, axis=1)

# Trasposizione della matrice
trasposta = matrix.T

print("Sotto-array:")
print(sotto_array)
print("Somma per riga:")
print(somma_per_riga)
print("Matrice trasposta:")
print(trasposta)
