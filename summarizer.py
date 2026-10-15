import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


model=ChatOllama(
    model="gemma3:1b",
    temperature=0.9,
    )
template=ChatPromptTemplate(
    [
         ("system",'''
         you are a AI text summarizer model.
         try to summarise the text in simple english.
         but keep the main keypoints in the summary.
         also try to keep it as short as possible.
         '''),
         ("human","{question}")
    ]
)

st.title("AI based Text Summarizer")

query=st.text_area("Enter the text")

prompt=template.invoke({"question":query})

if query:
    if st.button("summarise"):
        with st.spinner("summarising"):
            output=model.invoke(prompt)
        st.write(output.content)