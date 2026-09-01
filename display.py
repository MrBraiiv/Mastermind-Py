import terminal

def render(board) -> None:
    print(f"{terminal.SCREEN['clear']}{terminal.SCREEN['home']}")
    for row in board.rows:
        print(_repr_row(row))

def _repr_row(row):
    blocks = [_repr_colorblock(c) for c in row.colors] + [_repr_resultblock(row.result)]
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
    return terminal.BLOCK[left] + terminal.BLOCK[mid] * 2 + terminal.BLOCK[right]

def _content_line(left, content, right):
    return terminal.BLOCK[left] + content + terminal.BLOCK[right]

def _backcolor(content, color):
    return terminal.COLORS[color] + content + terminal.COLORS['reset']

def _pin_pair(p1, p2):
    return _backcolor(' ', p1) + _backcolor(' ', p2)
