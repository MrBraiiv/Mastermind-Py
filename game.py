from dataclasses import dataclass, field
import random
import collections

_COLORS = (
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
)

_CODE_LEN = 4

@dataclass
class History:
    guesses: list[tuple] = field(default_factory=list)
    exacts: list[int] = field(default_factory=list)
    misplaced: list[int] = field(default_factory=list)

class Game:
    def __init__(self):
        self._code = _random_code()
        self.history = History()
        self.cursor = 0
        self.turn = 0

def _random_code() -> tuple:
    return tuple(random.choice(_COLORS) for i in range(_CODE_LEN))

def _calc_exacts(code, guess):
    return sum(code[i] == guess[i] for i in range(_CODE_LEN))

def _calc_misplaced(code, guess, exacts_count):
    code_count, guess_count = collections.Counter(code), collections.Counter(guess)
    color_matches = sum(min(code_count[color], guess_count[color]) for color in code_count)
    # ^ min per color = shared pegs of that color; summed = all color
    return color_matches - exacts_count
    # ^ matches (includes exact), so subtracting exacts_count leaves misplaced.

def _calc_feedback(code, guess):
    exacts = _calc_exacts(code, guess)
    return (exacts, _calc_misplaced(code, guess, exacts))
