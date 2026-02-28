from langchain_community.document_loaders import  WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI()
url='https://www.flipkart.com/allen-solly-analog-watch-men/p/itmba94bce84ff2b?pid=WATG57J8GXH9GKGP&lid=LSTWATG57J8GXH9GKGPONDWMI&hl_lid=&marketplace=FLIPKART&fm=eyJ3dHAiOiJyZWNvIiwicHJwdCI6ImhwIiwibWlkIjoicGVyc29uYWxpc2VkUmVjb21tZW5kYXRpb24vcDJwLXNhbWUifQ%3D%3D&pageUID=1772220957456'
loader=WebBaseLoader(url)
docs=loader.load()
prompt=PromptTemplate(
    template='answer the foloowing {question} from following {text}',
    input_variables=['question','text']
)
parser=StrOutputParser()

chain=prompt|model|parser
print(chain.invoke({'question':'what is the product listed','text':docs[0].page_content}))