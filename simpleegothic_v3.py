import ply.lex as lex
import ply.yacc as yacc
from collections import deque

# tokeny
tokens = (
    'TYPE',
    'CH',
    'ST',
    'NAMES',
    'NAMEC',
    'NUMBER',
    'ID',
    'EQ',
    'SUM',
    'ASUM',
    'POW',
    'DIV',
    'TEXT',
    'ONAW',
    'KOT',
    'ZNAW',
    'SPACE',
    'END',
)


def t_TYPE(t):
    r'int\ |double\ '
    v = len(t.value)
    if t.value[v - 1] == " ":
        t.value = t.value[0:v - 1]
    return t


def t_CH(t):
    r'char\ '
    return t


def t_ST(t):
    r'string\ '
    return t


def t_NAMES(t):
    r'suicide|Suicide'
    t.value = t.value.lower()
    return t


def t_NAMEC(t):
    r'defenestracja|Defenestracja'
    t.value = t.value.lower()
    return t


def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z0-9]+'
    return t


def t_EQ(t):
    r'\s*=\s*'
    return t


def t_TEXT(t):
    r'\"[A-Za-z0-9]+\"'
    return t


def t_END(t):
    r'\s*\;'
    return t


def t_ONAW(t):
    r'\('
    return t


def t_ZNAW(t):
    r'\)'
    return t


def t_SPACE(t):
    r'\ '


lexer = lex.lex()

token_list = []

# Test the lexer
data = 'int s=3; double a = "bleee";'
lexer.input(data)
for token in lexer:
    token_list.append(token)
    print(token)
