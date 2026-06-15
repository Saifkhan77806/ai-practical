# Introduction to Python Programming: Learn the different libraries - NumPy, Pandas, SciPy, Matplotlib, Scikit Learn

import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# NumPy

print("----- NumPy -----")
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# Pandas Series
print("\n----- Pandas Series -----")
ser = pd.Series(['g', 'e', 'e', 'k', 's'])
print(ser)

# Pandas DataFrame
print("\n----- Pandas DataFrame -----")
df = pd.DataFrame({
    'Name': ['Asha', 'Ravi', 'Neha'],
    'Roll': [1, 2, 3]
})
print(df)

# SciPy
print("\n----- SciPy -----")
print("SciPy version:", scipy.__version__)

# Scikit-learn
print("\n----- Scikit-learn -----")
iris = load_iris()

print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)
print("First 5 rows:\n", iris.data[:5])

# Matplotlib
print("\n----- Matplotlib Graph -----")

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Simple Line Graph")
plt.show()
