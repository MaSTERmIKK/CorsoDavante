from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Caricamento del dataset Iris
iris = load_iris()
X, y = iris.data, iris.target

# Applicazione di PCA per ridurre le dimensioni a 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Visualizzazione dei risultati
plt.figure(figsize=(8, 6))
for class_label in set(y):
    plt.scatter(X_pca[y == class_label, 0], X_pca[y == class_label, 1], label=f'Classe {class_label}')

plt.title('PCA su Iris Dataset')
plt.xlabel('Componente Principale 1')
plt.ylabel('Componente Principale 2')
plt.legend()
plt.show()
