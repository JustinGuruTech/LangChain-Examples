# Chats Example

This script demonstrates the usage of the `ChatOpenAI` class in LangChain to create interactive conversations with AI. It presents different ways to communicate with LangChain Chat Models, such as single messages, multi-messages, and batch messages. It also illustrates the usage of Chat Prompt Templates and Chat Chains to simplify interaction with LLMs in a chat context.

## Key Components

-   **LangChain, ConversationChain, and PromptTemplate**: The script imports several classes from `langchain` including `ChatOpenAI`, `LLMChain`, `HumanMessage`, `SystemMessage`, and various prompt templates. These are used to structure the conversation with the language model and handle input variables.
    
-   **Default LLM**: The script uses the default language model defined in `config.py`.
    
-   **ConsoleLogger**: This utility from `utils.console_logger` is used for handling user input and output in the console.
    

## How It Works

The script first sets up the language model and initializes a `ChatOpenAI` instance with the language model. It then gets an example number from the user. Depending on the example number, it performs one of the following tasks:

-   **Single Message Example**: The chat model generates a response to a single human message.
-   **Multi-Message Example**: The chat model generates a response considering multiple messages as context.
-   **Batch Messages Example**: The chat model generates responses for several sets of messages in parallel.
-   **Chat Prompt Template Example**: The chat model generates a response based on a formatted prompt.

Each example demonstrates a different aspect of interacting with language models in a chat context using LangChain.

## Running the Script

You can run this script from the command line using the following command:

`python -m examples.chats`

When you run the script, you'll be asked to choose an example to run. Depending on your choice, the script will demonstrate single message interaction, multi-message interaction, batch message interaction, or interaction using chat prompt templates.