listanum = []
while True:
    n = int(input('Digite um valor: '))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor existente! Não vou adicionar.')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
listanum.sort()
print(f'Os valores digitados foram {listanum}')