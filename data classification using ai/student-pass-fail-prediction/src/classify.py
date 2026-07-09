"""
Project 2: Data Classification Using AI
DecodeLabs Industrial Training Kit

GOAL
----
Predict whether a student PASSES or FAILS based on:
    - hours_studied
    - attendance_percent
    - assignments_completed

PIPELINE (Input -> Process -> Output)
INPUT   -> Load the dataset, scale the features
PROCESS -> Train/test split, train a Logistic Regression classifier
OUTPUT  -> Accuracy, Confusion Matrix, F1 Score, saved plot
"""

import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # allows saving plots without a display/GUI
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    f1_score,
    ConfusionMatrixDisplay,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "student_data.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data(path: str) -> pd.DataFrame:
    """STEP 1: Load and understand the dataset."""
    df = pd.read_csv(path)

    print("=" * 60)
    print("STEP 1: LOAD & UNDERSTAND THE DATASET")
    print("=" * 60)
    print(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns\n")
    print("First 5 rows:")
    print(df.head(), "\n")
    print("Summary statistics:")
    print(df.describe(), "\n")
    print("Class balance (passed column):")
    print(df["passed"].value_counts(), "\n")

    return df


def split_data(df: pd.DataFrame):
    """STEP 2: Split data into training and testing sets."""
    print("=" * 60)
    print("STEP 2: TRAIN / TEST SPLIT")
    print("=" * 60)

    X = df[["hours_studied", "attendance_percent", "assignments_completed"]]
    y = df["passed"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples:  {len(X_test)}\n")

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler


def train_model(X_train, y_train):
    """STEP 3: Apply a simple classification algorithm."""
    print("=" * 60)
    print("STEP 3: TRAIN THE MODEL (Logistic Regression)")
    print("=" * 60)

    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)

    print("Model trained successfully.\n")
    return model


def evaluate_model(model, X_test, y_test):
    """STEP 4: Evaluate using Confusion Matrix and F1 Score."""
    print("=" * 60)
    print("STEP 4: EVALUATE THE MODEL")
    print("=" * 60)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print(f"Accuracy: {accuracy:.2%}")
    print(f"F1 Score: {f1:.2f}\n")
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=["Fail", "Pass"]))
    print("Confusion Matrix:")
    print(cm, "\n")

    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Fail", "Pass"])
    disp.plot(cmap="Blues")
    plt.title("Confusion Matrix - Student Pass/Fail Prediction")
    plot_path = os.path.join(OUTPUT_DIR, "confusion_matrix.png")
    plt.savefig(plot_path, bbox_inches="tight")
    plt.close()
    print(f"Confusion matrix plot saved to: {plot_path}\n")

    return accuracy, f1


def predict_new_student(model, scaler):
    """BONUS: Use the trained model on a brand-new student."""
    print("=" * 60)
    print("BONUS: PREDICT A NEW STUDENT")
    print("=" * 60)

    new_student = pd.DataFrame(
        [[7.5, 85.0, 8]],
        columns=["hours_studied", "attendance_percent", "assignments_completed"],
    )
    new_student_scaled = scaler.transform(new_student)
    prediction = model.predict(new_student_scaled)[0]
    probability = model.predict_proba(new_student_scaled)[0][1]

    result = "PASS" if prediction == 1 else "FAIL"
    print("New student -> hours=7.5, attendance=85%, assignments=8")
    print(f"Prediction: {result} (probability of passing: {probability:.2%})\n")


def main():
    df = load_data(DATA_PATH)
    X_train, X_test, y_train, y_test, scaler = split_data(df)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    predict_new_student(model, scaler)

    print("=" * 60)
    print("DONE! Project 2 pipeline completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()
