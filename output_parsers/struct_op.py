from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
load_dotenv()
model=ChatOpenAI()


schema=[
    ResponseSchema(name='fact1',description='Fact1 about the topic'),
    ResponseSchema(name='fact2',description='Fact2 about the topic'),
    ResponseSchema(name='fact3',description='Fact3 about the topic') 
]

parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template='give 3 fact about {topic}\n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
# prompt=template.invoke({'topic':'black hole'})
# result=model.invoke(prompt)
# final_res=parser.parse(result.content)
# print(final_res)
chain=template | model | parser
result=chain.invoke({'topic':'black hole'})
print(result)