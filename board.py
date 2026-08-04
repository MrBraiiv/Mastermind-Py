from dataclasses import dataclass, field

class Board:
    def __init__(self, rows):
        self.rows = rows

class Row:
    def __init__(self, blocks):
        self.blocks = blocks

class Block:
    """Base for Block object types"""

@dataclass
class ColorBlock(Block):
    color: str
    

@dataclass(frozen=True)
class ResultBlock(Block):
    pins: list[str] = field(default_factory=list)

