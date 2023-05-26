# LangChain Examples

[LangChain is a framework for developing applications powered by language models.](https://python.langchain.com/en/latest/index.html) 

This project contains example usage and documentation around using the LangChain library to work with language models.

API keys and default language models for OpenAI & HuggingFace are set up in `config.py`. In this file, the default LLMs are set up with the callback class defined in `custom_stream.py`, which handles streaming output.

### Resources
- [LangChain Overview From Pinecone](https://www.pinecone.io/learn/langchain-intro/)
- [LangChain Quickstart Guide](https://python.langchain.com/en/latest/getting_started/getting_started.html)

### Introduction

An [OpenAI API key](https://platform.openai.com/account/api-keys) is needed for this project, but it could also be used with [HuggingFace](https://huggingface.co/settings/tokens) with a few tweaks. [SerpApi](https://serpapi.com/) is used for searching in `agents.py` and has a free tier.

### Installation
1. Set up API keys for OpenAI (and SerpApi if running agents)
2. Install the required packages using
`pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and update the placeholder values with your API keys.
4. Run `python -m main` to run the interactive example selector

### Example Files
There are several files in the `examples` folder, each demonstrating different aspects of working with Language Models and the LangChain library. 

**Files**
1. `interactive_chat.py`: Sets up a conversation in the command line with memory using LangChain
2. `basics.py`: Demonstrates using PromptTemplate & LLMChain to generate chat completions.
3. `memory.py`: Shows how to use ConversationChain to maintain context across multiple calls.
4. `agents.py`: Demonstrates using Agents with access to tools to perform various tasks.
5. `chat.py`: Demonstrates the usage of Chat Messages, Chat Prompt Templates, and Chat Chains with Language Models.

Individual files can be run using the following commands:
```
python -m examples.interactive_chat
python -m examples.basics
python -m examples.memory
python -m examples.agents
python -m examples.chats
```

### Utils
- `console_logger.py` is used for colorful input & logging to the console
- `custom_stream.py` contains a `Callbacks` class that can be passed to an LLM to automatically color the output stream when `streaming=True` 