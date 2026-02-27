print ('-=-'*10)
print ('Analisador de Triângulos')
print ('-=-'*10)
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a+b>c and a+c>b and b+c>a:
    print('As retas acima podem formar um triângulo', end=' ')
    if a==b==c:
        print('Equilátero!')
    elif a!=b!=c!=a:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('As retas acima NÃO PODEM FORMAR um triãngulo')
