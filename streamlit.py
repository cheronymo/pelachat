import streamlit as st
import query_data as query_data

st.title("PelaChat")

question = st.chat_input()
if question:
    st.chat_message("user").write(question)
    with st.spinner("Searching for an answer..."):
        answer = query_data.query_rag(question)
        reponse, source = answer
    st.chat_message("assistant").write(reponse)
    st.chat_message("assistant").write(source)
