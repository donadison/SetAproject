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


def var(type, id, number):
    variables[id.value] = (type.value, number.value)
    print("Zmienna typu", type.value, "nazwa", id.value, "wartość", number.value)
    print(variables)


polecenia = {
    'var': var,
}

def group_tokens(tokens):
    # tymczasowa lista na najblizsze polecenie
    temp = []
    for token in tokens:
        match token.type:
            case 'TYPE':
                stack.append('var')
                temp.append(token)
                # if info["next"] == 'Any':
                #     # info["group_start"] += 1
                #     # .append(token)
                #     # info["next"] = 'ID'
                #     # info["type"] = token.value
                #     # queue.append('var')
                # else:
                #     print("Blad skladniowy: 'TYPE'")
            case 'ID':
                if stack[-1] == 'var':
                    temp.append(token)
                # if info["next"] == 'ID':
                #     # temp.append(token)
                #     # info["next"] = 'EQ'
                # else:
                #     print("Blad skladniowy: 'ID'")
            case 'EQ':
                pass
                # if info["next"] == 'EQ':
                #     temp.append(token)
                #     info["next"] = 'VALUE'
                # else:
                #     print("Blad skladniowy: 'EQ'")
            case 'NUMBER':
                if stack[-1] == 'var':
                    temp.append(token)
                # if info["next"] == 'VALUE' and (info["type"] == 'int' or 'double'):
                #     temp.append(token)
                # #     # if queue[-1] == 'var':
                #
                # else:
                #     print("Blad skladniowy 'NUMBER'")
            case 'TEXT':
                if stack[-1] == 'var':
                    temp.append(token)
            case "NAMES":
                stack.append('suicidie')
            case _:
                print(token.type, token.value)
        if stack[-1] == 'var' and len(temp) == 3:
            queue.append(('var', temp))
            stack.pop()
            temp = []
    print(temp)


group_tokens(token_list)

for item in queue:
    name, params = item
    polecenia[name](*params)

print(stack)
print(queue)


"""
TYPE    :   sprawdź następne 3 tokeny ID EQ (NUMBER | TEXT | ZNAK), jeśli się zgadza zapisz zmienną
NAMEC   :   sprawdź tokeny w nawiasie do zamknięcia wszystkich nawiasów, czort wie ile, wydrukuj każdy jeśli jest TYPE etc
            w innym przypadku wywal błąd, bo można tylko wydrukować zmienną xd
NAMES   :   sprawdź następny token (NUMBER), zbierz zawartość nawiasów do listy i powiel zadaną ilość razy, następnie
            następnie przerób na tokeny

"""