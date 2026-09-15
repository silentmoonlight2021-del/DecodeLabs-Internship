import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def main():
    print(" DecodeLabs - Project 2: Data Classification Using AI")

    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target

    print("\n[+] Step 1: Dataset Successfully Loaded")
    print(f"Features: {list(X.columns)}")
    print(f"Classes: {list(iris.target_names)}")
    print(f"Total Samples: {X.shape[0]}")
    print("\nFirst 5 Rows of Dataset:")
    print(X.head())


    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print("\n[+] Step 2: Data Split Completed")
    print(f"Training Set Size: {X_train.shape[0]} samples")
    print(f"Testing Set Size: {X_test.shape[0]} samples")

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("\n[+] Step 3: Model Training Completed (RandomForest)")

    y_pred = model.predict(X_test)

    print("\n[+] Step 4: Model Evaluation & Validation")

    acc = accuracy_score(y_test, y_pred)
    print(f"\nModel Accuracy: {acc * 100:.2f}%")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nDetailed Classification Report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    print("\n[+] Step 5: Testing with Unseen Sample Data")
    sample_data = [[5.1, 3.5, 1.4, 0.2]]  # Expected: setosa
    predicted_class_id = model.predict(sample_data)[0]
    predicted_class_name = iris.target_names[predicted_class_id]

    print(f"Sample Input: {sample_data}")
    print(f"Predicted Class: {predicted_class_name}")


if __name__ == "__main__":
    main()