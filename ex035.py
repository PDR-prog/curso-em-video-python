print ('-=-'*10)
print ('Analisador de Triângulos')
print ('-=-'*10)
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a+b>c and a+c>b and b+c>a:
    print('As retas acima podem formar um triângulo')
else:
    print('As retas acima NÃO PODEM FORMAR um triãngulo')
