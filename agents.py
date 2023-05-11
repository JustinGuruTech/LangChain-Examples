from dotenv import load_dotenv
import os

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI, HuggingFaceHub

#region API/LLM Setup
# - See app.py for more details

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY")
SERPAPI_API_KEY = os.environ.get("SERPAPI_API_KEY")

llm_open_ai = OpenAI(
    temperature=0.9,
    max_tokens=100
)

llm_hugging_face = HuggingFaceHub(
    repo_id="google/flan-t5-xl", 
    model_kwargs={
        "temperature": 0.6,
        "max_length": 64
    }
) 

#endregion

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
agent.run("Find any recent articles on Guru Technologies in Layton, UT.")

#endregion
