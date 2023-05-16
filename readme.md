# LangChain Examples

[LangChain is a framework for developing applications powered by language models.](https://python.langchain.com/en/latest/index.html) 

Its primary goal is to provide a straightforward way for developers to interact with LLMs, create agents for specific tasks, and maintain memory/context throughout conversations.

This project contains example usage and documentation around using the LangChain library to work with language models from OpenAI and HuggingFace.

API keys and default language models for OpenAI & HuggingFace are set up in `config.py`

### Resources
- [LangChain Overview From Pinecone](https://www.pinecone.io/learn/langchain-intro/)
- [LangChain Quickstart Guide](https://python.langchain.com/en/latest/getting_started/getting_started.html)

### Introduction

The (paid) [OpenAI](https://platform.openai.com/account/api-keys) and (free) [HuggingFace](https://huggingface.co/settings/tokens) APIs can both be used for LLM interactions. [SerpApi](https://serpapi.com/) is used for searching in `agents.py` and has a free tier.

### Installation
1. Set up API keys for OpenAI, HuggingFace, and SerpApi (links above).
2. Install the required packages using
`pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and update the placeholder values with your API keys.

### Example Files
There are several files in the `examples` folder, each demonstrating different aspects of working with Language Models and the LangChain library. These can be run using the following commands:
```
python -m examples.interactive_chat
python -m examples.1_basics
python -m examples.2_memory
python -m examples.3_agents
python -m examples.4_chats
```

1. `interactive_chat.py`: Sets up a conversation in the command line with memory using LangChain
2. `1_basics.py`: Demonstrates using PromptTemplate & LLMChain with the OpenAI & HuggingFace APIs to generate chat completions.
3. `2_memory.py`: Shows how to use ConversationChain to maintain context across multiple calls.
4. `3_agents.py`: Demonstrates using Agents with access to tools to perform various tasks.
5. `4_chat.py`: Demonstrates the usage of Chat Messages, Chat Prompt Templates, and Chat Chains with Language Models.

### Utils
- `console_logger.py` is used for colorful logging to the console, along with assisting in the coloring of LLM streams
- `custom_stream.py` contains a `Callbacks` class that can be passed to an LLM to automatically color the output stream when `streaming=True` 