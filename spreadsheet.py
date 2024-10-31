
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        value = self.get(cell)
        if value.isdigit():
            return int(value)
        try:
            float(value)  # Check if it can be a valid float
            return "#Error"
        except ValueError:
            if value.startswith("'") and value.endswith("'"):
                return value[1:-1]
            elif value.startswith("="):
                if value[1:].isdigit():
                    return value[1:]
                elif value[1:].startswith("'") and value[-1] == "'":
                    return value[2:-1]
                elif value[1:] in self._cells:
                    return self.evaluate(value[1:])
            return "#Error"

