class Parser:
    def __init__(self, code: str):
        self.code = code

    def  check_brackets_balance(self) -> bool:
        open_count = 0
        close_count = 0

        for char in self.code:
            if char == "[":
                open_count += 1
            elif char == "]":
                close_count += 1

        return open_count == close_count