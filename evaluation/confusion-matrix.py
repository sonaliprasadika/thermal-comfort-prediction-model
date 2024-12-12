from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import joblib
import pandas as pd
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

# Predict on test data
y_pred = clf.predict(X_test)

# Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Display confusion matrix and save as image
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
disp.plot(cmap='viridis')

# Save the confusion matrix plot as an image
plt.tight_layout()  # Ensures everything fits within the figure
plt.savefig('diagrams/confusion_matrix.png', dpi=300)  # Save with high resolution
plt.close()  # Close the plot to release memory
