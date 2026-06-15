# Implementation of Logistic regression

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=4
)

# Create Logistic Regression model
logreg = LogisticRegression(max_iter=200)

# Train model
logreg.fit(X_train, y_train)

# Predict on test data
y_pred = logreg.predict(X_test)

# Display predictions
print("Predicted Output:")
print(y_pred)

# Accuracy
print("\nAccuracy:")
print(metrics.accuracy_score(y_test, y_pred))
