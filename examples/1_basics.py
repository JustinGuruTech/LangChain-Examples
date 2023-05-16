# This file demonstrates the usage of LLMChain with OpenAI and HuggingFace Language Models.
# It shows how to build a prompt, create an LLMChain, and run the chain with different Language Models.

from langchain import LLMChain, PromptTemplate

from config import default_llm_open_ai, default_llm_hugging_face
from utils.console_logger import ConsoleLogger

console_logger = ConsoleLogger()

# See config.py for API key setup and default LLMs
llm_open_ai = default_llm_open_ai
llm_hugging_face = default_llm_hugging_face

#region Build Prompt
# - Input variables fill in the templates in the prompt (like an fstring)
# - The prompt is passed to the language model
# - This building block approach is important as things scale

prompt = PromptTemplate(
    input_variables=["event_objective", "team_size"],
    template="You are an event planner for corporate team-building events. Plan an event that achieves the given objective for a team of the specified size.\n\nEvent objective: {event_objective}\nTeam size: {team_size}"
)

#endregion
#region Create Chain 
# - A chain is a wrapper around a prompt and language model that streamlines use
# - Chains can be reused and fit into larger pipelines

chain_open_ai = LLMChain(prompt=prompt, llm=llm_open_ai)
chain_hugging_face = LLMChain(prompt=prompt, llm=llm_hugging_face)

#endregion
#region Run Chain
# - Chains allow calling the LLM directly with input variables with minimal overhead
# - Chains also allow for callbacks to handle result/streams/etc. - see utils/custom_stream.py

# Create example task
event_objective = "Laser Tag Event"
team_size = "1000 people."

# Format prompt with input variables for logging
formatted_prompt = prompt.format(
    event_objective=event_objective, 
    team_size=team_size
)

# Log formatted prompt
console_logger.log_input(formatted_prompt)
console_logger.log_thinking() # Thinking...

# Set response color for logging
console_logger.set_response_stream_color()
# Makes call to LLM
result = chain_open_ai.run(
    # chain_hugging_face, # alternative model
    event_objective=event_objective, 
    team_size=team_size
) # result contains chat completion result

#endregion
