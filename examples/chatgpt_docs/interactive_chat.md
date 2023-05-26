# Interactive Chat Example

This script demonstrates a simple interactive conversation loop with a user. It uses LangChain components to handle conversation management, memory, and language model interactions.

## Key Components

-   **LangChain Prompts**: The script imports several classes from `langchain.prompts` including `ChatPromptTemplate`, `MessagesPlaceholder`, `SystemMessagePromptTemplate`, and `HumanMessagePromptTemplate`. These are used to structure the conversation with the language model.
    
-   **ConversationChain**: This class from `langchain.chains` is used to manage the conversation, including maintaining context across multiple exchanges.
    
-   **ConversationBufferMemory**: This class from `langchain.memory` is used to store the conversation history.
    
-   **Default LLM**: The script uses the default language model defined in `config.py`.
    
-   **ConsoleLogger**: This utility from `utils.console_logger` is used for handling user input and output in the console.
    

## How It Works

The script first sets up the language model and the chat prompt template. The template includes a system message, a placeholder for the conversation history, and a human message for user input.

Next, it sets up a simple memory for the conversation using `ConversationBufferMemory`.

Then, it wraps everything in a `ConversationChain`, which manages the conversation, memory, and interaction with the language model.

Finally, it enters an interactive chat loop. The user can type their input, and the script uses the `ConversationChain` to generate a response from the language model. The conversation continues until the user types 'exit'.

## Running the Script

You can run this script from the command line using the following command:

`python -m examples.interactive_chat`

When you run the script, you'll be able to have an interactive chat with the language model. The model is set up to act as a helpful and friendly AI, trained to answer questions about the world and its inhabitants.