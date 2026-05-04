from flask import Flask, render_template, request
import pandas as pd
import joblib

from feature_extraction import prepare_features
from agents import detector_agent, analyzer_agent, reporter_agent


app = Flask(__name__)

model = joblib.load("model.pkl")


def predict_log(log_data):
   log_df = pd.DataFrame([log_data])
   features = prepare_features(log_df)

   prediction = model.predict(features)[0]

   status = "normal" if prediction == 1 else "suspicious"
   risk_level = "high" if status == "suspicious" else "low"

   detection_message = detector_agent(status)
   analysis = analyzer_agent(log_data, status)
   report = reporter_agent(status, risk_level, analysis)

   return {
       "log": log_data,
       "status": status,
       "risk_level": risk_level,
       "detection_message": detection_message,
       "analysis": analysis,
       "report": report
   }


@app.route("/")
def dashboard():
   return render_template(
       "dashboard.html",
       results=[],
       total_logs=0,
       suspicious_logs=0,
       normal_logs=0
   )


@app.route("/analyze", methods=["POST"])
def analyze():
   url = request.form["url"]

   log_data = {
       "duration": len(url),
       "bytes_sent": len(url) * 50,
       "bytes_received": len(url) * 70,
       "failed_logins": url.lower().count("login"),
       "port": 443 if url.startswith("https") else 80,
       "protocol": "TCP"
   }

   result = predict_log(log_data)
   result["url"] = url

   return render_template(
       "dashboard.html",
       results=[result],
       total_logs=1,
       suspicious_logs=1 if result["status"] == "suspicious" else 0,
       normal_logs=1 if result["status"] == "normal" else 0
   )


if __name__ == "__main__":
   app.run(debug=True)