from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import numpy as np

# Generazione dati sintetici
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # 100 campioni, 1 feature
y = 2.5 * X.flatten() + np.random.randn(100) * 2  # y = 2.5x + rumore

# Suddivisione in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creazione e addestramento del modello
model = LinearRegression()
model.fit(X_train, y_train)

# Previsione e calcolo del punteggio R²
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

print(f"Punteggio R²: {r2:.2f}")
