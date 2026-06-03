num = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    c = str(input('Quer continuar? [S/N] '))
    if c in 'Nn':
        break
num.sort()
listapar.sort()
listaimpar.sort()
print(f'Você digitou os valores {num}')
print(f'Os valores pares digitados foram {listapar}')
print(f'Os valores ímpares digitados foram {listaimpar}')



