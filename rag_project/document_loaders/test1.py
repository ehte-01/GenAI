import os
print("Current Directory:", os.getcwd())

from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator="",
    chunk_size = 10,
    chunk_overlap=1
)

data = TextLoader("rag_project/document_loaders/notes.txt",
    encoding="utf-8")

docs = data.load()
print(docs)
print(len(docs))

chunks = splitter.split_documents(docs)

#print(chunks)
#print(len(chunks))

for i in chunks:
    print(i.page_content)
    print()
    print()
    print()
