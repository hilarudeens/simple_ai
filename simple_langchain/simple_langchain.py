# LGEL - Langchanin expression language

from langchain_core.runnables import RunnableLambda

def add_salutation(name: str) -> str:
    return f"Hi {name}"

def say_greet(sal: str) -> str:
    return  f"{sal} Good Morning!"

# Convert the python functions to RunnableLambda objects
step_1_runnable = RunnableLambda(add_salutation)
step_2_runnable = RunnableLambda(say_greet)

# Execute the runnables as chain

# chain = step_1_runnable | step_2_runnable
chain = step_2_runnable | step_1_runnable

result = chain.invoke("Sheik")

print(f"Result: {result}")
