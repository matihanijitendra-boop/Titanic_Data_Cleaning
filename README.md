# Titanic Data Cleaning - Week 1 Assignment

## Project contents
- `main.py` - complete Python program
- `requirements.txt` - required Python libraries
- `train.csv` - add the Titanic dataset here (not included)
- `cleaned_titanic.csv` - generated after running the program
- `age_distribution.png` - generated age histogram

## Step 1: Download the dataset
1. Open https://www.kaggle.com/competitions/titanic/data
2. Sign in to Kaggle if required.
3. Download the competition data and extract the ZIP file.
4. Copy **train.csv** into this project folder, beside `main.py`.

## Step 2: Open in VS Code
1. Extract `Titanic_Data_Cleaning.zip`.
2. Open VS Code.
3. Select **File > Open Folder** and choose `Titanic_Data_Cleaning`.

## Step 3: Install packages
Open **Terminal > New Terminal** in VS Code and run:

```bash
python -m pip install -r requirements.txt
```

If `python` is not recognized on Windows, try:

```bash
py -m pip install -r requirements.txt
```

## Step 4: Run the project
```bash
python main.py
```
Or on Windows:
```bash
py main.py
```

The program displays dataset information and statistics, fills missing Age/Fare values with the median, fills Embarked with the mode, encodes Sex and Embarked, creates an age-distribution graph, and saves `cleaned_titanic.csv`.

## Important
The Kaggle `train.csv` file is not bundled in this ZIP. Download it and place it in this folder before running the program.
