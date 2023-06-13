import ply.lex as lex
import ply.yacc as yacc

# tokeny
tokens = (
    'ID',
    'TYPE',
    'CH',
    'ST',
    'NAMES',
    'NAMEC',
    'EQ',
    'SUM',
    'ASUM',
    'POW',
    'DIV',
    'NUMBER',
    'TEXT',
    'ONAW',
    'KOT',
    'ZNAW',
    'SPACE',
    'END',
)

states = (
  ('kot', 'exclusive'),
)


def t_TYPE(t):
    r'int|double\ '
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


def t_EQ(t):
    r'\s*=\s*'
    return t


def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z0-9]+'
    return t


def t_TEXT(t):
    r'\"[A-Za-z0-9]+\"'
    return t


def t_END(t):
    r'\s*\~'
    return t


# znaleziony otwierający nawias
def t_ONAW(t):
    r'\('
    t.lexer.code_start = t.lexer.lexpos  # zapisuje pozycję, do której wrócić
    t.lexer.level = 1  # wchodzi w pierwszy poziom nawiasów
    t.lexer.begin('kot')   # wchodzi w stan "kot"


# zasady w zagnieżdżonym kodzie

# lewy nawias
def t_kot_ONAW(t):
    r'\('
    t.lexer.level += 1


# nawias zamykajacy
def t_kot_ZNAW(t):
    r'\)'
    t.lexer.level -= 1

    # zewnetrzny nawias zamykajacy
    if t.lexer.level == 0:
        t.value = t.lexer.lexdata[t.lexer.code_start:t.lexer.lexpos - 1]
        t.type = "KOT"
        t.lexer.lineno += t.value.count('\n')
        t.lexer.begin('INITIAL')
        return t


def t_kot_RANDOM(t):
    r'.'
    pass


def t_ZNAW(t):
    r'\)'
    return t


def t_SPACE(t):
    r'\ '
    return t


lexer = lex.lex()

# Test the lexer
data = "suicide 3 (int a = 666)~"
lexer.input(data)
for token in lexer:
    print(token)

# słownik na zmienne
variables = {}


def p_codes(p):
    """
    loop    : NAMES SPACE NUMBER SPACE kot END
    """
    n = int(p[3])
    code = p[5]
    print(n, " ", code)
    for i in range(n):
        print(i)
        print(code)
        res = parser.parse(code)
        print(res)


def p_kot(p):
    """
    kot     : KOT
            | var
            | expression
            | loop
    """
    p[0] = str(p[1])


def p_var(p):
    """
    var         : TYPE SPACE ID EQ expression
                | CH SPACE ID EQ expression
                | ST SPACE ID EQ expression
    """
    v_type = p[1]
    v_name = p[3]
    v_value = p[5]
    p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4]) + str(p[5])

    variables[v_name] = (v_type, v_value)

    print("Zmienna typu ", v_type, " nazwa ", v_name, " wartość ", v_value)
    print(variables)


def p_expression(p):
    """
    expression  : NUMBER
                | TEXT
    """
    p[0] = p[1]

    if isinstance(p[0], (int, float, complex)):
        print(p[0], " jest liczbą")
    elif isinstance(p[0], str):
        print(p[0], " jest stringiem")
    else:
        print(p[0], "co ty żeś debilu wpisał jebany xD")

    return p[0]


parser = yacc.yacc()

result = parser.parse(data, lexer)
print(result)
