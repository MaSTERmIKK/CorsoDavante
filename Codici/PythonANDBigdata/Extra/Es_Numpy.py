
"""
Panoramica pratica di NumPy:
- Creazione di array e proprietà di base
- Indicizzazione, slicing e mascheramento
- Broadcasting e funzioni universali (ufunc)
- Operazioni di aggregazione
- Uso del modulo random di NumPy
- Reshape e concatenazione
- Algebra lineare (dot, inv, eig)
- Interoperabilità con liste Python
"""

import numpy as np # type: ignore

# ==============================================================
# 1. CREAZIONE DI ARRAY E PROPRIETÀ DI BASE
# ==============================================================

a1 = np.array([1, 2, 3])              # array 1‑D da lista
a2 = np.arange(0, 10, 2)              # array 1‑D con step 2
a3 = np.linspace(0, 1, 5)             # 5 punti equidistanti tra 0 e 1
m1 = np.zeros((2, 3), dtype=int)      # matrice 2×3 di zeri
m2 = np.ones((3, 3)) * 7              # matrice 3×3 piena di 7
m3 = np.eye(4)                        # matrice identità 4×4
rand = np.random.random((2, 4))       # matrice 2×4 di float uniformi [0,1)

print("=== Creazione e proprietà ===")
for arr in [a1, a2, a3, m1, m2, m3]:
    print(f"{arr}\n  shape={arr.shape},  dtype={arr.dtype},  ndim={arr.ndim}")
print()

# ==============================================================
# 2. INDICIZZAZIONE, SLICING, MASCHERAMENTO
# ==============================================================

print("=== Indicizzazione & slicing ===")
b = np.arange(10)         # [0 1 2 3 4 5 6 7 8 9]
print("b[3] =", b[3])     # singolo elemento
print("b[2:7:2] =", b[2:7:2])  # slice con step
b[0:3] = 100              # assegnazione a slice (broadcast su slice)
print("b dopo assegnazione slice:", b)

# Mascheramento booleano
mask = b > 5
print("mask =", mask)
print("b[mask] =", b[mask])   # elementi > 5
print()

# ==============================================================
# 3. BROADCASTING & UFUNC
# ==============================================================

print("=== Broadcasting & funzioni universali ===")
x = np.array([[1, 2, 3],
              [4, 5, 6]])
y = np.array([10, 20, 30])    # shape (3,)
print("x + y  -> broadcasting colonna‑per‑riga:\n", x + y)
print("np.sqrt(x) -> radice quadrata element‑wise:\n", np.sqrt(x))
print()

# ==============================================================
# 4. AGGREGAZIONI
# ==============================================================

print("=== Aggregazioni ===")
print("x.sum() =", x.sum())
print("x.mean(axis=0) (media colonne) =", x.mean(axis=0))
print("x.max(axis=1)  (max righe) =", x.max(axis=1))
print()

# ==============================================================
# 5. NUMPY RANDOM
# ==============================================================

print("=== NumPy Random ===")
np.random.seed(42)                       # riproducibilità
samples = np.random.normal(loc=0, scale=1, size=5)
print("Campioni normali N(0,1):", samples)
perm = np.random.permutation(10)         # permutazione casuale
print("Permutazione 0‑9:", perm)
print()

# ==============================================================
# 6. RESHAPE, CONCATENAZIONE, SPLIT
# ==============================================================

print("=== Reshape & concatenazione ===")
c = np.arange(12).reshape(3, 4)          # 3×4
d = c.reshape(4, 3).T                    # trasposizione rapida
print("c:\n", c)
print("d (reshape + T):\n", d)

h_stack = np.hstack([c, c])              # concat orizzontale
v_stack = np.vstack([c, c])              # concat verticale
print("hstack shape:", h_stack.shape)
print("vstack shape:", v_stack.shape)
print()

# ==============================================================
# 7. ALGEBRA LINEARE
# ==============================================================

print("=== Algebra lineare ===")
A = np.array([[3, 1],
              [2, 4]])
b_vec = np.array([9, 8])
sol = np.linalg.solve(A, b_vec)          # risolve Ax = b
print("Soluzione sistema lineare x:", sol)

eigvals, eigvecs = np.linalg.eig(A)
print("Autovalori:", eigvals)
print("Autovettori:\n", eigvecs)
print("A·eigvec ≈ eigval*eigvec:\n", A @ eigvecs[:, 0],
      "\n", eigvals[0] * eigvecs[:, 0])
print()

# ==============================================================
# 8. INTEROPERABILITÀ LISTE ↔️ NUMPY
# ==============================================================

print("=== Interoperabilità Python list / NumPy ===")
py_list = [10, 20, 30]
np_arr = np.array(py_list)
print("Da lista a array:", np_arr, "| tipo:", type(np_arr))

back_to_list = np_arr.tolist()
print("Da array a lista:", back_to_list, "| tipo:", type(back_to_list))
