'''import math
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
co2= math.pow(co,2)
ca2= math.pow(ca,2)
hip2= co2 + ca2
hip= math.sqrt(hip2)
print('A hipotenusa é igual a {}' .format(hip))'''

'''co=float(input('Cateto oposto: '))
ca=float(input('Cateto adjacente: '))
hip= (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é igual a {}'.format(hip))'''

from math import hypot
co= float(input('Qual o valor do cateto oposto? '))
ca= float(input('Qual o valor do cateto adjacente? '))
hip= hypot(co,ca)
print('A hipotenusa é igual a {}' .format(hip))
