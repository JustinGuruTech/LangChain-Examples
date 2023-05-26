# Memory Example

This script introduces the use of the `ConversationChain` in LangChain for memory retention and contextualized conversations. It demonstrates how to use the `ConversationChain` to maintain context across multiple calls to the language model.

## Key Components

-   **ConversationChain and PromptTemplate**: The script imports `ConversationChain` and `PromptTemplate` from `langchain`. These are used to structure the conversation with the language model and handle input variables.
    
-   **Default LLM**: The script uses the default language model defined in `config.py`.
    
-   **ConsoleLogger**: This utility from `utils.console_logger` is used for handling user input and output in the console.
    

## How It Works

The script first sets up the language model and initializes a `ConversationChain` with the language model. The `ConversationChain` is used to maintain context across multiple calls to the language model.

Next, it prepares a `PromptTemplate` with placeholders for `name` and `bio`.

Then, it gets the `name` and `bio` from user input, formats the prompt with these input variables, and logs the formatted prompt.

Finally, it provides the formatted prompt to the `ConversationChain`'s predict method, which generates a response from the language model. It then asks for a sensible bio based on the original input, demonstrating the recall capability of the `ConversationChain`.

## Running the Script

You can run this script from the command line using the following command:

`python -m examples.memory`

When you run the script, you'll be asked to provide a name and some details about yourself. The language model will then generate a silly bio based on these inputs, followed by a sensible one.