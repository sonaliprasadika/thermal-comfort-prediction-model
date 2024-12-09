import pandas as pd
from everywhereml.sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Prepare dataset
df = pd.read_csv("../data/dataset.csv", sep=",").sample(frac=1, random_state=42).reset_index(drop=True)
X = df[["Temperature", "Humidity", "Pressure"]].values
y = df["Label"].values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, stratify=y, random_state=42
)

# Train RandomForestClassifier
clf = RandomForestClassifier(n_estimators=20, max_leaf_nodes=10)
clf.fit(X_train, y_train)

# Evaluate and predict
print(f'Score: {clf.score(X_test, y_test):3.3f}')
prediction = clf.predict([[70, 20, 1000]])
print("Prediction for new input:", prediction)

# Save the trained model
joblib.dump(clf, 'random_forest_model.pkl')
print("Model saved as 'random_forest_model.pkl'")

# Save the model for MicroPython
clf.to_micropython_file('random_forest_model.py')

import random_forest_model
model = random_forest_model.RandomForestClassifier()
print(model.predict([23.7, 42.6, 1016.6]))