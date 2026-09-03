import terminal, os
from constants import BLOCK_WIDTH, BOARD_SIZE, CONTROLS

def render(board, current_row=None, cursor=None) -> None:
    print(f"{terminal.SCREEN['clear']}{terminal.SCREEN['home']}")
    pad = _padding()
    for row_index, row in enumerate(board.rows):
        for line in _repr_row(row).split('\n'):
            print(pad + line)
        if row_index == current_row and cursor is not None:
            print(pad + ' ' * (cursor * BLOCK_WIDTH + 1) + '^^')
    print(_repr_controls(CONTROLS, terminal.TEXT['black'], terminal.COLORS['green']))

def message(text, color) -> None:
    print(terminal.TEXT['bold'] + terminal.TEXT[color] + text + terminal.COLORS['reset'])

def repr_colors(colors):
    return _join([_repr_colorblock(c) for c in colors])

def _padding():
    return ' ' * max(0, (os.get_terminal_size().columns - BOARD_SIZE) // 2)

def _repr_row(row):
    return _join([_repr_colorblock(c) for c in row.colors] + [_repr_resultblock(row.result)])

def _repr_controls(content, text_color, background_color):
    width = os.get_terminal_size().columns
    return background_color + text_color + content.center(width)[:width] + terminal.COLORS['reset']

def _join(blocks):
    return '\n'.join([''.join(block[i] for block in blocks) for i in range(4)])

def _repr_colorblock(block):
    content = _content_line('vertical', _backcolor('  ', block.color), 'vertical')
    return [_border('top_left', 'horizontal', 'top_right'),
            content,
            content,
            _border('bottom_left', 'horizontal', 'bottom_right')]

def _repr_resultblock(block):
    return [_border('double_top_left', 'double_horizontal', 'double_top_right'),
            _content_line('double_vertical', _pin_pair(block.pins[0], block.pins[1]), 'double_vertical'),
            _content_line('double_vertical', _pin_pair(block.pins[2], block.pins[3]), 'double_vertical'),
            _border('double_bottom_left', 'double_horizontal', 'double_bottom_right')]

def _border(left, mid, right):
    return terminal.BLOCK[left] + terminal.BLOCK[mid] * (BLOCK_WIDTH - 2) + terminal.BLOCK[right]

def _content_line(left, content, right):
    return terminal.BLOCK[left] + content + terminal.BLOCK[right]

def _backcolor(content, color):
    return terminal.COLORS[color] + content + terminal.COLORS['reset']

def _pin_pair(p1, p2):
    return _backcolor(' ', p1) + _backcolor(' ', p2)
