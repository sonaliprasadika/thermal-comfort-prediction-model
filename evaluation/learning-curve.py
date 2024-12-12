from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split

scaler_path = "../models/scaler.pkl"

scaler = joblib.load(scaler_path)

# Prepare dataset
df = pd.read_csv("../data/dataset.csv", sep=",").sample(frac=1, random_state=42).reset_index(drop=True)
X = df[["Temperature", "Humidity", "Pressure"]].values
y = df["Label"].values

# Normalize the features
X_normalized = scaler.transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_normalized, y, test_size=0.1, stratify=y, random_state=42
)

# Path to the saved model file in the "model" folder
model_path = "../models/random_forest_model.pkl"

# Load the trained model
clf = joblib.load(model_path)

# Generate learning curve data
train_sizes, train_scores, test_scores = learning_curve(
    clf, X, y, cv=5, scoring='accuracy', train_sizes=np.linspace(0.1, 1.0, 10)
)

# Calculate mean and std deviation of scores
train_mean = train_scores.mean(axis=1)
train_std = train_scores.std(axis=1)
test_mean = test_scores.mean(axis=1)
test_std = test_scores.std(axis=1)

# Plot learning curve
plt.plot(train_sizes, train_mean, label="Training Score", color="blue")
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, color="blue", alpha=0.2)
plt.plot(train_sizes, test_mean, label="Cross-validation Score", color="orange")
plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, color="orange", alpha=0.2)
plt.xlabel("Training Set Size")
plt.ylabel("Accuracy")
plt.title("Learning Curve")
plt.legend()
plt.savefig('diagrams/learning_curve.png') 
plt.show()
