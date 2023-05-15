# This file handles console logging in various colors consistently across the project.

class ConsoleLogger:
    # ANSI color codes
    COLOR_CYAN = "\033[96m"
    COLOR_MAGENTA = "\033[95m"
    COLOR_GREEN = "\033[92m"
    COLOR_RED = "\033[91m"
    COLOR_RESET = "\033[0m"

    COLOR_INPUT = COLOR_CYAN
    COLOR_THINKING = COLOR_MAGENTA
    COLOR_REPSONSE = COLOR_GREEN

    @staticmethod
    def log_input(input_text):
        print(f"{ConsoleLogger.COLOR_INPUT}INPUT: {input_text}{ConsoleLogger.COLOR_RESET}")

    @staticmethod
    def log_thinking():
        print(f"\n{ConsoleLogger.COLOR_THINKING}Thinking...{ConsoleLogger.COLOR_RESET}\n")

    @staticmethod
    def log_response(response_text):
        print(f"{ConsoleLogger.COLOR_REPSONSE}RESPONSE: {response_text}{ConsoleLogger.COLOR_RESET}")
