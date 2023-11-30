def sp_symbols(line):
    special_symbols = '_*[]()~`>#+-=|{}.!'
    symbols = {
        '_': '\_',
        '*': '\*',
        '[': '\[',
        ']': '\]',
        '(': '\(',
        ')': '\)',
        '~': '\~',
        '`': '\`',
        '>': '\>',
        '#': '\#',
        '+': '\+',
        '-': '\-',
        '=': '\=',
        '|': '\|',
        '{': '\{',
        '}': '\}',
        '.': '\.',
        '!': '\!'
    }
    if any([x in line for x in special_symbols]):
        return ''.join(map(lambda x: symbols[x] if x in symbols else x, line))
    else:
        return line
