import os
import base64
import pickle
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from kneed import KneeLocator

# Load data (Wine dataset)


def load_data():
    wine = load_wine()
    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    df["target"] = wine.target
    serialized = pickle.dumps(df)
    return base64.b64encode(serialized).decode("ascii")


# Preprocessing

def data_preprocessing(data_b64: str):
    data_bytes = base64.b64decode(data_b64)
    df = pickle.loads(data_bytes)
    feature_cols = [c for c in df.columns if c != "target"]
    df = df.dropna()
    X = df[feature_cols].values
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    serialized = pickle.dumps(X_scaled)
    return base64.b64encode(serialized).decode("ascii")




def build_save_model(data_b64: str, filename: str):
    data_bytes = base64.b64decode(data_b64)
    X_scaled = pickle.loads(data_bytes)

    kmeans_kwargs = {"init": "random", "n_init": 10, "max_iter": 300, "random_state": 42}
    sse = []
    last_model = None
    for k in range(1, 16):
        km = KMeans(n_clusters=k, **kmeans_kwargs)
        km.fit(X_scaled)
        sse.append(km.inertia_)
        last_model = km

    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)
    with open(output_path, "wb") as f:
        pickle.dump(last_model, f)

    return sse



def load_model_elbow(filename: str, sse: list, data_b64: str):
    
    model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model", filename)
    kmeans = pickle.load(open(model_path, "rb"))

    kl = KneeLocator(range(1, 16), sse, curve="convex", direction="decreasing")
    print(f"Optimal number of clusters (elbow): {kl.elbow}")

    data_bytes = base64.b64decode(data_b64)
    X_scaled = pickle.loads(data_bytes)
    pred = kmeans.predict(X_scaled[:1])[0]
    try:
        return int(pred)
    except Exception:
        return pred.item() if hasattr(pred, "item") else pred
