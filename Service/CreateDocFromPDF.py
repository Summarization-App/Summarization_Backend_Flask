# from langchain_community.document_loaders import pdf
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pypdf

import os

# from app import app

pdf_path = os.path.join("uploads")

def CreateDoc(filename):
    thePDFPath = os.getcwd()+"/uploads/"+filename
    
    loader = PyPDFLoader(thePDFPath)

    docs_raw = loader.load()

    docs_raw_text = [doc.page_content for doc in docs_raw]

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
                                                   chunk_overlap=1000)
    
    docs = text_splitter.create_documents(docs_raw_text)

    return docs



