from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

from langchain.chat_models import init_chat_model
model = init_chat_model(model="google_genai:gemini-3.5-flash")
response = model.invoke("Explain machine learning")
print(response.content[0]['text'])