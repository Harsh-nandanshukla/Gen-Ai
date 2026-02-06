from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()
model=ChatOpenAI()
parser=JsonOutputParser()
template=PromptTemplate(
    template='give me the name ,age,city of a fictional person in \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
# prompt=template.format()
# # print(prompt)
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)
chain = template| model | parser
result=chain.invoke({'topic':'black hole'})
print(result)
# print('final :',final_result)
# print(type(final_result))
