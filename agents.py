# This file demonstrates the usage of Agents for determining which tools to use and how to use them to achieve a specific goal.
# It shows an example of setting up an Agent with tools and parameters, then running the Agent to achieve a specific task.


from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from config import default_llm_open_ai, default_llm_hugging_face
from console_logger import ConsoleLogger

console_logger = ConsoleLogger()

# see config.py for API key setup and default LLMs
llm_open_ai = default_llm_open_ai
llm_hugging_face = default_llm_hugging_face

#region Agent Setup/Run
# - Agents can determine what tools to use and how to use them to achieve a goal.
# - For example, if an agent's task is to find a recent article on a company, it will determine that it needs to use a search engine.

# Serpapi enables web search
tools = load_tools(["serpapi"])

# Set up agent with tools & parameters
agent = initialize_agent(
    tools, 
    llm_open_ai,
    # llm_hugging_face, # alternative LLM
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True
)

# Create prompt for agent and log to console
agent_prompt = "Find any recent articles on Guru Technologies in Layton, UT."
console_logger.log_input(agent_prompt)
console_logger.log_thinking() # Thinking...

agent.run(agent_prompt)

#endregion
