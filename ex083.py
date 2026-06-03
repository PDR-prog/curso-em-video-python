expres = str(input('Digite uma expressão numérica: '))
while True:
    if expres.count('(') == expres.count(')'):
        print('Expressão válida!')
    else:
        print('Expressão inválida!')
    break





expres = []
while True:
    e = str(input('Digite uma expressão numérica: '))
    expres.append(e)
    if e.count('(') == e.count(')'):
        print('Expressão válida!')
    else:
        print('Expressão inválida!')
    break