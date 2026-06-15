# Improve the prediction accuracy by estimating the weight values for the training data using stochastic gradient descent.(Perceptron) 

import numpy as np

# Training data
X = np.array([
    [2, 3],
    [1, 1],
    [2, 1],
    [-1, -1],
    [-2, -1],
    [-3, -2]
])

# Target output
y = np.array([1, 1, 1, 0, 0, 0])

# Initialize weights and bias
w = np.zeros(2)
b = 0

# Hyperparameters
lr = 0.1
epochs = 10

# Step activation function
def activation(z):
    return 1 if z >= 0 else 0

print("Training using Stochastic Gradient Descent\n")

for epoch in range(epochs):
    correct = 0

    for i in range(len(X)):
        z = np.dot(X[i], w) + b
        y_pred = activation(z)

        error = y[i] - y_pred

        # SGD update
        w = w + lr * error * X[i]
        b = b + lr * error

        if y_pred == y[i]:
            correct += 1

        print(
            f"Epoch {epoch+1}, "
            f"Input: {X[i]}, "
            f"Target: {y[i]}, "
            f"Predicted: {y_pred}, "
            f"Error: {error}"
        )

    accuracy = correct / len(X) * 100

    print(f"\nEpoch {epoch+1} Accuracy: {accuracy:.2f}%")
    print("Weights:", w)
    print("Bias:", b)
    print("-" * 50)

print("\nFinal Weights:", w)
print("Final Bias:", b)

# Testing
print("\nTesting Final Model")

for i in range(len(X)):
    z = np.dot(X[i], w) + b
    y_pred = activation(z)

    print(f"Input: {X[i]} -> Predicted Output: {y_pred}")
    