import numpy as np
import pandas as pd
from openai import OpenAI
import streamlit as st
import ast
from sklearn.metrics import classification_report

df_predicted=pd.read_json("messages_classification.json", encoding="windows-1252")
df_org=pd.read_csv("messages.csv")

y_true=df_org["Sentiment"]
y_pred=df_predicted["sentiment"]

print(classification_report(y_true, y_pred))

y_true=df_org["Intent"]
y_pred=df_predicted["intent(s)"]


print(classification_report(y_true, y_pred))


