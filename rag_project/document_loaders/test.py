from langchain_community.document_loaders import TextLoader
data = TextLoader("rag_project/document_loaders/GenAI_Course_Part1_Notes.txt"
                  ,encoding="utf-16")

docs=data.load()

#print(doc)
#print(docs[0].page_content)
print(len(docs))