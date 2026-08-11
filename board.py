from dataclasses import dataclass, field

from constants import MAX_TURNS, CODE_LEN

class Board:
    def __init__(self, num_rows=MAX_TURNS):
        self.rows = [Row() for i in range(num_rows)]

class Row:
    def __init__(self, num_colors=CODE_LEN):
        self.colors = [ColorBlock('reset') for i in range(num_colors)]
        self.result = ResultBlock(['reset' for i in range(num_colors)])

@dataclass
class ColorBlock:
    color: str

@dataclass
class ResultBlock:
    pins: list[str] = field(default_factory=list)
