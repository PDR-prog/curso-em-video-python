n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n),end='')
while c > 0:
    print('{}'.format(c,),end='')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print('{}'.format(f))


'''n = int(input('Digite um número para calcular seu fatorial: '))
f2 = 1
for c in range(1, n+1):
    f2 *= c
print('O resultado de {}! é {}'.format(n,f2))'''