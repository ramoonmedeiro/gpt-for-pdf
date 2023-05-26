# lib for env vars
from dotenv import load_dotenv
import os

# Streamlit
import streamlit as st

# Parse pdfs
from PyPDF2 import PdfReader

# Langchain libs
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.callbacks import get_openai_callback

# Util methods
from .utils import spliter_into_chunks, storage_vector

load_dotenv('.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

st.set_page_config(page_title='Ask anything to your PDF file:')
pdf = st.file_uploader(
    label='Upload you PDF file',
    type='pdf'
    )

if pdf is not None:
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    chunks = spliter_into_chunks(text=text)

    # create embeddings
    embeddings = OpenAIEmbeddings()

    know_database = storage_vector(chunks=chunks, embedding=embeddings)

    user_question = st.text_input("Pergunte algo sobre o seu PDF:")
    if user_question:
        docs = know_database.similarity_search(user_question)

        llm = OpenAI()
        chain = load_qa_chain(llm=llm, chain_type='stuff')
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=user_question)
            print(cb)

        st.write(response)
