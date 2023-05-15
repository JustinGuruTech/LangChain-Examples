# This file demonstrates the usage of LLMChain with OpenAI and HuggingFace Language Models.
# It shows how to build a prompt, create an LLMChain, and run the chain with different Language Models.


from langchain import LLMChain, PromptTemplate
from config import default_llm_open_ai, default_llm_hugging_face
from console_logger import ConsoleLogger

console_logger = ConsoleLogger()

# See config.py for API key setup and default LLMs
llm_open_ai = default_llm_open_ai
llm_hugging_face = default_llm_hugging_face

#region Build Prompt
# - Input variables fill in the templates in the prompt (like an fstring)
# - The prompt is passed to the language model
# - This building block approach is important as things scale

prompt = PromptTemplate(
    input_variables=["task_name", "task_description"],
    template="You are a meticulous project manager. Evaluate the given task and ask clarifying and exploratory questions that are within scope.\n\nTask name: {task_name}\nTask description: {task_description}"
)

#endregion
#region Create Chain 
# - A chain is a wrapper around a prompt and language model that streamlines use
# - Chains can be reused and fit into larger pipelines

chain_open_ai = LLMChain(prompt=prompt, llm=llm_open_ai)
chain_hugging_face = LLMChain(prompt=prompt, llm=llm_hugging_face)

#endregion
#region Run Chain
# - To modularize use of chains, they can be run in functions
# - This comes in handy when building applications on top of LLMs

def run_task_chain(chain, task_name, task_description):
    result = chain.run(task_name=task_name, task_description=task_description)
    return result

# Create example task
task_name = "Update landing page"
task_description = "Update the landing page to include a new section for the new product."

# Format prompt with input variables for logging
formatted_prompt = prompt.format(task_name=task_name, task_description=task_description)

# Log formatted prompt
console_logger.log_input(formatted_prompt)
console_logger.log_thinking() # Thinking...

# Makes call to LLM
result = run_task_chain(
    chain_open_ai,
    # chain_hugging_face, # alternative model
    task_name=task_name, 
    task_description=task_description
)
# Log response
console_logger.log_response(result)

#endregion
