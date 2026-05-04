import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest

from feature_extraction import prepare_features


df = pd.read_csv("network_logs.csv")

X = prepare_features(df)

model = IsolationForest(
   contamination=0.5,
   random_state=42
)

model.fit(X)

predictions = model.predict(X)

df["prediction"] = predictions
df["prediction_label"] = df["prediction"].apply(
   lambda x: "normal" if x == 1 else "suspicious"
)

print("Training Results:")
print(df[["label", "prediction_label"]])

joblib.dump(model, "model.pkl")

print("\nModel trained and saved successfully as model.pkl")