"""
Week 1 Mini Project: Titanic Survival Prediction - Data Cleaning
Run from VS Code terminal: python main.py

Required input:
    train.csv (download from Kaggle Titanic competition and place beside this file)
"""

from pathlib import Path
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "train.csv"
OUTPUT_CSV = BASE_DIR / "cleaned_titanic.csv"
OUTPUT_PLOT = BASE_DIR / "age_distribution.png"


def main():
    if not DATA_FILE.exists():
        print("ERROR: train.csv was not found.")
        print("Download train.csv from:")
        print("https://www.kaggle.com/competitions/titanic/data")
        print(f"Save it here: {BASE_DIR}")
        sys.exit(1)

    # 1. Load dataset and show basic statistics
    df = pd.read_csv(DATA_FILE)
    print("\\nFIRST FIVE ROWS")
    print(df.head())
    print("\\nDATASET INFORMATION")
    df.info()
    print("\\nBASIC STATISTICS")
    print(df.describe(include="all"))
    print("\\nMISSING VALUES BEFORE CLEANING")
    print(df.isnull().sum())

    # 2. Handle missing values
    # Median is used for numerical columns; mode for Embarked.
    if "Age" in df.columns:
        df["Age"] = df["Age"].fillna(df["Age"].median())
    if "Fare" in df.columns:
        df["Fare"] = df["Fare"].fillna(df["Fare"].median())
    if "Embarked" in df.columns and df["Embarked"].isnull().any():
        df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Cabin usually has many missing values in the Titanic training data.
    if "Cabin" in df.columns:
        df = df.drop(columns=["Cabin"])

    # 3. Encode categorical columns
    if "Sex" in df.columns:
        label_encoder = LabelEncoder()
        df["Sex"] = label_encoder.fit_transform(df["Sex"].astype(str))

    if "Embarked" in df.columns:
        # Support both newer (sparse_output) and older (sparse) sklearn versions.
        try:
            encoder = OneHotEncoder(
                sparse_output=False, handle_unknown="ignore"
            )
        except TypeError:
            encoder = OneHotEncoder(
                sparse=False, handle_unknown="ignore"
            )

        encoded_values = encoder.fit_transform(df[["Embarked"]])
        encoded_columns = encoder.get_feature_names_out(["Embarked"])
        encoded_df = pd.DataFrame(
            encoded_values, columns=encoded_columns, index=df.index
        )
        df = pd.concat([df.drop(columns=["Embarked"]), encoded_df], axis=1)

    # 4. Visualize age distribution
    if "Age" in df.columns:
        plt.figure(figsize=(9, 5))
        sns.histplot(df["Age"], bins=30, kde=True)
        plt.title("Titanic Passenger Age Distribution")
        plt.xlabel("Age")
        plt.ylabel("Number of Passengers")
        plt.tight_layout()
        plt.savefig(OUTPUT_PLOT, dpi=150)
        plt.show()
        print(f"Age distribution graph saved to: {OUTPUT_PLOT.name}")

    # 5. Save cleaned dataset
    df.to_csv(OUTPUT_CSV, index=False)
    print("\\nMISSING VALUES AFTER CLEANING")
    print(df.isnull().sum())
    print(f"\\nCleaned dataset saved to: {OUTPUT_CSV.name}")
    print("\\nPROJECT COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    main()
