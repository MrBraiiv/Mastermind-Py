import keys, display
from constants import CODE_LEN, PegColors, GameState

def play(game, board):
    display.render(board)
    while game.gamestate == GameState.CONTINUE:
        key = keys.read()
        _handle_key(key, game)
        if key == 'submit':
            row_index = len(game.history.guesses) - 1
            _fill(board.rows[row_index], game.buffer, game.history.exacts[row_index], game.history.misplaced[row_index])
            display.render(board)

def _handle_key(key, game):
    match(key):
        case 'left':
            game.move_left()
        case 'right':
            game.move_right()
        case 'submit':
            game.submit_guess()
        case color:
            game.set_color(color)


def _fill(row, buffer, exacts, misplaced):
    for i in range(CODE_LEN):
        row.colors[i].color = buffer[i]
    for i in range(exacts):
        row.result.pins[i] = PegColors.WHITE.name.lower()
    for i in range(exacts, exacts + misplaced):
        row.result.pins[i] = PegColors.CYAN.name.lower()
