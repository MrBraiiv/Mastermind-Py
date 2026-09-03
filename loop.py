import keys, display, board
from constants import CODE_LEN, MAX_TURNS, PegColors, GameState, WIN_MESSAGE, LOST_MESSAGE

def play(game):
    _render(game)
    while game.gamestate == GameState.CONTINUE:
        key = keys.read()
        _handle_key(key, game)
        _render(game)
    if game.gamestate == GameState.WIN:
        display.message(WIN_MESSAGE, 'yellow')
    elif game.gamestate == GameState.LOST:
        display.message(LOST_MESSAGE, 'red')
        print(display.repr_colors([board.ColorBlock(c) for c in game.code]))

def _render(game):
    display.render(_build_board(game),
                   current_row=len(game.history.guesses),
                   cursor=game.cursor)

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
