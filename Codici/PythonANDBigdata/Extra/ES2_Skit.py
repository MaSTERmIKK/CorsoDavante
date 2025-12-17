from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Caricamento del dataset Iris
iris = load_iris()
X, y = iris.data, iris.target

# Suddivisione in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creazione e addestramento del modello SVM
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Previsione e calcolo dell'accuratezza
y_pred = svm_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuratezza: {accuracy:.2f}")
