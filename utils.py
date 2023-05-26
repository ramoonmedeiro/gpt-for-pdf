from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS


def spliter_into_chunks(text: str) -> list:

    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
        )

    chunks = text_splitter.split_text(text=text)

    return chunks


def storage_vector(chunks, embedding) -> FAISS:
    return FAISS.from_texts(chunks, embedding)
