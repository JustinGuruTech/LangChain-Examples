import sys

# ANSI color codes
COLOR_CYAN = "\033[96m"
COLOR_MAGENTA = "\033[95m"
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"

COLOR_INPUT = COLOR_CYAN
COLOR_THINKING = COLOR_MAGENTA
COLOR_REPSONSE = COLOR_GREEN
COLOR_TOOL = COLOR_MAGENTA
COLOR_ERROR = COLOR_RED


class ConsoleLogger:
    """
    This class handles console logging in various colors consistently across the project.
    Additionally, it handles coloring streamed output from the Language Models, which is only available on select LLMs.
    """

    current_stream_color = COLOR_REPSONSE

    # region Input

    @staticmethod
    def input(message, color=COLOR_INPUT):
        """
        Prints a colored message to the console and captures user input.
        """
        return input(f"{color}{message}{COLOR_RESET}")

    @staticmethod
    def input_with_default(message, default, show_default=True, color=COLOR_INPUT):
        """
        Prints a colored message to the console and captures user input with a default value.
        """
        prompt = f"{color}{message} (default - {default}): " if show_default else f"{color}{message}: "
        user_input = input(prompt)
        return default if user_input == "" else user_input

    @staticmethod
    def input_int(message, color=COLOR_INPUT):
        """
        Prints a colored message to the console and captures an integer user input.
        """
        while True:
            try:
                return int(input(f"{color}{message}{COLOR_RESET}"))
            except ValueError:
                print(f"{COLOR_ERROR}Invalid input! Please enter an integer.{COLOR_RESET}")


    # endregion
    # region Logging

    @staticmethod
    def log(message, color=COLOR_RESET, prefix=""):
        """
        Logs to console with color & an optional prefix.
        """
        ConsoleLogger.current_stream_color = COLOR_RESET
        print(f"{color}{prefix}: {message}{COLOR_RESET}" if prefix else f"{color}{message}{COLOR_RESET}")

    @staticmethod
    def log_input(input_text):
        """
        Logs with the 'INPUT: ' prefix and input color.
        """
        print(f"{COLOR_INPUT}INPUT: {input_text}{COLOR_RESET}")

    @staticmethod
    def log_thinking():
        """
        Logs the 'Thinking...' message to the console
        """
        print(f"\n{COLOR_THINKING}Thinking...{COLOR_RESET}")

    @staticmethod
    def log_response(response_text):
        """
        Logs with the 'RESPONSE: ' prefix and response color.
        """
        print(f"{COLOR_REPSONSE}RESPONSE: {response_text}{COLOR_RESET}")

    @staticmethod
    def log_tool(tool_text):
        """
        Logs with the 'TOOL: ' prefix and tool color.
        """
        print(f"{COLOR_TOOL}TOOL: {tool_text}{COLOR_RESET}")

    @staticmethod
    def log_error(error_text):
        """
        Logs with the 'ERROR: ' prefix and error color.
        """
        print(f"{COLOR_ERROR}ERROR: {error_text}{COLOR_RESET}")

    # endregion
    # region Streaming

    @staticmethod
    def log_streaming(token: str):
        """
        Prints a token in the stream with the response color.
        """
        sys.stdout.write(COLOR_REPSONSE + token)
        sys.stdout.flush()

    @staticmethod
    def set_stream_color(color: str):
        """
        Sets the color for subsequent streamed output.
        """
        ConsoleLogger.current_stream_color = color

    @staticmethod
    def set_response_stream_color():
        """
        Sets the color for the subsequent streamed output to the response color.
        """
        ConsoleLogger.set_stream_color(COLOR_REPSONSE)

    @staticmethod
    def set_default_stream_color():
        """
        Sets the color for the subsequent streamed output to the default color.
        """
        ConsoleLogger.set_stream_color(COLOR_RESET)

    # endregion
