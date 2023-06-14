from simpleegothic_v3 import token_list
from collections import deque

token_list = deque(token_list)

# słownik na zmienne
variables = {}

# "kolejka" na polecenia
# "append" i "popleft"
queue = []

# stos na coś na pewno
# "append" i "pop"
stack = deque()
#
# info = {
#     "group_start": 0,
#     "group_end": 0,
#     "next": 'Any',
#     "type": 'Any'
# }

syntax_dict = {
    'var': [
        ['TYPE', 'ID', 'EQ', 'NUMBER', 'END'],
        ['TYPE', 'ID', 'EQ', 'DOUBLE', 'END'],
        ['ST', 'ID', 'EQ', 'TEXT', 'END'],
        ['ST', 'ID', 'EQ', 'ZNAK', 'END'],
        ['CH', 'ID', 'EQ', 'ZNAK', 'END']
    ],
    'codec': ['NAMEC', 'ONAW', 'var', 'ZNAW', 'END'],
    'codes': ['NAMES', 'NUMBER', 'ONAW', 'any', 'ZNAW', 'END']
}


def validate_syntax(function, tokens):
    syntax = syntax_dict[function]
    match = []
    if function == 'var':
        # todo powinien wykrywać string f = "d"; jako poprawnego stringa a tego nie robi, do naprawy XD
        for i, option in enumerate(syntax):
            m = [(token.type == tk) for token, tk in zip(tokens, option)]
            if False in m:
                pos = m.index(False)
                err = tokens[pos]
                match.append(err)
            else:
                return True
            err = min(tokens, key=lambda token: token.lexpos)
            if err == tokens[0]:
                err = tokens[3]
            # todo przerobić to na wyjątek, bo inaczej nie wyrobimy na ilość linii kodu XD
            return err

    if function == 'codec':
        syntax = syntax_dict['codec']
        # todo błagam napisać to bardziej po ludzku, pewnie w jakiejś pętli, bo mnie aż oczy bolą od tego potórzenia
        last = len(tokens)
        part1 = tokens[:2]
        part2 = tokens[2:last-2]
        part3 = tokens[last-2:]
        last = len(syntax)
        syntax1 = syntax[:2]
        syntax3 = syntax[last - 2:]

        match1 = [(token.type == tk) for token, tk in zip(part1, syntax1)]
        match3 = [(token.type == tk) for token, tk in zip(part3, syntax3)]
        match2 = []
        for li in part2:
            m = validate_syntax('var', li)

    if function == 'codes':
        print("też w budowie")


def var(tokens):
    match = validate_syntax('var', tokens)
    v_type = tokens[0].value
    v_name = tokens[1].value
    v_value = tokens[3].value

    if match is True:
        variables[v_name] = (v_type, v_value)
        print('Zmienna typu', v_type, 'nazwa', v_name, 'wartość', v_value)
    else:
        if match == tokens[3]:
            print('Syntax error at line', match.lineno, 'position', match.lexpos, ': "', v_value,
                  '" is not a valid', v_type)
        else:
            print('Syntax error at line', match.lineno, 'position', match.lexpos, ':', match)


def codec(tokens):
    validate_syntax('codec', tokens)
    print("codec")
    print(tokens)


polecenia = {
    'var': var,
    'codec': codec,
}


def group_tokens(tokens):
    # tymczasowa lista na najblizsze polecenie
    temp = []
    while len(tokens) > 0:
        token = tokens.popleft()
        match token.type:
            case 'TYPE' | 'CH' | 'ST':
                while token.type != 'END':
                    temp.append(token)
                    token = tokens.popleft()
                temp.append(token)
                queue.append(('var', *temp))
                temp.clear()
            case 'END':
                print(token, "END")
            case 'NAMEC':
                templist = []
                start = token
                temp.append(token)
                token = tokens.popleft()
                while token.type != 'END':
                    while token.type != 'ZNAW':
                        if token.type == 'ONAW':
                            stack.append(token)
                            temp.append(token)
                        elif token.type == 'END':
                            templist.append(token)
                            temp.append([*templist])
                            templist.clear()
                        else:
                            templist.append(token)
                        token = tokens.popleft()
                    stack.pop()
                    temp.append(token)
                    token = tokens.popleft()
                temp.append(token)
                queue.append(('codec', *temp))
                temp.clear()
            case _:
                print("Syntax error")


print("******")
group_tokens(token_list)

for item in queue:
    params = item[1:]
    name = item[0]
    # print(name, params)
    polecenia[name](params)
    validate_syntax(name, params)

# print(stack)
# print(queue)

"""
TYPE    :   sprawdź następne 3 tokeny ID EQ (NUMBER | TEXT | ZNAK), jeśli się zgadza zapisz zmienną
NAMEC   :   sprawdź tokeny w nawiasie do zamknięcia wszystkich nawiasów, czort wie ile, wydrukuj każdy jeśli jest TYPE etc
            w innym przypadku wywal błąd, bo można tylko wydrukować zmienną xd
NAMES   :   sprawdź następny token (NUMBER), zbierz zawartość nawiasów do listy i powiel zadaną ilość razy, następnie
            następnie przerób na tokeny

"""
