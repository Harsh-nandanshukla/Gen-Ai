from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser,ResponseSchema
from pydantic import BaseModel, Field
load_dotenv()
model=ChatOpenAI()

class Person(BaseModel):
    name:str=Field(description='name of the person')
    age:int=Field(gt=18,description='age of the person')
    city:str=Field(description='name of the city where person lives')


parser=PydanticOutputParser(pydantic_object=Person) 
template=PromptTemplate(
    template='generate the name,age,city of the person lving in  a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

    
   )
# prompt=template.invoke({'place':'india'})
# print(prompt)
# res=model.invoke(prompt)
# final_res=parser.parse(res.content)
# print(final_res)
chain=template |model| parser
result=chain.invoke({'place':'india'})
print(result)