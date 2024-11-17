from brainfuck.exceptions import MemoryOverflowError

class Memory:
    def __init__(self, size: int = 30000) -> None:
        self.cells: bytearray = bytearray(size)
        self.pointer: int = 0
        self.size: int = size

    def increment(self) -> None:
        self.cells[self.pointer] = (self.cells[self.pointer] + 1) % 256

    def decrement(self) -> None:
        self.cells[self.pointer] = (self.cells[self.pointer] - 1) % 256

    def move_right(self) -> None:
        if self.pointer >= len(self.cells) - 1:
            raise MemoryOverflowError(self.pointer, self.size)
        self.pointer += 1

    def move_left(self) -> None:
        if self.pointer == 0:
            raise MemoryOverflowError(self.pointer, self.size)
        self.pointer -= 1

    def get_value(self) -> int:
        return self.cells[self.pointer]

    def set_value(self, value: int) -> None:
        if 0 <= value <= 255:
            self.cells[self.pointer] = value
        else:
            raise ValueError(f"Value {value} is out of range")
