import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "../model/wine_model.pkl"

def predict_data(X):
    model = joblib.load(MODEL_PATH)
    y_pred = model.predict(X)
    return y_pred


