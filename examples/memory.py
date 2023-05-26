"""
This script introduces the use of the `ConversationChain` in LangChain for memory retention and contextualized conversations.
It demonstrates how to use the `ConversationChain` to maintain context across multiple calls to the language model.
"""

from langchain import ConversationChain, PromptTemplate

from config import default_llm
from utils.console_logger import ConsoleLogger, COLOR_INPUT

def main():
    # See config.py for API key setup and default LLMs
    llm = default_llm

    # Initialize ConversationChain with the LLM. 
    # The ConversationChain is used to maintain context across multiple calls to the language model.
    conversation = ConversationChain(
        llm=llm,
        verbose=False # True to log LLM's context to console
    )

    # Prepare prompt template
    prompt = PromptTemplate(
        input_variables=["name", "bio"],
        template="Hi! I'm {name}. {bio}. Could you write a bio for me, making it silly and exaggerative? Thanks!"
    )

    # Get name and bio from user
    ConsoleLogger.log("Provide a name and some details about yourself to generate a silly bio, followed by a sensible one.")
    name = ConsoleLogger.input_with_default(
        "Name",
        "Justin", # default value
        show_default=False # don't show default value in prompt
    )
    bio = ConsoleLogger.input_with_default(
        "Bio details (I like...)",
        "playing guitar, making music, and adventuring with my partner & our two small dogs. I enjoy writing software and keeping up with AI developments.", # default value
        show_default=False # don't show default value in prompt
    )

    # Format prompt with input variables
    formatted_prompt = prompt.format(
        name=name,
        bio=bio
    )
    # Log formatted prompt
    ConsoleLogger.log_input(formatted_prompt)

    # First ask for a silly bio with specific details
    output = conversation.predict(input=formatted_prompt) # Thinking...

    # Create prompt & log to console
    bio_request_followup = "This is great! Can you now generate me a sensible one based on my original input? Thanks again :)"
    ConsoleLogger.log_input(bio_request_followup)

    # Now ask for a serious bio with the same details to demonstrate recall
    response = conversation.predict(input=bio_request_followup) # Thinking...


if __name__ == "__main__":
    main()
