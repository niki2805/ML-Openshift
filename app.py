"""
Tiny Iris-classifier REST API (Flask)

Run locally:
    python app.py
Then open:
    http://127.0.0.1:5000/healthz        -> "ok"
    POST to /predict with JSON {"features":[5.1,3.5,1.4,0.2]}
"""

from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import numpy as np

# ── 1. Train a model once at container start ──────────────────
iris = load_iris()
model = LogisticRegression(max_iter=200)
model.fit(iris["data"], iris["target"])

# ── 2. Build the Flask app  ───────────────────────────────────
app = Flask(__name__)

@app.route("/healthz")                         # liveness / readiness
def health():
    return "ok", 200

@app.route("/predict", methods=["POST"])       # main ML endpoint
def predict():
    payload = request.get_json(force=True)
    try:
        features = np.asarray(payload["features"]).reshape(1, -1)
    except (KeyError, ValueError, TypeError):
        return jsonify({"error": "JSON must contain key 'features' with 4 numeric values"}), 400

    pred = int(model.predict(features)[0])
    return jsonify({"prediction": pred})

# ── 3. Launch dev server if run directly  ─────────────────────
if __name__ == "__main__":
    # host 0.0.0.0 lets it listen inside containers too
    app.run(host="0.0.0.0", port=5001, debug=True)
