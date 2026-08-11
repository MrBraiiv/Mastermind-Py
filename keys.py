import sys
from constants import Colors

def read():
    while True:
        match sys.stdin.read(1).lower():
            case '<' | ',':
                return 'left'
            case '>' | '.':
                return 'right'
            case c if c in Colors:
                return Colors(c).name.lower()
            case _:
                continue
