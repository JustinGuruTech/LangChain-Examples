from dotenv import load_dotenv
import os

from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI
from langchain.llms import HuggingFaceHub

load_dotenv()

# Paid OpenAI API (https://platform.openai.com/account/api-keys)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
# Free HuggingFace API (https://huggingface.co/settings/tokens)
HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY")

#region Instantiate Language Models
# - Different models can be used or tweaked for different results
# - Temperature - 0-1: "randomness/diversity" of output (higher = more random)

# Paid OpenAI model (https://openai.com/blog/openai-api)
llm_open_ai = OpenAI(
    temperature=0.9,
    max_tokens=100
)

# Free HuggingFace model (https://huggingface.co/google/flan-t5-xl)
llm_hugging_face = HuggingFaceHub(
    repo_id="google/flan-t5-xl", 
    model_kwargs={
        "temperature": 0.6,
        "max_length": 64
    }
) 

#endregion
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

# Makes call to LLM
result = run_task_chain(
    chain_open_ai,
    # chain_hugging_face, # alternative model
    task_name="Update landing page", 
    task_description="Update the landing page to include a new section for the new product."
)
print(result)

#endregion
