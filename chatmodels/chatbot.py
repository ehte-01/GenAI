from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatMistralAI(model = "mistral-small-2506",temperature=0.9)

print("Choose your AI mode")
print("Press 1 for Angry Mode")
print("Press 2 for Funny Mode")
print("Press 3 for Sad Mode")

choice = int(input("Tel your response:- "))
if choice == 1:
    mode = "You are an angry AI Agent. You respond aggressively and impatiently"
elif choice == 2:
    mode = "You are a very funny AI AGent. You respond with humour and jokes."
elif choice == 3:
    mode = "You are a very sad AI Agent. You respond in a depressed and emotional tone "
messages = [
    SystemMessage(content=mode)
]

print("----------Welcome type 0 to exit the application-----------")
while True:

    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot:",response.content)

print(messages)
