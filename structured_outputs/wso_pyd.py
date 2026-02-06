from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional,Literal
load_dotenv()
from pydantic import BaseModel,Field

model=ChatOpenAI()

class Review(BaseModel):
    key_themes:list[str]=Field(description='Write down all the key themes discussed in the review list')
    summary:str=Field(description='a brief summar of the review')
    sentiment:Literal['pos','neg']=Field(description='return sentiment either negative positive or neutral')
    pros:Optional[list[str]]=Field(default=None,description='write down all the pros inside a list ')
    cons:Optional[list[str]]=Field(default=None,description='write down all the cons inside a list ')
    name:Optional[str]=Field(default=None,description='write down all the cons inside a list ')
structured_model=model.with_structured_output(Review)
result=structured_model.invoke("""The hardware is genuinely impressive and feels solid in daily use, with excellent build quality, strong performance, and a display that stands out in its price segment. However, the overall software experience significantly drags down what could otherwise be a great product. The system comes loaded with a large number of pre-installed applications, many of which cannot be uninstalled or even properly disabled, leading to unnecessary storage usage and background activity. This makes the device feel cluttered right out of the box.

In addition to the bloatware issue, the user interface design feels dated and inconsistent when compared to competing brands that offer cleaner, more modern UI experiences. Some menus are unintuitive, animations feel sluggish at times, and system settings are scattered in a way that reduces usability. While the core features are present, the lack of polish makes everyday interactions less enjoyable than expected.

Overall, the device has strong potential due to its capable hardware, but the software needs serious refinement. A major software update that focuses on reducing bloatware, modernizing the UI, and improving system optimization would greatly enhance the user experience. Until then, the product feels like a missed opportunity where excellent hardware is held back by poorly optimized software decisions. """)

# print(result.name)
print(result)