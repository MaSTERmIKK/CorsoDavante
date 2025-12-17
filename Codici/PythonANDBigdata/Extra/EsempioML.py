# Esempio di Machine Learning generale con scikit-learn

# Importazione delle librerie necessarie
from sklearn.datasets import load_iris  # Dataset di esempio incluso in scikit-learn
from sklearn.model_selection import train_test_split  # Per dividere il dataset in training e test
from sklearn.preprocessing import StandardScaler  # Per standardizzare le caratteristiche
from sklearn.tree import DecisionTreeClassifier  # Modello di classificazione
from sklearn.metrics import accuracy_score  # Per valutare le prestazioni del modello

# 1. Raccolta dei dati
# In questo caso, utilizziamo il dataset Iris, un classico dataset per problemi di classificazione
iris = load_iris()
X = iris.data  # Matrice delle caratteristiche (Features)
y = iris.target  # Vettore delle etichette (Labels)

# 2. Pre-elaborazione dei dati
# La pre-elaborazione può includere la pulizia dei dati, la gestione dei valori mancanti e la standardizzazione
# Standardizziamo le caratteristiche per avere media=0 e deviazione standard=1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Divisione del dataset
# Dividiamo il dataset in set di training e di test per valutare le prestazioni del modello su dati non visti
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 4. Selezione e creazione del modello
# Scegliamo un algoritmo di Machine Learning adatto; in questo caso, un albero di decisione
model = DecisionTreeClassifier(random_state=42)

# 5. Addestramento del modello
# Il modello apprende dai dati di training trovando pattern e relazioni nei dati
model.fit(X_train, y_train)

# 6. Predizione sui dati di test
# Utilizziamo il modello addestrato per fare previsioni sulle caratteristiche del set di test
y_pred = model.predict(X_test)

# 7. Valutazione del modello
# Confrontiamo le predizioni con le etichette reali per valutare l'accuratezza del modello
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza del modello: {accuracy * 100:.2f}%")

# 8. Interpretazione dei risultati
# Un'accuratezza elevata indica che il modello è efficace nel generalizzare su nuovi dati
