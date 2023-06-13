import ply.lex as lex
import ply.yacc as yacc

# tokeny
tokens = (
    'TYPE',
    'EQ',
    'SUM',
    'ASUM',
    'POW',
    'DIV',
    'NUMBER',
    'TEXT',
    'ONAW',
    'ZNAW',
    'SPACE',
)


def t_TYPE(t):
    r'\ int|double\ '
    return t


def t_EQ(t):
    r'\='
    return t


# def t_SUM(t):
#     r'\+'
#     return t
#
#
# def t_ASUM(t):
#     r'\-'
#     return t
#
#
# def t_POW(t):
#     r'\*'
#     return t
#
#
# def t_DIV(t):
#     r'\/'
#    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t


def t_TEXT(t):
    r'[A-Za-z0-9]+'
    return t


# def t_ONAW(t):
#     r'\('
#     return t
#
#
# def t_ZNAW(t):
#     r'\)'
#     return t


def t_SPACE(t):
    r'\ +'
    return t


# słownik na zmienne
variables = {}


def p_var(p):
    """
    expression  : TYPE SPACE TEXT SPACE EQ SPACE NUMBER SPACE
    """
    v_type = p[1]
    v_name = p[3]
    v_value = p[7]

    print("Zmienna typu ", v_type, " nazwa ", v_name, " wartość ", v_value)


# reguły gramatyczne
def p_expression(p):
    """
    expression  : NUMBER
                | TEXT
    """
    p[0] = p[1]

    print("liczba lub tekst", p[0])


#
# def p_codes(p):
#     """
#     expression  : NAMES SPACE+ NUMBER SPACE+ ONAW SPACE* helper* SPACE* ZNAW SPACE*
#     """
#     n = p[3]
#     for i in range(n):
#         p[7]

#
# def p_codec(p):
#     """
#     expression  : NAMEC SPACE+ ONAW SPACE* types SPACE* ZNAW SPACE*
#     """


lexer = lex.lex()
parser = yacc.yacc()

# Test the lexer
data = "integral"
lexer.input(data)
for token in lexer:
    print(token)

result = parser.parse(data, lexer=lexer)
print(result)
