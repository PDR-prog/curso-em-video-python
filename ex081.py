lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    c = str(input('Quer continuar? [S/N] '))
    if c in 'Nn':
        break
print('=-' * 30)
print(f'Quantidade de valores digitados na lista: {len(lista)} valores.')
print('=-' * 30)
print(f'Lista ordenada de forma decrescente: {sorted(lista, reverse=True)}')
print('=-' * 30)
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')

'''if 5 in lista:
    quant = lista.count(5)
    print(f'O valor 5 foi digitado e aparece {quant} vezes na lista')
else:
    print('O valor 5 não foi digitado')'''