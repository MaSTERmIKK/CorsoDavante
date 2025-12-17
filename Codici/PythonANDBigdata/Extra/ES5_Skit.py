from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Generazione di un dataset sintetico
X, y = make_classification(n_samples=100, n_features=4, n_classes=2, random_state=42)

# Suddivisione in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creazione e addestramento dell'albero decisionale
tree_model = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_model.fit(X_train, y_train)

# Previsione e calcolo dell'accuratezza
y_pred = tree_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza: {accuracy:.2f}")

# Visualizzazione dell'albero decisionale
plt.figure(figsize=(12, 8))
plot_tree(tree_model, feature_names=[f'Feature {i}' for i in range(X.shape[1])], class_names=['Classe 0', 'Classe 1'], filled=True)
plt.show()
