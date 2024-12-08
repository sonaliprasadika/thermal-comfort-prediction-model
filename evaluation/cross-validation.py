from sklearn.model_selection import cross_val_score
import pandas as pd
from everywhereml.sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

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

# Perform 5-fold cross-validation
cv_scores = cross_val_score(clf, X_train, y_train, cv=5, scoring='accuracy')
print(f'Cross-validation scores: {cv_scores}')
print(f'Mean CV Accuracy: {cv_scores.mean():.3f}')
