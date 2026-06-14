# Implementation of Boosting Algorithms – AdaBoost, Stochastic Gradient Boosting, and Voting Ensemble

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    VotingClassifier,
    RandomForestClassifier
)

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# --------------------------------
# AdaBoost
# --------------------------------
ada = AdaBoostClassifier(
    n_estimators=50,
    learning_rate=1.0,
    random_state=42
)

ada.fit(X_train, y_train)

ada_pred = ada.predict(X_test)

# --------------------------------
# Stochastic Gradient Boosting
# --------------------------------
sgb = GradientBoostingClassifier(
    n_estimators=100,
    subsample=0.8,
    random_state=42
)

sgb.fit(X_train, y_train)

sgb_pred = sgb.predict(X_test)

# --------------------------------
# Voting Ensemble
# --------------------------------
lr = LogisticRegression(max_iter=200)

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

svm = SVC(
    probability=True,
    random_state=42
)

voting = VotingClassifier(
    estimators=[
        ('lr', lr),
        ('rf', rf),
        ('svm', svm)
    ],
    voting='soft'
)

voting.fit(X_train, y_train)

vote_pred = voting.predict(X_test)

# --------------------------------
# Results
# --------------------------------
print("AdaBoost Accuracy:")
print(accuracy_score(y_test, ada_pred))

print("\nStochastic Gradient Boosting Accuracy:")
print(accuracy_score(y_test, sgb_pred))

print("\nVoting Ensemble Accuracy:")
print(accuracy_score(y_test, vote_pred))