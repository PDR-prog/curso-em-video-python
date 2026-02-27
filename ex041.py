from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.' .format(idade))
if idade <=9:
    print('CATEGORIA: MIRIM')
elif idade <=14:
    print('CATEGORIA: INFANTIL')
elif idade <=19:
    print('CATEGORIA: JÚNIOR')
elif idade <= 25:
    print('CATEGORIA: SÊNIOR')
else:
    print('CATEGORIA: MASTER')