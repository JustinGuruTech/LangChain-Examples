# This file demonstrates the usage of Agents for determining which tools to use and how to use them to achieve a specific goal.
# It shows examples of setting up an Agent with tools and parameters, then running the Agent to achieve specific tasks.

from langchain.prompts import (
    ChatPromptTemplate, 
    MessagesPlaceholder, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

from config import default_llm_open_ai, default_llm_hugging_face
from utils.console_logger import ConsoleLogger

console_logger = ConsoleLogger()

# See config.py for API key setup and default LLMs
llm_open_ai = default_llm_open_ai
llm_hugging_face = default_llm_hugging_face

example_number = 0

# LLM Agents
# - Agents can determine what tools to use and how to use them to achieve a goal.
# - For example, if an agent's task is to find a recent article on a company, it will determine that it needs to use a search engine.

#region Message Agent (Web Search)
# - This agent uses Serpapi to find recent information it has not been trained on.

if (example_number == 0):
    # Serpapi enables web search
    tools = load_tools(["serpapi"])

    # Set up agent with tools & parameters
    agent = initialize_agent(
        tools, 
        llm_open_ai,
        # llm_hugging_face, # alternative LLM
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True # This logs the agent's actions to the console
    )

    # Create prompt for agent and log to console
    agent_prompt = "Find a recent article on Guru technologies, summarize it's content, and describe what the company does."
    console_logger.log_input(agent_prompt)
    console_logger.log_thinking() # Thinking...

    agent.run(agent_prompt)

#endregion

#region Chat Agent (Search & Math)
# - This agent uses a chat for streamlining agent interaction.
# - Uses Serpapi to find a math problem and uses llm-math to solve it.

if (example_number == 1):
    # First load the chat that will be used by the agent.
    chat = ChatOpenAI(temperature=0.9, max_tokens=100)

    # Next, load tools for the agent. Some tools like llm-math require a LLM to be passed in.
    llm = OpenAI(temperature=0.9, max_tokens=100)
    tools = load_tools(["serpapi", "llm-math"], llm=llm)

    # Initialize an agent with the tools, language model, and type of agent
    agent = initialize_agent(
        tools, 
        chat, 
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True
    )

    # Create prompt for agent and log to console
    agent_prompt = "Find a ridiculously long PEMDAS math problem online and solve it."
    console_logger.log_input(agent_prompt)
    console_logger.log_thinking() # Thinking...

    # Run agent
    agent.run(agent_prompt)

#endregion

#region ConversationChain Agent
# - This agent uses ConversationChain to interact in a more natural conversation format.
# - Uses a custom prompt and ConversationBufferMemory to maintain a context.
# - Logs output manually using ConsoleLogger for cleanliness.

if (example_number == 2):
    # Define a custom prompt for the conversation
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template("The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know."),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}")
    ])

    # Set up the language model and memory for the conversation
    llm = ChatOpenAI(temperature=0.9, max_tokens=100)
    memory = ConversationBufferMemory(return_messages=True)

    # Initialize the ConversationChain with the custom prompt, memory, and language model
    conversation = ConversationChain(
        memory=memory, 
        prompt=prompt, 
        llm=llm,
    )

    # Interact with the conversation agent
    input = "Exactly what year did humans first develop consciousness?"
    console_logger.log_input(input)
    console_logger.log_thinking() # Thinking...
    output = conversation.predict(input=input)
    console_logger.log_response(output)

    input = "I see. In that case, what are some of the earliest signs of consciousness?"
    console_logger.log_input(input)
    console_logger.log_thinking() # Thinking...
    output = conversation.predict(input=input)
    console_logger.log_response(output)

    input = "Can you summarize this conversation in 3 bullet points?"
    console_logger.log_input(input)
    output = conversation.predict(input=input)
    console_logger.log_response(output)

#endregion
