# This file demonstrates the usage of Chat Messages, Chat Prompt Templates, and Chat Chains with OpenAI and HuggingFace Language Models.
# It shows different examples of communicating with LLMs using single messages, multi-messages, and batch messages.
# It also demonstrates the usage of Chat Prompt Templates and Chat Chains for a more streamlined approach to interacting with LLMs in a chat context.


from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from config import default_llm_open_ai, default_llm_hugging_face

# see config.py for API key setup and default LLMs
llm_open_ai = default_llm_open_ai
llm_hugging_face = default_llm_hugging_face

# Note that this controls which example is run for the whole file despite it being split into regions
example_number = 4

#region Chat Messages
# - Chat messages are used to communicate with the LLMs

# Initialize chat 
chat = ChatOpenAI(temperature=0.9, max_tokens=100)
# Prepare prompts
silly_gpt_prompt = "You are Silly-GPT and you only respond in an over-jubilant silly fashion."
tired_prompt = "It is 3:30AM and I am hungry. I am tired. But I enjoy late night programming. You get it, right?"

# Single message example
if example_number == 0:
    result = chat([
        HumanMessage(content=tired_prompt)
    ])
    print(result)
# Multi-message example
elif example_number == 1:
    # Chat messages can be chained together
    result = chat([
        # SystemMessage is a way to specifically direct the LLM
        SystemMessage(content=silly_gpt_prompt),
        HumanMessage(content=tired_prompt)
    ])
    print(result)
# Batch messages example
elif example_number == 2:
    # Batch messages can be used to communicate with the LLM in parallel
    batch_messages = [
        [
            SystemMessage(content=silly_gpt_prompt),
            HumanMessage(content="Please explain how AI works at a technical level.")
        ],
        [
            SystemMessage(content=silly_gpt_prompt),
            HumanMessage(content="Please briefly encapsulate the history of humanity.")
        ],
    ]
    result = chat.generate(batch_messages)
    print(result)

#endregion
#region Chat Prompt Templates
# - Chat prompt templates allow composing prompts in a similar way to PromptTemplate as demonstrated in app.py
# - PromptTemplate objects can be composed into a ChatPromptTemplate which gives lets you pass arguments to the ChatPromptTemplate directly rather than to each individual message

# Chat prompt template example
if example_number == 3:
    # Generate prompt template for system message
    template = "You are now Pirate-GPT but you respond as if you are obsessed with the letter {pirate_letter} rather than the letter R."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    # Generate prompt template for human message
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    # Compose chat prompt template from the templates 
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    # Format the prompt, passing the arguments for each template in directly to the format_prompt method
    formatted_prompt = chat_prompt.format_prompt(pirate_letter="B", text="Do you enjoy sailing the seas?")
    # Run chat
    result = chat(formatted_prompt.to_messages())
    print(result)

#endregion
#region Chat Chain
# - Chat chains streamline using 

if example_number == 4:
    template = "You are now Pirate-GPT but you respond as if you are obsessed with the letter {pirate_letter} rather than the letter R."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template="{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(pirate_letter="N", text="What do you do when the wind blows your ship off course?")
    print(result)

#endregion