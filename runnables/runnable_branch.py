from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda,RunnableBranch


load_dotenv()


prompt1=PromptTemplate(
    template='give a detailed report on {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='give a summary of the {text}',
    input_variables=['text']
)
parser=StrOutputParser()
model=ChatOpenAI()
chain1=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>300,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(chain1,branch_chain)
print(final_chain.invoke({'topic':'blackhole'}))