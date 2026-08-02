import sys, tty, termios

class Cbreakmode:
    def __init__(self, fd = None):
        self._fd = sys.stdin.fileno() if fd is None else fd

    def __enter__(self):
        self._old = tty.setcbreak(self._fd)

    def __exit__(self, exc_type, exc_val, exc_tb):
        termios.tcsetattr(self._fd, termios.TCSADRAIN, self._old)



