from random import randint
tentativas = 0
comp = randint(0,10)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
jogador = int(input('Qual é o seu palpite? '))
while jogador != comp:
    tentativas += 1
    if jogador < comp:
        print('Errado! Tente de novo.')
    else:
        print('Errado! Tente de novo')
    jogador = int(input('Digite seu palpite: '))
tentativas += 1
print('Parabéns!!! Você acertou')
print('Você tentou {} vezes até acertar.'.format(tentativas))