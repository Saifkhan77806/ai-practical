# Implementation of Classifying Data using Support Vector Machine (SVM)

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load dataset
data = load_breast_cancer()

# Use first two features
X = data.data[:, :2]

# Target labels
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Create SVM model
model = SVC(kernel='linear')

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Output
print("Predicted Output:")
print(y_pred)

print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))