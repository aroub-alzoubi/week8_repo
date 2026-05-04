def prepare_features(df):
   df = df.copy()

   protocol_map = {
       "TCP": 1,
       "UDP": 2,
       "ICMP": 3
   }

   df["protocol"] = df["protocol"].map(protocol_map)

   features = df[
       [
           "duration",
           "bytes_sent",
           "bytes_received",
           "failed_logins",
           "port",
           "protocol"
       ]
   ]

   return features