from enum import Enum, IntEnum, auto

CODE_LEN = 4
MAX_TURNS = 10
BLOCK_WIDTH = 4

WIN_MESSAGE = 'Congrats! You Won! You Broke The Secret Code!'
LOST_MESSAGE = 'Too Bad! You Lost. Be Stronger For The Next Match!\nCode was:'

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
