from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
load_dotenv()

model=ChatOpenAI()
parser=StrOutputParser()
class Feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description='give the sentiment feedback')
parser2=PydanticOutputParser(pydantic_object=Feedback)    

prompt1=PromptTemplate(
    template='classify the sentiment of the following feedback text into positive or negative \n {feedback}\n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)
classifier_chain= prompt1|model|parser2


prompt2=PromptTemplate(
    template='write an appropriate response to this positive feedback {feedback}',
    input_variables=['feedback']

)

prompt3=PromptTemplate(
    template='write an appropriate response to this negative feedback {feedback}',
    input_variables=['feedback']
)

chain1=prompt2|model|parser
chain2=prompt3|model|parser
branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive',chain1),
    (lambda x:x.sentiment=='negative',chain2),
    RunnableLambda(lambda x :"could not find sentiment")

)
chain=classifier_chain|branch_chain
print(chain.invoke({'feedback':'this is a good phone'}))