import random
import time
import json

while True:

    data = {
        "oxygen": round(random.uniform(16, 21), 2),
        "h2s": round(random.uniform(0, 50), 2),
        "methane": round(random.uniform(0, 200), 2),
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(40, 90), 2),
        "water_level": round(random.uniform(0, 100), 2)
    }

    with open("sensor_data.json", "w") as file:
        json.dump(data, file)

    print(data)

    time.sleep(5)