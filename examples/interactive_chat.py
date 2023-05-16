# This file demonstrates how to create a simple interactive conversation loop with a user.
# It uses the LangChain components to handle conversation management, memory, and language model interactions.

from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

from config import default_llm_open_ai
from utils.console_logger import ConsoleLogger
from utils.custom_stream import CustomStreamCallback

console_logger = ConsoleLogger()

# See config.py for API key setup and default LLMs
llm_open_ai = default_llm_open_ai

# Initialize Language Model
llm = ChatOpenAI(
    temperature=0.9, 
    max_tokens=100,
    streaming=True, # This enables streaming for the language model
    callbacks=[CustomStreamCallback()] # Custom callback to log response to console
)

# Set up Chat Prompt Template that will be passed to the ConversationChain
prompt = ChatPromptTemplate.from_messages([
    # System prompt to contextualize
    SystemMessagePromptTemplate.from_template("You are a helpful and friendly AI, trained to answer questions about the world and the creatures, places, and things that inhabit it."),
    # Placeholder for chat history which will be filled by the ConversationChain
    MessagesPlaceholder(variable_name="history"),
    # Human prompt for inserting user input
    HumanMessagePromptTemplate.from_template("{input}")
])

# Set up memory for the conversation, 
memory = ConversationBufferMemory(return_messages=True)

# Wrap everything in a ConversationChain
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

# Interactive chat loop
print("Welcome to the interactive chat! Type 'exit' to end the conversation.")
while True:
    # Get user input
    user_input = console_logger.input("\n\nYou: ")
    if user_input.lower() == "exit":
        break

    console_logger.log_thinking() # Thinking...
    # Set color for response
    console_logger.set_response_stream_color()
    # Run the conversation with user input
    response = conversation.predict(input=user_input)
