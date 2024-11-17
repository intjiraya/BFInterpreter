# Brainfuck Interpreter

## Overview

This project is a Brainfuck interpreter implemented in Python. Brainfuck is an esoteric programming language that uses a minimalistic set of commands to manipulate an array of memory cells. This interpreter allows you to run Brainfuck code from a file and provides error handling for common issues such as memory overflow and syntax errors.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Error Handling](#error-handling)
- [Code Structure](#code-structure)
- [Examples](#examples)
- [License](#license)

## Installation

To run the Brainfuck interpreter, ensure you have Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Clone the repository or download the source code:

```bash
git clone <repository-url>
cd BFInterpreter
```

## Usage

To run a Brainfuck program, use the following command:

```bash
python main.py <path_to_brainfuck_file>
```

### Command-Line Arguments

- `file`: The path to the Brainfuck file you want to execute.
- `--maxmem`: (Optional) The maximum memory size (default: 30000 cells).

### Example

To run a Brainfuck program that prints "Hello World!", you can use the following command:

```bash
python main.py examples/hello_world.bf
```

## Features

- **Memory Management**: The interpreter uses a bytearray to manage memory cells, allowing for efficient memory operations.
- **Error Handling**: The interpreter raises specific exceptions for memory overflow, syntax errors, and infinite loops.
- **Bracket Matching**: The interpreter checks for balanced brackets in the Brainfuck code to ensure proper loop functionality.

## Error Handling

The interpreter includes the following custom exceptions:

- `BrainfuckError`: Base class for all Brainfuck-related errors.
- `MemoryOverflowError`: Raised when the memory pointer exceeds the bounds of the memory array.
- `SyntaxError`: Raised for syntax errors in the Brainfuck code, including unmatched brackets.
- `InfiniteLoopError`: Raised when a Brainfuck program enters an infinite loop.

## Code Structure

The project is organized into the following main components:

- **`main.py`**: The entry point of the interpreter, responsible for parsing command-line arguments and executing the Brainfuck code.
- **`brainfuck/interpreter.py`**: Contains the `BrainfuckInterpreter` class, which implements the logic for executing Brainfuck commands.
- **`brainfuck/memory.py`**: Manages the memory cells and provides methods for manipulating memory.
- **`brainfuck/parser.py`**: Contains the `Parser` class, which checks for balanced brackets in the Brainfuck code.
- **`brainfuck/exceptions.py`**: Defines custom exceptions for error handling.

## Examples

### Hello World

To run a Brainfuck program that prints "Hello World!", use the following code:

```brainfuck
>+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.>>>++++++++[<++++>-]<.>>>++++++++++[<+++++++++>-]<---.<<<<.+++.------.--------.>>+.>++++++++++.
```

## License

This project is licensed under the GNU General Public License v3. See the [LICENSE](LICENSE) file for more details.
