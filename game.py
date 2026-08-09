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
    guesses: list[tuple[str, ...]] = field(default_factory=list)
    exacts: list[int] = field(default_factory=list)
    misplaced: list[int] = field(default_factory=list)

class Game:
    def __init__(self):
        self._code = _random_code()
        self.buffer = [None] * _CODE_LEN
        self.history = History()
        self.cursor = 0
        self.turn = 0

    def submit_guess(self) -> None:
        if self.full_buffer():
            _record_turn(self.history, self.buffer, _calc_feedback(self._code, tuple(self.buffer)))
            self.turn += 1

    def move_left(self) -> None:
        if self.cursor > 0: self.cursor -= 1

    def move_right(self) -> None:
        if self.cursor < _CODE_LEN - 1: self.cursor += 1

    def full_buffer(self) -> bool:
        return None not in self.buffer

    def set_color(self, color) -> None:
        self.buffer[self.cursor] = color

def _random_code():
    return tuple(random.choice(_COLORS) for i in range(_CODE_LEN))

def _calc_exacts(code, guess):
    return sum(code[i] == guess[i] for i in range(_CODE_LEN))

def _calc_misplaced(code, guess, exacts_count):
    code_count, guess_count = collections.Counter(code), collections.Counter(guess)
    # min per color = shared pegs of that color; summed = all color
    # matches (incl. exact), so subtracting exacts_count leaves misplaced.
    color_matches = sum(min(code_count[color], guess_count[color]) for color in code_count)
    return color_matches - exacts_count

def _calc_feedback(code, guess):
    exacts = _calc_exacts(code, guess)
    return (exacts, _calc_misplaced(code, guess, exacts))

def _record_turn(history, buffer, feedback):
    exacts, misplaced = feedback
    history.guesses.append(tuple(buffer))
    history.exacts.append(exacts)
    history.misplaced.append(misplaced)
