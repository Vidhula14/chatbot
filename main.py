import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
def responseGenerator(prompt):
    load_dotenv()
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    response= chat_completion.choices[0].message.content
    return response
st.title("chatbot") 
if "messages" not in st.session_state:
    st.session_state.messages=[]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

with st.chat_message("ai"):
    st.write("how can i help you?")
if prompt:=st.chat_input("ask me anything"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})
    try:
        response = responseGenerator(prompt)
    except:
        response="problem"
    with st.chat_message("ai"):
        st.markdown(response ) 
    st.session_state.messages.append({"role":"ai","content":response})














# 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