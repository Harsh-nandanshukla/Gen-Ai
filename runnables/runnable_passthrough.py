from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel,RunnableSequence,RunnablePassthrough

load_dotenv()

model=ChatOpenAI()
parser=StrOutputParser()

prompt1=PromptTemplate(
    template='Give a joke on the  {topic}',
    input_variables=['topic']

)
chain1=RunnableSequence(prompt1,model,parser)#generates joke
prompt2=PromptTemplate(
    template='give explaination of  {text}',
    input_variables=['text']

)
parallel_chain=RunnableParallel({
    'joke': RunnablePassthrough(),# IN CASE WE WANT TO PRINT JOKE AND EXPLANATION BOTH 
    'explaination': RunnableSequence(prompt2,model,parser)
})
final_chain=RunnableSequence(chain1, parallel_chain)
print(final_chain.invoke({'topic':'black khole'}))