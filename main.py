from utils.console_logger import ConsoleLogger, COLOR_INPUT, COLOR_RESET, COLOR_ERROR
from examples.interactive_chat import main as interactive_chat
from examples.basics import main as basics
from examples.memory import main as memory
from examples.agents import main as agents
from examples.chats import main as chats

def main():
    # Display intro message
    ConsoleLogger.log("Welcome to the LangChain Examples playground!", COLOR_INPUT)
    ConsoleLogger.log("""
Available examples:
    0. interactive_chat.py - A simple conversation loop using LangChain components.
    1. basics.py: Prompt Templates and LLM Chains used in an event planning example.
    2. memory.py: ConversationChain used for memory retention in a bio generation example.
    3. agents.py: Agents with access to web search & calculator tools.
    4. chats.py: More advanced usage of chats, including Chat Models, Chat Prompt Templates, and Chat Chains.\n
    """)
    
    # Ask user for the example they want to run
    example_number = ConsoleLogger.input_int(
        "Choose an example (0-4): "
    )

    # Run the selected example
    if example_number == 0:
        interactive_chat()
    elif example_number == 1:
        basics()
    elif example_number == 2:
        memory()
    elif example_number == 3:
        agents()
    elif example_number == 4:
        chats()
    else:
        ConsoleLogger.log(
            "Invalid selection. Please enter a number between 1 and 4.", 
            COLOR_ERROR
        )

if __name__ == "__main__":
    while True:
        main()
