print('-' * 30)
print('CADASTRE UMA PESSOA')
print('-' * 30)
tot18 = totH = totM20 = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F] ')).strip().upper()[0]
    if idade >18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Tem {tot18} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {totH} homens.')
print(f'Tem {totM20} mulheres com menos de 20 anos.')