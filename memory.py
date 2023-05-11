from dotenv import load_dotenv
import os

from langchain import OpenAI, ConversationChain
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

#region Contextual Conversation
# - Calls to the API don't have memory or context which is very limiting
# - A ConversationChain can be used to maintain memory/context across multiple calls

conversation = ConversationChain(
    llm=llm_open_ai,
    # llm=llm_hugging_face, # alternative LLM
    verbose=True
)
# First ask for a silly bio with specific details
output = conversation.predict(
    input="Hi! I'm Justin. I like playing guitar, making music, and adventuring with my partner & our two small dogs. I enjoy writing software and keeping up with AI developments. Could you write a bio for me, making it silly and exaggerative? Thanks!",
)
print(output)
# Now ask for a serious bio with the same details to demonstrate recall
output = conversation.predict(
    input="This is great! Can you now generate me a sensible one based on my original input? Thanks again :)"
)
print(output)

#endregion
