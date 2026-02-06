# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# load_dotenv()

# llm=HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
# )
# model=ChatHuggingFace(llm=llm)
# result=llm.invoke("what is the capital of india")
# print(result)
from langchain_huggingface import HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "do_sample": True,
        "temperature": 0.5,
        "max_new_tokens": 50,
        "return_full_text": False
    }
)

prompt = "Answer in one sentence: What is the capital of India?"
print(llm.invoke(prompt))

