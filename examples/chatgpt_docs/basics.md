# Basics Example

This script introduces basic LangChain components. It demonstrates how to build a prompt with input variables using `PromptTemplate`, create an `LLMChain`, which wraps the prompt and language model for easy use, and run the chain with input variables taken from user input.

## Key Components

-   **LangChain and PromptTemplate**: The script imports `LLMChain` and `PromptTemplate` from `langchain`. These are used to structure the conversation with the language model and handle input variables.
    
-   **Default LLM**: The script uses the default language model defined in `config.py`.
    
-   **ConsoleLogger**: This utility from `utils.console_logger` is used for handling user input and output in the console.
    

## How It Works

The script first sets up the language model and a `PromptTemplate`. The template handles input variables much like an f-string and includes placeholders for `event_objective` and `team_size`.

Next, it creates an `LLMChain`, which is a convenience object that wraps a prompt and a language model, providing an easy way to use the two together.

Then, it gets the `event_objective` and `team_size` from user input, formats the prompt with these input variables, and logs the formatted prompt.

Finally, it provides the input variables to the `LLMChain`'s run method, which handles the template formatting and generates a response from the language model.

## Running the Script

You can run this script from the command line using the following command:

`python -m examples.basics`

When you run the script, you'll be asked to provide an event objective and a team size. The language model will then generate a response based on these inputs.