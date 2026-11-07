# Titanic Survival Prediction

Supervised classification project that predicts whether a passenger survived the Titanic disaster from ticket class, sex, age, family size, fare, and related features.

## Dataset

Kaggle-format Titanic files are stored in `data/` (downloaded automatically by the first notebook cell if missing):

- `data/train.csv` — 891 passengers with the `Survived` label (`0` = did not survive, `1` = survived)
- `data/test.csv` — 418 passengers without labels, used for the final prediction file

Source (public copies of the classic Kaggle files):

- https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv
- https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/test.csv

If the files are missing, the first notebook cell downloads them, or run:

```bash
python download_data.py
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## How to run

1. Open `titanic_survival_prediction.ipynb` in Jupyter or VS Code / Cursor.
2. Run all cells from top to bottom (`random_state=42` throughout).
3. Final unlabeled-test predictions are written to `outputs/submission.csv` (`PassengerId`, `Survived`).

```bash
jupyter notebook titanic_survival_prediction.ipynb
```

To execute the notebook non-interactively:

```bash
jupyter nbconvert --to notebook --execute titanic_survival_prediction.ipynb --output titanic_survival_prediction.ipynb
```

## Notebook contents

- Exploratory data analysis (class imbalance and survival by sex, class, age, port)
- Missing-value handling and feature engineering (title, family size, cabin deck, age/fare bins)
- Logistic Regression, Random Forest, and XGBoost with stratified 5-fold cross-validation
- GridSearchCV hyperparameter tuning
- Accuracy, precision, recall, F1, ROC-AUC, and confusion matrix
- Insights on gender and class bias in the historical data

## Reproducibility

- `random_state=42` for all splits, models, and search
- Imputers and encoders are fit on training data only (sklearn `Pipeline`)
- Test labels are never used (the test file has none)
