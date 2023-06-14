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

info = {
    "group_start": 0,
    "group_end": 0,
    "next": 'Any',
    "type": 'Any'
}


def var(tokens):
    syntax = ['TYPE', 'ID', 'EQ', 'NUMBER']
    match = [(token.type == synt) for token, synt in zip(tokens, syntax)]
    print(match)
    if False in match:
        print("Syntax error:", tokens[3].value, 'is not a valid', tokens[0].value)
    else:
        v_type = tokens[0].value
        v_name = tokens[1].value
        v_value = tokens[3].value
        print('Zmienna typu', v_type, 'nazwa', v_name, 'wartość', v_value)


polecenia = {
    'var': var,
}


def group_tokens(tokens):
    # tymczasowa lista na najblizsze polecenie
    temp = []
    while len(tokens) > 0:
        token = tokens.popleft()
        match token.type:
            case 'TYPE':
                while token.type != 'END':
                    temp.append(token)
                    token = tokens.popleft()
                queue.append(('var', *temp))
                temp.clear()
            case 'END':
                print(token, "END")
            case 'NAMEC':
                token = tokens.popleft()
                while token.type != 'END':
                    if token.type == 'ONAW':
                        stack.append(token)
                    while token.type != 'ZNAW':
                        token = tokens.popleft()
                        if token.type != 'END':
                            temp.append(token)
                        else:
                            queue.append(('var', temp))
                            queue.append(('codec', temp))
                            temp.clear()
                    stack.pop()
            case _:
                print("Syntax error")


group_tokens(token_list)

for item in queue:
    params = item[1:]
    name = item[0]
    # print(name, params)
    polecenia[name](params)

# print(stack)
# print(queue)

"""
TYPE    :   sprawdź następne 3 tokeny ID EQ (NUMBER | TEXT | ZNAK), jeśli się zgadza zapisz zmienną
NAMEC   :   sprawdź tokeny w nawiasie do zamknięcia wszystkich nawiasów, czort wie ile, wydrukuj każdy jeśli jest TYPE etc
            w innym przypadku wywal błąd, bo można tylko wydrukować zmienną xd
NAMES   :   sprawdź następny token (NUMBER), zbierz zawartość nawiasów do listy i powiel zadaną ilość razy, następnie
            następnie przerób na tokeny

"""
