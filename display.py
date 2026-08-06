import terminal, board

def _border(left, mid, right):
    return terminal.BLOCK[left] + terminal.BLOCK[mid] * 2 + terminal.BLOCK[right]

def _content_line(left, content, right):
    return terminal.BLOCK[left] + content + terminal.BLOCK[right]

def _backcolor(content, color):
    return terminal.COLORS[color] + content + terminal.COLORS['reset']

def _pin_pair(p1, p2):
    return _backcolor(' ', p1) + _backcolor(' ', p2)

def _repr_colorblock(b: board.ColorBlock) -> list: # join block struct in one string
    content = _content_line('vertical', _backcolor('  ', b.color), 'vertical')
    return [_border('top_left', 'horizontal', 'top_right'),
            content,
            content,
            _border('bottom_left', 'horizontal', 'bottom_right')]

def _repr_resultblock(b: board.ResultBlock) -> list: # join block struct in one string
    return [_border('double_top_left', 'double_horizontal', 'double_top_right'),
            _content_line('double_vertical', _pin_pair(b.pins[0], b.pins[1]), 'double_vertical'),
            _content_line('double_vertical', _pin_pair(b.pins[2], b.pins[3]), 'double_vertical'),
            _border('double_bottom_left', 'double_horizontal', 'double_bottom_right')]

def repr_block(b: board.Block):
    match b:
        case board.ColorBlock():
            return _repr_colorblock(b)
        case board.ResultBlock():
            return _repr_resultblock(b)
        case _:
            raise TypeError(f"unsupported block type {type(b).__name__}")


def disp_row(row: board.Row):
    blocks = [repr_block(b) for b in row.blocks]
    return '\n'.join([''.join(block[i] for block in blocks) for i in range(4)])
