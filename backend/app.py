# ================================
# Section 1: Imports
# ================================

import os
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS


# ================================
# Section 2: App Configuration
# ================================

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_FOLDER = BASE_DIR

model_path = os.path.join(MODEL_FOLDER, "disease_model.joblib")
encoder_path = os.path.join(MODEL_FOLDER, "symptoms_encoder.joblib")


# ================================
# Section 3: Load AI Model
# ================================

model = joblib.load(model_path)
encoder = joblib.load(encoder_path)


# ================================
# Section 4: Helper Functions
# ================================

def predict_disease(symptoms):

    # convert symptoms to vector
    symptom_vector = encoder.transform([symptoms])

    # predict disease
    prediction = model.predict(symptom_vector)[0]

    return prediction


# ================================
# Section 5: API Endpoints
# ================================

@app.route("/")
def home():
    return jsonify({
        "message": "Symptom Checker API Running"
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json(silent=True) or {}

    if "symptoms" not in data:
        return jsonify({"error": "Symptoms not provided"}), 400

    symptoms = [
        symptom.strip()
        for symptom in data["symptoms"]
        if isinstance(symptom, str) and symptom.strip()
    ]

    if not symptoms:
        return jsonify({"error": "Symptoms cannot be empty"}), 400

    result = predict_disease(symptoms)

    return jsonify({
        "predicted_disease": result,
        "input_symptoms": symptoms
    })


# ================================
# Run Server
# ================================

if __name__ == "__main__":
    app.run(debug=True)