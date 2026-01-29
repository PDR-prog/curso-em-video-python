from random import randint
from time import sleep
comp = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if jogador == comp:
    print('PARABÉNS! Você ganhou')
else:
    print('Você perdeu, eu pensei no número {} e não no número {}!' .format(comp,jogador))