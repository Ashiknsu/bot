import io
import os

import openai
import streamlit as st
from streamlit_chat import message as msg

openai.api_key = os.getenv("chatbot")

st.title("University of Liberal Arts Bangladesh")
st.subheader("Department of Computer Science and Engineering")
st.write("***")
if 'history' not in st.session_state:
    st.session_state.history = []

userInput = st.text_input("Write your Question Please")
btn_env = st.button("Send")

if btn_env:
    st.session_state.history.append({"role": "user", "content": userInput})
    request_openai = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.history,
        max_tokens=500,
        n=1
    )
    st.session_state.history.append(
        {"role": "assistant",
         "content": request_openai['choices'][0]['message']['content']})

if 'exam' in userInput:
    st.write("Are you want to know the date of final exam for Spring 2023")
    if 'yes' in userInput:
        st.write("Final exam is going to start from 02 May 2023")

if len(st.session_state.history) > 0:
    for i in range(len(st.session_state.history)):
        if i % 2 == 0:
            msg("Question:" + st.session_state.history[i]['content'], is_user=True)
        else:
            msg("Answer:" + st.session_state.history[i]['content'])

if len(st.session_state.history) > 0:
    btn_save = st.button("Save Text")
    if btn_save:
        data = io.BytesIO()
        document = docx.Document()
        document.add_heading('abc', level=1)
