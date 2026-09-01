import game, board, loop, terminal

with terminal.Cbreakmode():
    loop.play(game.Game(), board.Board())
