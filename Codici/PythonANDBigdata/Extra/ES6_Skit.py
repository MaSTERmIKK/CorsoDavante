from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Generazione di dati bidimensionali
np.random.seed(42)
X = np.vstack([
    np.random.randn(50, 2) + np.array([2, 2]),
    np.random.randn(50, 2) + np.array([-2, -2]),
    np.random.randn(50, 2) + np.array([5, -3])
])

# Creazione e addestramento del modello K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Visualizzazione dei cluster
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.6, label='Punti')
plt.scatter(centroids[:, 0], centroids[:, 1], color='red', marker='x', s=200, label='Centroidi')
plt.title('Clusterizzazione con K-Means')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

