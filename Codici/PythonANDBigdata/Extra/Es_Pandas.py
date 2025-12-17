"""
Panoramica pratica di pandas:
- Series e DataFrame
- Indicizzazione, selezione, filtri
- Operazioni su colonne e missing data
- GroupBy e aggregazioni
- Merge / Join
- DateTime e resampling
- I/O essenziali (CSV)
- Statistiche descrittive e plot veloce
"""
import pandas as pd
import numpy as np

# =================================================================
# 1. CREAZIONE DI SERIES E DATAFRAME
# =================================================================

s = pd.Series([4, 7, -5, 3], name="esempio_series")
df = pd.DataFrame({
    "A": np.arange(1, 5),
    "B": pd.date_range("2025-01-01", periods=4, freq="D"),
    "C": ["rosso", "verde", "blu", "giallo"],
    "D": np.random.randn(4)
})
print("=== Series e DataFrame ===")
print(s)
print(df, "\n")

# =================================================================
# 2. INDICIZZAZIONE, SELEZIONE, FILTRI
# =================================================================

print("=== Selezione e filtri ===")
print("df['A']          -> colonna:\n", df["A"])
print("df.loc[1, 'C']   -> riga 1, colonna 'C':", df.loc[1, "C"])
print("df.iloc[0:2, 0:2] -> slicing posizionale:\n", df.iloc[0:2, 0:2])

filtro = df["D"] > 0
print("Righe con D > 0:\n", df[filtro], "\n")

# =================================================================
# 3. OPERAZIONI SU COLONNE & MISSING DATA
# =================================================================

df["E"] = df["A"] * 10                # nuova colonna derivata
df.loc[2, "E"] = np.nan               # introduciamo un NaN
print("=== Colonna derivata & NaN ===")
print(df)

print("\nConta NaN per colonna:\n", df.isna().sum())
df["E"].fillna(df["E"].mean(), inplace=True)  # imputazione semplice
print("Dopo fillna sulla colonna E:\n", df, "\n")

# =================================================================
# 4. GROUPBY E AGGREGAZIONI
# =================================================================

print("=== GroupBy e aggregazioni ===")
df["gruppo"] = ["x", "x", "y", "y"]
agg = df.groupby("gruppo")["E"].agg(["count", "mean", "max"])
print(agg, "\n")

# =================================================================
# 5. MERGE / JOIN
# =================================================================

print("=== Merge / Join ===")
left = pd.DataFrame({"id": [1, 2, 3], "val": ["a", "b", "c"]})
right = pd.DataFrame({"id": [2, 3, 4], "descr": ["uno", "due", "tre"]})
merged = left.merge(right, on="id", how="outer")
print(merged, "\n")

# =================================================================
# 6. DATE-TIME, INDEX & RESAMPLING
# =================================================================

print("=== DateTime e resampling ===")
rng = pd.date_range("2025-03-01", periods=120, freq="H")  # 5 giorni di dati orari
ts = pd.Series(np.random.randn(len(rng)), index=rng, name="temperatura")
giornaliero = ts.resample("D").mean()
print("Serie oraria (head):\n", ts.head())
print("Resample giornaliero (media):\n", giornaliero, "\n")

# =================================================================
# 7. I/O ESSENZIALI
# =================================================================

print("=== I/O: salvataggio CSV temporaneo ===")
# Salva e ricarica rapidamente in memoria (StringIO) solo come demo
from io import StringIO
buffer = StringIO()
df.to_csv(buffer, index=False)
buffer.seek(0)
df_loaded = pd.read_csv(buffer)
print("Caricato da CSV:\n", df_loaded, "\n")

# =================================================================
# 8. STATISTICHE DESCRITTIVE & QUICK PLOT*
# =================================================================

print("=== Statistiche descrittive ===")
print(df.describe(include='all'), "\n")

# *Plot rapido (richiede matplotlib). Verrà mostrato solo se esegui in ambiente con GUI:
if __name__ == "__main__":
    try:
        import matplotlib.pyplot as plt
        df["E"].plot(kind="bar", title="Colonna E (dopo imputazione)")
        plt.tight_layout()
        plt.show()
    except ImportError:
        print("matplotlib non disponibile: plot saltato.")
