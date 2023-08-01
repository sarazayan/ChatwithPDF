# -*- coding: utf-8 -*-
"""GPT4All_Trial_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zb49PAJRi-p6zlMe1KooEwJfzoRMoBpf
"""

#from google.colab import drive
#drive.mount('/content/drive/')

#!ls '/content/drive/MyDrive/Multiple_PDFs'

#!apt-get install poppler-utils  #to present pages of p

'''!pip install -Uqqq pip --progress-bar off
!pip install -qqq langchain==0.0.173 --progress-bar off
!pip install -qqq chromadb==0.3.23 --progress-bar off
!pip install -qqq pypdf==3.8.1 --progress-bar off
!pip install -qqq pygpt4all==1.1.0 --progress-bar off
!pip install -qqq pdf2image==1.16.3 --progress-bar off
'''
#!gdown 1DpFisoGXsQbpQJvijuvxkLW_pg-FUUMF

!wget https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin #4GB_memory , 6B parameter

from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import GPT4All
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from pdf2image import convert_from_path
from langchain.retrievers.self_query.base import SelfQueryRetriever

'''from langchain.document_loaders import PyPDFDirectoryLoader
loader = PyPDFDirectoryLoader('multiple docs')
docs = loader.load()
type(docs)
print(docs)
'''

from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("/content/volkswagen.pdf")
docs = loader.load()

documents = loader.load_and_split() #converted into documents for langchain

len(documents)

print(documents[0].page_content)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64) #model has only 1000 tokens as limit , it will take both pages and convert it into text
texts = text_splitter.split_documents(documents)

len(texts)

print(texts[0].page_content)
#First page was divided into 2

#Create Embeddings to search for text
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") #MiniLM created by microsoft

#to store embeddings in vector database
db = Chroma.from_documents(texts, embeddings, persist_directory="db")
#db.persists 3shan law 3yza t store it in your disk

#Create Chain
#load gpt4all model
model_n_ctx = 1000
model_path = "./ggml-gpt4all-j-v1.3-groovy.bin"
llm = GPT4All(model=model_path, n_ctx=1000, backend="gptj",temp=0.9,verbose=False)
#trained with gpt-j

#Retrieval
#we get source of document
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever(search_kwargs={"k": 2}),
    return_source_documents=True,
    verbose=False,
)

#print(res["result"])

# Commented out IPython magic to ensure Python compatibility.
# %%time
# prompt = f"""How much is the investment amount in Microsoft on 6/22? Extract the answer from the text."""
# res = qa(prompt.strip())

# Commented out IPython magic to ensure Python compatibility.
#Ask Questions
 %%time
res = qa("Give examples of the main purposes of the KGAS.")

res

# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa(
#     "Summarize the right of contracting authority."
# )

  #res

# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa(
#     "List at least 5 items the training strategy must contain"
# )



# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa(
#     "What is FOSS in 5 sentences "
# )



# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa(
#     "Describe in detail the quality assurance goals "
# )



# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa(
#     "List examples of Unit Test requirements in terms of coverage "
# )



# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa(
#     "What are the categories or types or requirements have to be assigned? "
# )



# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa(
#     "What are the main components of project management?  "
# )



# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa(
#     "How the usage of FOSS is permitted?  "
# )

es

# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa(
#     "What is data acquisition strategy, and what does it include? "
# )



# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa(
#     "How to select and use programming language of the software product? "
# )



# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa(
#     "Describe in detail the quality assurance goals "
# )



# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa(
#     "What are the categories or types or requirements have to be assigned?"
# )

# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa(
#     "Describe in details the General Cybersecurity Requirements"
# )



# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa(
#     "Describe Briefly the General Cybersecurity Requirements"
# )



# Commented out IPython magic to ensure Python compatibility.
# #Ask Questions
# %%time
# res = qa("Where is the documentation deliverable provided ?"
# )

 #0.1

 #0.5

 #0.9

