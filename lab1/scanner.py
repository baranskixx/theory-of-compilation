import ply.lex as lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
    'print': 'print'
}

literals = ['=', '+', '-', '*', '/',
            '(', ')', '[', ']', '{', '}', '<', '>', ':', ';', ',', '\'']

tokens = ['DOTADD', 'DOTSUB', 'DOTMUL', 'DOTDIV',
          'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN',
          'LEQ', 'GEQ', 'NEQ', 'EQ',
          'ID', 'INTNUM', 'FLOAT', 'STRING'] + list(reserved.values())

t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

t_DOTADD = r'\.\+'
t_DOTSUB = r'\.\-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'-='
t_DIVASSIGN = r'/='
t_LEQ = r'<='
t_GEQ = r'>='
t_EQ = r'=='
t_NEQ = r'!='

t_INTNUM = r'\d+'
t_FLOAT = r'(\d+\.\d*|\.\d+)([eE][-+]?\d+)?'
t_STRING = r'\"(\\.|[^"\\\n])*\"'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_error(t):
    print("Illegal character '%s' at line no. %d" % t.value[0], t.lineno)
    t.lexer.skip(1)


lexer = lex.lex()
