import requests
import streamlit as st
import json


st.title("Customer Message Classifier")
message=st.text_input("Enter your message :")

response = requests.post(
    "http://127.0.0.1:5000/classify",
    json={"message": message}
)
data = response.json()

if st.button("Classify"):
    st.write(data["sentiment"])
    st.write(data["intent"])

