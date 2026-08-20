# Unsupervised Clustering: K-Means vs DBSCAN
import numpy as np

def kmeans_scratch(data, k=2, max_iters=10):
    centroids = data[np.random.choice(len(data), k, replace=False)]
    for _ in range(max_iters):
        distances = np.abs(data[:, np.newaxis] - centroids)
        labels = np.argmin(distances, axis=1)
        new_centroids = np.array([data[labels == j].mean() if len(data[labels == j]) > 0 else centroids[j] for j in range(k)])
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return labels, centroids

mock_data = np.array([1.2, 1.5, 1.0, 5.0, 5.5, 4.8, 10.0, 10.5])
labels, centroids = kmeans_scratch(mock_data, k=3)
print("--- K-Means Clustering from Scratch (1D Data) ---")
print(f"Labels    : {labels}")
print(f"Centroids : {centroids}")
