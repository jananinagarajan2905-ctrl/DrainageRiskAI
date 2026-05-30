import pandas as pd
import random

data = []

for _ in range(5000):

    oxygen = round(random.uniform(15, 21), 2)
    h2s = round(random.uniform(0, 50), 2)
    methane = round(random.uniform(0, 200), 2)
    temp = round(random.uniform(20, 45), 2)
    humidity = round(random.uniform(40, 100), 2)
    water_level = round(random.uniform(0, 100), 2)

    score = 0

    if oxygen < 18:
        score += 3
    elif oxygen < 19.5:
        score += 1

    if h2s > 20:
        score += 3
    elif h2s > 10:
        score += 1

    if methane > 100:
        score += 3
    elif methane > 50:
        score += 1

    if water_level > 50:
        score += 3
    elif water_level > 20:
        score += 1

    if temp > 35:
        score += 1

    if score <= 2:
        risk = "Safe"
    elif score <= 5:
        risk = "Warning"
    else:
        risk = "Danger"

    data.append([
        oxygen,
        h2s,
        methane,
        temp,
        humidity,
        water_level,
        risk
    ])

df = pd.DataFrame(
    data,
    columns=[
        "oxygen",
        "h2s",
        "methane",
        "temperature",
        "humidity",
        "water_level",
        "risk"
    ]
)

df.to_csv("drainage_risk_dataset.csv", index=False)

print("Dataset Created")