from langchain_community.document_loaders import  DirectoryLoader,PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI()
loader=DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)
# docs=loader.load()
docs=loader.lazy_load()


for document in docs:
    print(document.metadata)

# print(len(docs))
# print(docs[11].page_content)
# print(docs[11].metadata)