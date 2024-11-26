from msvcrt import getch
from .memory import Memory
from .parser import Parser
from .exceptions import SyntaxError
from typing import List

class BrainfuckInterpreter:
    def __init__(self, code: str):
        self.memory: Memory = Memory()
        self.code: str = code
        self.loop_stack: List[int] = []

    def run(self):
        i = 0
        while i < len(self.code):
            char = self.code[i]
            if char in self.command_map:
                self.command_map[char](i)
            else:
                i += 1

    def move_right(self, _):
        self.memory.move_right()

    def move_left(self, _):
        self.memory.move_left()

    def increment(self, _):
        self.memory.increment()

    def decrement(self, _):
        self.memory.decrement()

    def input_value(self, _):
        self.memory.set_value(ord(getch()))

    def output_value(self, _):
        print(chr(self.memory.cells[self.memory.pointer]), end="")

    def open_loop(self, i):
        if self.memory.cells[self.memory.pointer] == 0:
            open_brackets = 1
            while open_brackets > 0:
                i += 1
                if i >= len(self.code):
                    raise SyntaxError(i, "Unmatched opening bracket.")
                if self.code[i] == "[":
                    open_brackets += 1
                elif self.code[i] == "]":
                    open_brackets -= 1
        else:
            self.loop_stack.append(i)

    def close_loop(self, i):
        if self.memory.cells[self.memory.pointer] != 0:
            if not self.loop_stack:
                raise SyntaxError(i, "Unmatched closing bracket.")
            return self.loop_stack[-1]
        else:
            self.loop_stack.pop()
            return None

    command_map = {
        ">": move_right,
        "<": move_left,
        "+": increment,
        "-": decrement,
        ",": input_value,
        ".": output_value,
        "[": open_loop,
        "]": close_loop,
    }
