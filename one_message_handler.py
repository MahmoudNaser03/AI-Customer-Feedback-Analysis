import requests
import streamlit as st
import json

st.title("Customer Message Classifier")
message=st.text_input("Enter your message :")


client = OpenAI(api_key = "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")

def classify_message(message):
    prompt=f"""Classify the following customer message. provide:
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

   

if st.button("Classify"):
    st.write(result)
   # st.write(data["intent"])

