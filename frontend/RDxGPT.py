import streamlit as st
import requests
from configs.config import backend_domain_name

st.title("🤖 Local GenAI Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Say something...")

if user_input:
    response = requests.post(
        f"{backend_domain_name}/chat/ollama",
        json={"message": user_input, "history": st.session_state.history}
    )
    print("response",response)
    response=response.json() 
    reply = response["reply"]

    st.session_state.history.append(user_input)
    st.session_state.history.append(reply)

for i, msg in enumerate(st.session_state.history):
    if i % 2 == 0:
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)
