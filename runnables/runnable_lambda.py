from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda

load_dotenv()

def word_count(text):
    return len(text.split())

# runnable_word_count=RunnableLambda(word_count)

model=ChatOpenAI()
parser=StrOutputParser()

prompt=PromptTemplate(
    template='Give a joke on the  {topic}',
    input_variables=['topic']

)
chain1=RunnableSequence(prompt,model,parser)#generates joke

parallel_chain=RunnableParallel({
    'joke': RunnablePassthrough(),
    # 'word_count': RunnableLambda(word_count), it will also work
    'word_count': RunnableLambda(lambda x: len(x.split()))

})

final_chain=RunnableSequence(chain1, parallel_chain)
print(final_chain.invoke({'topic':'black khole'}))