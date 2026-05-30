# Drainage Risk AI

An AI-powered drainage safety monitoring system that predicts risk levels inside drainage systems using environmental sensor data.

## Features

* Real-time drainage risk prediction
* Synthetic sensor simulation
* Machine learning classification
* Flask web dashboard
* Automatic monitoring workflow

## Tech Stack

* Python
* Flask
* Pandas
* Scikit-Learn
* Random Forest

## Workflow

Virtual Sensor → Sensor Data → AI Model → Risk Prediction → Dashboard

## Risk Levels

* Safe
* Warning
* Danger

## Run the Project

Install dependencies:

```bash
pip install flask pandas scikit-learn joblib numpy
```

Run sensor simulator:

```bash
python sensor_simulator.py
```

Run dashboard:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

## Future Enhancements

* ESP32 Integration
* Real Gas Sensors
* Cloud Database
* SMS Alerts
* Mobile Application
* Historical Analytics
