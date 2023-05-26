# Agents Example

This script introduces the use of agents in LangChain. Agents can determine when a tool is necessary for a task, for example, determining when a web search or a calculator is needed. It shows examples of setting up an Agent with tools and parameters, then running the Agent to achieve specific tasks.

## Key Components

-   **LangChain, ConversationChain, and PromptTemplate**: The script imports several classes from `langchain` including `ConversationChain`, `PromptTemplate`, and various prompt templates. These are used to structure the conversation with the language model and handle input variables.
    
-   **LangChain Agents**: The script imports `load_tools`, `initialize_agent`, and `AgentType` from `langchain.agents`. These are used to set up an agent with specific tools and parameters.
    
-   **Default LLM**: The script uses the default language model defined in `config.py`.
    
-   **ConsoleLogger**: This utility from `utils.console_logger` is used for handling user input and output in the console.
    

## How It Works

The script first sets up the language model and gets an example number from the user. Depending on the example number, it performs one of the following tasks:

-   **Web Search**: The script sets up an agent with the Serpapi tool, gets a company name from the user, and asks the agent to find a recent article on the company, summarize its content, and describe what the company does.
    
-   **Web Search & Calculator**: The script sets up an agent with the Serpapi and llm-math tools, and asks the agent to find a ridiculously long PEMDAS math problem online and solve it.
    
-   **ConversationBufferMemory Agent for Context Retention**: The script sets up a `ConversationChain` with a custom prompt and `ConversationBufferMemory`, and interacts with the conversation agent.
    

## Running the Script

You can run this script from the command line using the following command:

`python -m examples.agents`

When you run the script, you'll be asked to choose an example to run. Depending on your choice, the script will perform a web search, solve a math problem, or demonstrate context retention in a conversation.