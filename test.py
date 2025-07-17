import requests
import streamlit as st
import json
from openai import OpenAI
import ast

# Custom CSS for adorable UI
st.markdown('''
    <style>
        body {
            background-color: #f7f5f2;
        }
        .main-card {
            background: #fffbe6;
            border-radius: 18px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.07);
            padding: 2rem;
            margin-top: 2rem;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
            border: 1.5px solid #ffd700;
        }
        .stButton>button {
            background-color: #ffd700;
            color: #333;
            border-radius: 10px;
            font-weight: bold;
            font-size: 1.1rem;
        }
    </style>
''', unsafe_allow_html=True)

st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.title("💬 Customer Message Classifier 🐻")
st.markdown("<h4 style='color:#ff9800;'>Let us help you understand your customers! 😊</h4>", unsafe_allow_html=True)

message = st.text_input("✍️ Enter your message :")

client = OpenAI(
    api_key="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")


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


if st.button("🔍 Classify"):
    result = classify_message(message)
    st.success(f"<b>Sentiment:</b> {result[0]}", icon="💡")
    st.info(f"<b>Intent(s):</b> {result[1]}", icon="📝")

st.markdown('</div>', unsafe_allow_html=True)
