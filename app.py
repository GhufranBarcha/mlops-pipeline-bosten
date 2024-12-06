from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Expect JSON input
    features = pd.DataFrame(data["features"])
    predictions = model.predict(features)
    return jsonify({"predictions": predictions.tolist()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)