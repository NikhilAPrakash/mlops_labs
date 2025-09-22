from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib
from data import load_data, split_data
import pathlib
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "../model/wine_model.pkl"

def fit_model(X_train, y_train):
    clf = Pipeline(steps=[
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=500, random_state=12))
    ])
    clf.fit(X_train, y_train)
    joblib.dump(clf, MODEL_PATH)

if __name__ == "__main__":
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    fit_model(X_train, y_train)