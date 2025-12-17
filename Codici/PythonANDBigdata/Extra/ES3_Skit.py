from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LinearRegression
import numpy as np

# Generazione dati sintetici
np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 3 * X.flatten() + np.random.randn(100) * 3

# Creazione del modello
model = LinearRegression()

# Validazione incrociata K-Fold
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, scoring='r2', cv=kf)

print(f"Punteggio medio R²: {scores.mean():.2f}")
print(f"Deviazione standard R²: {scores.std():.2f}")
