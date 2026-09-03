import sys
from constants import Colors

def read():
    while True:
        match sys.stdin.read(1).lower():
            case 'q':
                return 'quit'
            case '<' | ',':
                return 'left'
            case '>' | '.':
                return 'right'
            case '\n' | '\r':
                return 'submit'
            case c if c in Colors:
                return Colors(c).name.lower()
            case _:
                continue
