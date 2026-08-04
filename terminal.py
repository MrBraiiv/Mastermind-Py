import sys, tty, termios

class Cbreakmode:
    def __init__(self, fd = None):
        self._fd = sys.stdin.fileno() if fd is None else fd

    def __enter__(self):
        self._old = tty.setcbreak(self._fd)

    def __exit__(self, exc_type, exc_val, exc_tb):
        termios.tcsetattr(self._fd, termios.TCSADRAIN, self._old)

BLOCK = {
    'horizontal':         '\u2500',  # ─
    'vertical':           '\u2502',  # │
    'top_left':           '\u250c',  # ┌
    'top_right':          '\u2510',  # ┐
    'bottom_left':        '\u2514',  # └
    'bottom_right':       '\u2518',  # ┘
    'light_shade':        '\u2591',  # ░
    'double_top_left':    '\u2554',  # ╔
    'double_top_right':   '\u2557',  # ╗
    'double_bottom_left': '\u255a',  # ╚
    'double_bottom_right':'\u255d',  # ╝
    'double_horizontal':  '\u2550',  # ═
    'double_vertical':    '\u2551',  # ║
}

COLORS = {
    'red':     '\033[41m',
    'green':   '\033[42m',
    'yellow':  '\033[43m',
    'blue':    '\033[44m',
    'magenta': '\033[45m',
    'cyan':    '\033[46m',
    'reset':   '\033[0m',
    'white':   '\033[47m',
}

CURSOR = {
    'up':      '\033[A',
    'down':    '\033[B',
    'right':   '\033[C',
    'left':    '\033[D',
    'hide':    '\033[?25l',
    'show':    '\033[?25h',
}

SCREEN = {
    'clear':          '\033[2J',
    'home':           '\033[H',
    'clear_scroll':   '\033[3J',
    'clear_line':     '\033[2K',
    'clear_to_end':   '\033[K',
}
