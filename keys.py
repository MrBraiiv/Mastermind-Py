import sys

_COLOR_KEYS = frozenset('rgbyp')

def read():
    match sys.stdin.read(1).lower():
        case '<' | ',':
            return 'left'
        case '>' | '.':
            return 'right'
        case c if c in _COLOR_KEYS:
            return c
        case _:
            return None
