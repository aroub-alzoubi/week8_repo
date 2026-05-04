def detector_agent(status):
   if status == "suspicious":
       return "Threat detected by the machine learning model."
   return "No threat detected by the machine learning model."


def analyzer_agent(log_data, status):
   if status == "normal":
       return "The activity follows normal network behavior patterns learned by the model."

   return "The model detected unusual network behavior based on the feature pattern."


def reporter_agent(status, risk_level, analysis):
   if status == "suspicious":
       return f"ALERT: {risk_level.upper()} risk activity detected. {analysis}"

   return "Report: The network activity is normal. No action required."