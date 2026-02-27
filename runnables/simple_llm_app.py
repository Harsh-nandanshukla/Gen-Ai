from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm=OpenAI(model_name='gpt-3.5-turbo',temperature=0.7)


prompt=PromptTemplate(
    input_variables=['topic'],
    template='suggest acatch blog title abOUT {topic}'
)


topic=input('enter a topic')
formatted_prompt=prompt.format(topic=topic)
blog_title=llm.predict(formatted_prompt)
print(blog_title)


