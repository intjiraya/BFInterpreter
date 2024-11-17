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
            match char:
                case ">":
                    self.memory.move_right()
                case "<":
                    self.memory.move_left()
                case "+":
                    self.memory.increment()
                case "-":
                    self.memory.decrement()
                case ",":
                    self.memory.set_value(ord(getch()))
                case ".":
                    print(chr(self.memory.cells[self.memory.pointer]), end="")
                case "[":
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
                case "]":
                    if self.memory.cells[self.memory.pointer] != 0:
                        if not self.loop_stack:
                            raise SyntaxError(i, "Unmatched closing bracket.")
                        i = self.loop_stack[-1]
                    else:
                        self.loop_stack.pop()
            i += 1
