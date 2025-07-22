import requests
import streamlit as st
import json
from openai import OpenAI
import ast

st.title("Customer Message Classifier")
message = st.text_input("Enter your message :")

client = OpenAI(
    api_key="API_KEY")


def classify_message(message):
    prompt = f"""Classify the following customer message. provide:
1. Sentiment: Positive, Neutral, or Negative
2. Intent(s): List **all applicable** intents from [Request Info, Complaint, Cancel Account, Feedback, Refund, ...]. 

Message:
{message}

Respond in a list of two text elements:['Sentiment :...', 'Intent : ..., ...']

"""
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    result = ast.literal_eval(completion.choices[0].message.content)
    return  result


if st.button("Classify"):
    st.write(classify_message(message))
# st.write(data["intent"])
