from flask import Flask, render_template
import pandas as pd
import joblib
import json

app = Flask(__name__)

# Load AI model
model = joblib.load("risk_model.pkl")
encoder = joblib.load("label_encoder.pkl")

@app.route("/")
def home():

    # Read latest sensor values
    with open("sensor_data.json", "r") as file:
        data = json.load(file)

    # Convert to DataFrame for prediction
    sample = pd.DataFrame([data])

    # Predict risk
    result = model.predict(sample)
    prediction = encoder.inverse_transform(result)[0]

    return render_template(
        "index.html",
        prediction=prediction,
        data=data
    )

if __name__ == "__main__":
    app.run(debug=True)