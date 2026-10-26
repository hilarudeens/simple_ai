import io
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

claude_model = init_chat_model(
    model="claude-sonnet-5-5",
    max_tokens=1000,
    max_retries=1,
    # temperature=0.5
)

conversation = [
    { "role": "system", "content": "You are a helpful bot to user and responsible to answers user question" }
]

# conversation.

def send_prompt(message: str) -> str:
    conversation.append({ "role": "user", "content": message})
    assistant_resp = claude_model.invoke(conversation)
    conversation.append({ "role": "assistant", "content": assistant_resp.content})
    # Return the response text
    return assistant_resp.text
 



while True:
    print("-------------------------------\n")
    query = str(input("Enter your query: \n"))
    response = send_prompt(query)
    print("-------------------------------\n")
    print(f"Agent: \n {response}")
    