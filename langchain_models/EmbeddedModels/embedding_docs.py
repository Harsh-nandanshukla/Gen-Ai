from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
documnets=[
    "Delhi is the capital of India ",
    "Paris is capital of France",
    "Berlin is capital of Germany"
]
result=embedding.embed_documents("Delhi is the capital of India") 
print(str(result))