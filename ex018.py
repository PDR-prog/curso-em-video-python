'''import math
num = float(input('Qual o valor do ângulo? '))
seno = math.sin(math.radians(num))
coseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))
print('O seno, coseno e tangente de {}\n são respectivamente {}, {} e {}' .format(num,seno,coseno,tangente))'''

from math import sin,cos,tan,radians
ângulo = float(input('Digite um ângulo: '))
seno = sin(radians(ângulo))
print('O ângulo {} tem o SENO de {:.2f}' .format(ângulo,seno))
cosseno = cos(radians(ângulo))
print('O ãngulo {} tem o COSSENO de {:.2f}' .format(ângulo,cosseno))
tangente = tan(radians(ângulo))
print('O ângulo {} tem a TANGENTE de {:.2f}' .format(ângulo,tangente))
