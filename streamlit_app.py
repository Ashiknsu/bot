import io
import os

import openai
import streamlit as st


openai.api_key = "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"

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
            st.write("Question:" + st.session_state.history[i]['content'], is_user=True)
        else:
            st.write("Answer:" + st.session_state.history[i]['content'])


