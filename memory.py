# This file demonstrates the usage of ConversationChain for maintaining context across multiple calls to the Language Model.
# It shows an example of generating a silly bio and then asking for a serious bio based on the same input, demonstrating recall.


from langchain import ConversationChain
from config import default_llm_open_ai, default_llm_hugging_face
from console_logger import ConsoleLogger

console_logger = ConsoleLogger()

# see config.py for API key setup and default LLMs
llm_open_ai = default_llm_open_ai
llm_hugging_face = default_llm_hugging_face

#region Contextual Conversation
# - Calls to the API don't have memory or context which is very limiting
# - A ConversationChain can be used to maintain memory/context across multiple calls

conversation = ConversationChain(
    llm=llm_open_ai,
    # llm=llm_hugging_face, # alternative LLM
    verbose=True
)

# Create prompt and log to console
silly_bio_request = "Hi! I'm Justin. I like playing guitar, making music, and adventuring with my partner & our two small dogs. I enjoy writing software and keeping up with AI developments. Could you write a bio for me, making it silly and exaggerative? Thanks!"
console_logger.log_input(silly_bio_request)
console_logger.log_thinking() # Thinking...

# First ask for a silly bio with specific details
output = conversation.predict(input=silly_bio_request)
console_logger.log_response(output)

# Now ask for a serious bio with the same details to demonstrate recall
bio_request_followup = "This is great! Can you now generate me a sensible one based on my original input? Thanks again :)"
console_logger.log_input(bio_request_followup)
console_logger.log_thinking() # Thinking...

output = conversation.predict(input=bio_request_followup)
console_logger.log_response(output)

#endregion
