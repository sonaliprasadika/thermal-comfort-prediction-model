from sklearn.metrics import precision_recall_curve, average_precision_score
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

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

# Predict probabilities for the positive class
y_prob = clf.predict_proba(X_test)[:, 1]

# Compute precision-recall curve
precision, recall, thresholds = precision_recall_curve(y_test, y_prob)
avg_precision = average_precision_score(y_test, y_prob)

# Plot precision-recall curve
plt.plot(recall, precision, label=f'AP = {avg_precision:.3f}')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()
plt.savefig('diagrams/precision-recall.png') 
plt.show()
