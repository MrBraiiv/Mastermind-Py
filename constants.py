from enum import Enum, IntEnum, auto

CODE_LEN = 4
MAX_TURNS = 10

class Colors(Enum):
    RED =     'r'
    GREEN =   'g'
    YELLOW =  'y'
    BLUE =    'b'
    MAGENTA = 'm'

class PegColors(Enum):
    WHITE = 'w'
    CYAN =  'c'

class GameState(IntEnum):
    CONTINUE = auto()
    LOST = auto()
    WIN = auto()
