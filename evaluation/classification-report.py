import joblib
from sklearn.metrics import classification_report
import pandas as pd
from sklearn.model_selection import train_test_split

# Paths to the saved model and scaler files
model_path = "../models/random_forest_model.pkl"
scaler_path = "../models/scaler.pkl"

# Load the trained model and scaler
clf = joblib.load(model_path)
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

# Predict on test data
y_pred = clf.predict(X_test)

# Generate classification report
print(classification_report(y_test, y_pred))
