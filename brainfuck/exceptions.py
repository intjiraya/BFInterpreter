class BrainfuckError(Exception):
    """Base class for Brainfuck errors."""
    def __init__(self, message):
        super().__init__(message)

class MemoryOverflowError(BrainfuckError):
    """Raised when memory pointer exceeds bounds."""
    def __init__(self, pointer: int, size: int):
        message: str = f"Memory pointer {pointer} exceeds bounds (size: {size})."
        super().__init__(message)

class SyntaxError(BrainfuckError):
    """Raised for syntax errors in the Brainfuck code."""
    def __init__(self, position: int, message: str = "Syntax error in Brainfuck code."):
        detailed_message: str = f"{message} Error at position {position}."
        super().__init__(detailed_message)

class InfiniteLoopError(BrainfuckError):
    """Raised when a Brainfuck program enters an infinite loop."""
    def __init__(self, iterations: int):
        message: str = f"Detected an infinite loop after {iterations} iterations."
        super().__init__(message)
