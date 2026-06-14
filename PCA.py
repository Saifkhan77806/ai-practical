# Implementation of Features Extraction and Selection, Normalization, Transformation, Principal Components Analysis.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.decomposition import PCA

# Load Iris Dataset
iris = load_iris()

X = iris.data
y = iris.target
feature_names = iris.feature_names

print("Original Shape:", X.shape)

# -----------------------------
# Feature Selection
# -----------------------------
selector = SelectKBest(score_func=f_classif, k=2)

X_selected = selector.fit_transform(X, y)

selected_features = np.array(feature_names)[selector.get_support()]

print("\nSelected Features:")
print(selected_features)

print("Shape after Feature Selection:", X_selected.shape)

# -----------------------------
# Normalization
# -----------------------------
scaler = MinMaxScaler()

X_normalized = scaler.fit_transform(X)

print("\nNormalized Data (First 5 Rows):")
print(X_normalized[:5])

# -----------------------------
# Standardization
# -----------------------------
std_scaler = StandardScaler()

X_standardized = std_scaler.fit_transform(X)

# -----------------------------
# PCA
# -----------------------------
pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_standardized)

print("\nPCA Transformed Shape:", X_pca.shape)

print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

# -----------------------------
# Correlation Matrix Heatmap
# -----------------------------
cov_data = np.corrcoef(X.T)

plt.figure(figsize=(7, 6))

img = plt.matshow(
    cov_data,
    cmap=plt.cm.rainbow,
    fignum=1
)

plt.colorbar(
    img,
    ticks=[-1, 0, 1],
    fraction=0.045
)

for i in range(cov_data.shape[0]):
    for j in range(cov_data.shape[1]):
        plt.text(
            j,
            i,
            f"{cov_data[i, j]:.2f}",
            ha="center",
            va="center",
            color="black"
        )

plt.title("Correlation Matrix Heatmap", pad=20)
plt.show()

# -----------------------------
# PCA Scatter Plot
# -----------------------------
plt.figure(figsize=(8, 6))

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=y
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA of Iris Dataset")

plt.show()