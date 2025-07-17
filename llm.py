import pandas as pd
import json
from openai import OpenAI

import numpy as np
import pandas as pd
from openai import OpenAI
import streamlit as st
import ast
from sklearn.metrics import classification_report

# Load the messages
df = pd.read_csv("messages.csv")

df=df["Message"]

print(df)

# Combine messages into a numbered list for the prompt
messages_text = "\n".join([
    f"{i+1}. \"{msg}\"" for i, msg in enumerate(df)
])

# Build the classification prompt
prompt = f"""Classify the following customer messages. For each message, provide:
1. Sentiment: Positive, Neutral, or Negative
2. Intent(s): List **all applicable** intents from [Request Info, Complaint, Cancel Account, Feedback, Refund, ...]. 

Messages:
{messages_text}

Respond in JSON list format like:
[
  {{"message": message text, "sentiment": "...", "intent(s)": "...and ...(if multi  Intent)"}},
  ...
]
"""


client = OpenAI(api_key = "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")


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

# Parse the response
response_json = completion.choices[0].message.content
print("API response:\n", response_json)

# Optional: Save to file
with open("messages_classification.json", "w") as f:
    f.write(response_json)


df_predicted=pd.read_json("messages_classification.json", encoding="windows-1252")
df_org=pd.read_csv("messages.csv")

y_true=df_org["Sentiment"]
y_pred=df_predicted["sentiment"]

print(classification_report(y_true, y_pred))

y_true=df_org["Intent"]
y_pred=df_predicted["intent(s)"]


print(classification_report(y_true, y_pred))