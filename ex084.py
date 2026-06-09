'''pessoas = []
peso = []
while True:
    pessoas.append(str(input('Nome: ')))
    peso.append(float(input('Peso: ')))
    c = str(input('Quer continuar? [S/N] ')).upper().strip()
    while c not in 'NS':
        c = str(input('Digite S ou N:')).upper().strip()
    if c in 'N':
        break
pessoasQuant = len(pessoas)
print(f'Foram cadastradas {pessoasQuant} pessoas na lista.')
print(f'O maior peso cadastrado foi de {max(peso)} de ', end='')
for c in range(0, len(pessoas)):
    if peso[c] == max(peso):
        print(f'"{pessoas[c]}" ')
print(f'O menor peso cadastrado foi de {min(peso)} de ', end='')
for c in range(0, len(pessoas)):
    if peso[c] == min(peso):
        print(f'"{pessoas[c]}" ')'''


temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]} ', end='')
print()
