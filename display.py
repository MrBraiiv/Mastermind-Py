import terminal, board

def _border(left, mid, right):
    return terminal.BLOCK[left] + terminal.BLOCK[mid] * 2 + terminal.BLOCK[right]

def _content_line(left, content, right):
    return terminal.BLOCK[left] + content + terminal.BLOCK[right]

def _backcolor(content, color):
    return terminal.COLORS[color] + content + terminal.COLORS['reset']

def _pin_pair(p1, p2):
    return _backcolor(' ', p1) + _backcolor(' ', p2)


def repr_colorblock(b: board.ColorBlock) -> str: # join block struct in one string
    return (_border('top_left', 'horizontal', 'top_right')
            + _content_line('vertical', _backcolor('  ', b.color), 'vertical') * 2
            + _border('bottom_left', 'horizontal', 'bottom_right'))

def repr_resultblock(b: board.ResultBlock) -> str: # join block struct in one string
    return (_border('double_top_left', 'double_horizontal', 'double_top_right')
            + _content_line('double_vertical', _pin_pair(b.pins[0], b.pins[1]), 'double_vertical')
            + _content_line('double_vertical', _pin_pair(b.pins[2], b.pins[3]), 'double_vertical')
            + _border('double_bottom_left', 'double_horizontal', 'double_bottom_right'))

