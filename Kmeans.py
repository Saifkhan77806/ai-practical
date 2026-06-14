# Implement Elbow Method for K-Means Clustering

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load Iris Dataset
iris = load_iris()

X = iris.data

# Calculate WCSS for different K values
wcss = []

for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        init='k-means++',
        random_state=42,
        n_init=10
    )

    kmeans.fit(X)

    wcss.append(kmeans.inertia_)

print("WCSS Values:")
print(wcss)

# Plot Elbow Graph
plt.plot(range(1, 11), wcss, marker='o')

plt.title('Elbow Method for K-Means')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')

plt.show()