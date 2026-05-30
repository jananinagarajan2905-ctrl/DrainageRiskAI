import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv("drainage_risk_dataset.csv")

X = df.drop("risk", axis=1)

encoder = LabelEncoder()
y = encoder.fit_transform(df["risk"])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("Accuracy:", accuracy)

joblib.dump(model, "risk_model.pkl")
joblib.dump(encoder, "label_encoder.pkl")