from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

model, le = joblib.load("modelo_disasters_melhor.pkl")
feature_columns = ['year', 'total_deaths', 'total_affected', 'total_damage_usd_original']

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        features = [float(data.get(col, 0)) for col in feature_columns]
        X = pd.DataFrame([features], columns=feature_columns)
        pred_encoded = model.predict(X)[0]
        pred_label = le.inverse_transform([pred_encoded])[0]

        return jsonify({"predicted_class": pred_label})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
