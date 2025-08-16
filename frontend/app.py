
import streamlit as st
import requests

st.title("🤖 Local Chatbot with GenAI")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("Say something...")

if user_input:
    response = requests.post(
        "http://127.0.0.1:8000/chat",
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
