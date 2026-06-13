from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(model='mistral-small-2506')

prompt = ChatPromptTemplate.from_messages([
    ("system","""You are an expert movie information extractor.

Instructions:
- Extract only information present in the paragraph.
- If information is missing, write NULL.
- Keep the summary short (2-3 lines).
- Do NOT guess unknown facts.
- Follow the exact output format.

Output Format:

Movie Title:
Release Year:
Genre:
Director:
Main Cast:
Characters:
Organizations:
Setting/Location:
Plot:
Themes:
Scientific Concepts:
Notable Features:
Keywords:

Short Summary:
"""
),

('human',
 """
Extract information from this paragraph:

{paragraph}
""")
]
)

para = input("Give your paragraph : ")
final_prompt = prompt.invoke(
    {"paragraph" : para}
)
response = model.invoke(final_prompt)

print(response.content)