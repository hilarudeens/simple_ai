import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    max_tokens=1024,
    system="You are a helpful hotel front desk assistant. Your hotel name is HLR International",
    messages= [
        {
            "role": "user",
            "content": "Greet me, I have booking today"
        }
    ],
    model="claude-sonnet-5-5"
)

# print(message)


if message.stop_reason == "end_turn":
    for block in message.content:
        if block.type == "text":
            print(block.text)

