from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence
load_dotenv()

parser=StrOutputParser()
prompt1=PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)
model=ChatOpenAI()

prompt2=PromptTemplate(
    template='explain the {text}',
    input_variables=['text']
)
# chain1=RunnableSequence(prompt1,model,parser)
# print(chain1.invoke({'topic':'cricket'}))
# chain2=RunnableSequence(prompt2,model,parser)
# final_chain= chain1 | chain2
# print(final_chain.invoke({'topic':'cricket'}))

final_chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)
print(final_chain.invoke({'topic':'cricket'}))