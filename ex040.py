n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {}.'.format(m))
if m < 5:
    print('Você foi REPROVADO! Estude mais.')
elif m > 7:
    print('PARABÉNS! VOCÊ PASSOU.')
else:
    print('Você está de RECUPERAÇÃO! Se esforce para passar.''')

