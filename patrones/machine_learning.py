from sklearn.cluster import KMeans
import numpy as np

datos = np.array([[1, 2], [1, 4], [1, 0],
                  [10, 2], [10, 4], [10, 0]])

kmeans = KMeans(n_clusters=2)
kmeans.fit(datos)

print("Centroides:", kmeans.cluster_centers_)
print("Etiquetas:", kmeans.labels_)
