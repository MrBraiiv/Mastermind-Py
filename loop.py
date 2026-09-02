import keys, display, board
from constants import CODE_LEN, MAX_TURNS, PegColors, GameState

def play(game):
    display.render(_build_board(game))
    while game.gamestate == GameState.CONTINUE:
        key = keys.read()
        _handle_key(key, game)
        display.render(_build_board(game))

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

def _build_board(game):
    b = board.Board()
    row_count = len(game.history.guesses)
    for row_index in range(row_count):
        _fill(b.rows[row_index], game.history.guesses[row_index], game.history.exacts[row_index], game.history.misplaced[row_index])
    if row_count < MAX_TURNS:
        _fill(b.rows[row_count], game.buffer, 0, 0)
    return b

def _fill(row, guess, exacts, misplaced):
    for i in range(CODE_LEN):
        if guess[i] is not None: row.colors[i].color = guess[i]
    for i in range(exacts):
        row.result.pins[i] = PegColors.WHITE.name.lower()
    for i in range(exacts, exacts + misplaced):
        row.result.pins[i] = PegColors.CYAN.name.lower()
