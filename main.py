from ollama import chat
from ollama import ChatResponse

def add(a: int, b: int) -> int:
    """
    Adds two integers together.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers.
    """

def run_agent(query: str):
    MODEL = "qwen3-coder:latest"
    messages = [
        {
            "role": "user",
            "content": query
         }
    ]

    MAX_ITERATIONS = 10

    for i in range(MAX_ITERATIONS):
        print(f'Iteration {i+1}/{MAX_ITERATIONS}')
        response: ChatResponse = chat(
            model=MODEL,
            messages=messages,
            tools=[add]
        )
        if response.message.tool_calls:
            print(f"Tool call detected: {response.message.tool_calls}")
            # Here you can add logic to handle the tool calls, for example, by executing the tool and adding the result back to the messages
            for tool_call in response.message.tool_calls:
                if tool_call.name == "add":
                    args = tool_call.args
                    result = add(**args)
                    print(f"Tool result: {result}")
                    messages.append({
                        "role": "tool",
                        "content": f"Result of add({args[0]}, {args[1]}) is {result}"
                    })
        else:
            return response.message.content

    print("Max iterations reached without a final answer.")
    return message[-1].content  # Return the last message content if max iterations reached

def main():
    query = "What is 5 + 3?"
    result = run_agent(query)
    print(f"Final result: {result}")

if __name__ == "__main__":
    main()