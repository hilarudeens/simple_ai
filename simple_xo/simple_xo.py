# import 
# from ollama import chat
from pathlib import Path
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

system_prompt_path =  Path.joinpath(Path(__file__).parent/"SYSTEM_PROMPT.md")

file = open(system_prompt_path, "r")
SYSTEM_PROMPT = file.read()


conversation = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

game = [
    ['_' for _ in range(3)],
    ['_' for _ in range(3)],
    ['_' for _ in range(3)],
]

# language_models.
claude_model = init_chat_model(
    model="claude-sonnet-5-5",
    max_tokens=1000,
    max_retries=1
)

class AgentGameResponse(BaseModel):
    message: str = Field(description="Any bot message except game string")
    game: str = Field(description="String game response format. Example: X,X,_|O,X,O|_,O,X")
    is_game_over: bool = Field(description="Boolean value should tell game over or not. True is game over. False is game continuing")
    whowins: str = Field(description="Tell who won the game. This should X or O ")

claude_model_structured_output = claude_model.with_structured_output(AgentGameResponse, method="json_schema")


def send_prompt(message: str) -> str:
    global game
    conversation.append({
        "role": "user",
        "content": message
    })
     

    claude_response = claude_model_structured_output.invoke(conversation)

    # conversation.append({ 
    #     "role": "assistant",
    #     "content": claude_response
    # })
    
    message, game, is_game_over, whowins = parser_agent_response(claude_response)
    return message, is_game_over, whowins


def serialize_game():
    game_str=""
    for i in range(0, 3):
        game_str += ",".join(game[i]) + "\n"
    return game_str


def deserialize_game(game_str: str) -> list:
    rows = game_str.split('|')
    game_grid = []
    for i in range(len(rows)):
        game_grid.append(rows[i].split(","))
    return game_grid


def parser_agent_response(message_json):
    agent_game_grid = deserialize_game(message_json.game)
    return message_json.message, agent_game_grid, message_json.is_game_over, message_json.whowins 


def print_game():
    print(serialize_game())


while True:
    print_game()
    print("------------------------------------\n")
    input_str = input("Choose row and column number as row-column, Example: For 2nd row and 3rd column, then type 2-3:\n")
    x,y= input_str.split('-')
    x = int(x)-1
    y = int(y)-1
    game[x][y] = 'X'
    game_message = serialize_game()
    agent_message, is_game_over, whowins = send_prompt(game_message)

    print("------------------------------------\n")
    print(f"Bot Response\n{agent_message}")
    if is_game_over:
        print_game()
        print(f"{whowins} Won the Game\n** GAME OVER! **")
        exit(0)
    