# LangChain Examples

[LangChain is a framework for developing applications powered by language models.](https://python.langchain.com/en/latest/index.html) 

Its primary goal is to provide a straightforward way for developers to interact with LLMs, create agents for specific tasks, and maintain memory/context throughout conversations.

This project contains example usage and documentation around using the LangChain library to work with language models from OpenAI and HuggingFace.

### Resources
- [LangChain Overview From Pinecone](https://www.pinecone.io/learn/langchain-intro/)
- [LangChain Quickstart Guide](https://python.langchain.com/en/latest/getting_started/getting_started.html)

### Introduction

The (paid) [OpenAI](https://platform.openai.com/account/api-keys) and (free) [HuggingFace](https://huggingface.co/settings/tokens) APIs can both be used for LLM interactions. [SerpApi](https://serpapi.com/) is used for searching in `agents.py` and has a free tier.

### Installation
1. Clone the repository.
2. Install the required packages using
`pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and update the placeholder values with your API keys.

### Files with examples & documentation
#### `app.py`
 - Example of a simple GPT interaction using LangChain's `PromptTemplate` & `LLMChain`
 - Details on setting up LLMs, building prompts, and making calls
 #### `memory.py`
- Example of a conversation with multiple messages & memory retention using `ConversationChain`
- Details on memory & context maintenance 
#### `agents.py`
- Example of a GPT Agent determining it needs to perform a web search, then doing so with [SerPapi](https://serpapi.com/) 
- Details on running agents with access to tools & decision making.
- Note, a [SerpApi](https://serpapi.com/) API key is needed for the web search in this example.

### Usage
Run each example file individually:
```
python app.py
python agents.py
python memory.py
```