from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model=ChatOpenAI()

# schema
json_schema = {
  "title": "Review",
  "description": "Structured analysis of a product review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Overall sentiment of the review"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {"type": "string"},
      "description": "List of positive aspects"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {"type": "string"},
      "description": "List of negative aspects"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}


structured_model=model.with_structured_output(json_schema)
result=structured_model.invoke("""The hardware is genuinely impressive and feels solid in daily use, with excellent build quality, strong performance, and a display that stands out in its price segment. However, the overall software experience significantly drags down what could otherwise be a great product. The system comes loaded with a large number of pre-installed applications, many of which cannot be uninstalled or even properly disabled, leading to unnecessary storage usage and background activity. This makes the device feel cluttered right out of the box.

In addition to the bloatware issue, the user interface design feels dated and inconsistent when compared to competing brands that offer cleaner, more modern UI experiences. Some menus are unintuitive, animations feel sluggish at times, and system settings are scattered in a way that reduces usability. While the core features are present, the lack of polish makes everyday interactions less enjoyable than expected.

Overall, the device has strong potential due to its capable hardware, but the software needs serious refinement. A major software update that focuses on reducing bloatware, modernizing the UI, and improving system optimization would greatly enhance the user experience. Until then, the product feels like a missed opportunity where excellent hardware is held back by poorly optimized software decisions. """)

# print(result.name)
print(type(result))
print(result)