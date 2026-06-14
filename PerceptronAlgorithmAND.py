# Implement Adaline algorithm for AND operation

import numpy as np

# Input for AND gate
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Target output for AND gate
y = np.array([0, 0, 0, 1])

# Initialize weights and bias
w = np.zeros(2)
b = 0

# Learning rate
lr = 0.1

# Training
for epoch in range(20):
    for i in range(len(X)):
        # Linear output
        y_in = np.dot(X[i], w) + b

        # Error calculation
        error = y[i] - y_in

        # ADALINE weight update rule
        w = w + lr * error * X[i]
        b = b + lr * error

# Final parameters
print("Final Weights:", w)
print("Final Bias:", b)

# Testing
print("\nTesting ADALINE for AND Operation:")

for i in range(len(X)):
    y_in = np.dot(X[i], w) + b

    # Threshold function
    y_pred = 1 if y_in >= 0.5 else 0

    print(X[i], "->", y_pred)