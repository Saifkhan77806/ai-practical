# Implement Perceptron algorithm for OR operation 

import numpy as np

# Input for OR gate
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Target output for OR gate
y = np.array([0, 1, 1, 1])

# Initialize weights and bias
w = np.zeros(2)
b = 0

# Learning rate
lr = 0.1

# Training
for epoch in range(10):
    print(f"Epoch {epoch + 1}")

    for i in range(len(X)):
        z = np.dot(X[i], w) + b
        y_pred = 1 if z >= 0 else 0

        # Update weights and bias
        w = w + lr * (y[i] - y_pred) * X[i]
        b = b + lr * (y[i] - y_pred)

        print(
            f"Input: {X[i]}, "
            f"Target: {y[i]}, "
            f"Predicted: {y_pred}, "
            f"Weights: {w}, "
            f"Bias: {b}"
        )

    print()

print("Final Weights:", w)
print("Final Bias:", b)

# Testing
print("\nTesting Perceptron for OR Operation:")

for i in range(len(X)):
    z = np.dot(X[i], w) + b
    y_pred = 1 if z >= 0 else 0
    print(f"{X[i]} -> {y_pred}")