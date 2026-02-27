from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel,RunnableSequence

load_dotenv()

model=ChatOpenAI()
parser=StrOutputParser()

prompt1=PromptTemplate(
    template='genearte tweet for {topic}',
    input_variables=['topic']

)
prompt2=PromptTemplate(
    template='genearte linkedin post for the {topic}',
    input_variables=['topic']

)
parallel_chain=RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    'linkedin_post': RunnableSequence(prompt2,model,parser)
})
print(parallel_chain.invoke({'topic':'AI'}))


