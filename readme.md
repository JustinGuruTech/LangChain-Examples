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
There are several example files, each demonstrating different aspects of working with Language Models and the LangChain library:

1. `app.py`: Demonstrates the usage of LLMChain with OpenAI and HuggingFace Language Models.
2. `memory.py`: Shows how to use ConversationChain to maintain context across multiple calls.
3. `agents.py`: Explains how Agents determine which tools to use and how to use them to achieve a specific goal.
4. `chat.py`: Demonstrates the usage of Chat Messages, Chat Prompt Templates, and Chat Chains with Language Models.


### Usage
Run each example file individually:
```
python app.py
python agents.py
python memory.py
python chat.py
```