import pandas as pd
import joblib

model = joblib.load("risk_model.pkl")
encoder = joblib.load("label_encoder.pkl")

sample = pd.DataFrame([{
    "oxygen": 20.8,
    "h2s": 2,
    "methane": 10,
    "temperature": 28,
    "humidity": 60,
    "water_level": 5
}])

prediction = model.predict(sample)

print(encoder.inverse_transform(prediction)[0])