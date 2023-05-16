from typing import Any

from langchain.schema import LLMResult
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from utils.console_logger import ConsoleLogger

# Custom callback handler that uses ConsoleLogger to color streamed output from current_stream_color
class CustomStreamCallback(StreamingStdOutCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Run on new LLM token. Only available when streaming is enabled."""
        ConsoleLogger.log_streaming(token)

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Run when LLM ends running."""
        ConsoleLogger.set_default_stream_color()