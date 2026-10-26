from ollama import chat

# Lauch Ollama locally
response = chat(
    model='granite4.2:3b',
    messages=[
        {
            'role': 'user',
            'content': 'Great me, I have booking today'
        }
    ]

)

# print(response)

if response.done_reason == 'stop':
    content = response.message.content
    print(content)