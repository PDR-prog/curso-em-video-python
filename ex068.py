from random import randint
print('-'*30)
print('PAR OU ÍMPAR')
print('-'*30)
v = 0
while True:
    jogador = int(input('Escolha um número: '))
    computador = randint(0, 11)
    total = jogador+computador
    tipo = ' '
    while tipo not in 'PIÍ':
        tipo = str(input('PAR OU ÍMPAR? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total deu {total}')
    print(f'Deu par' if total % 2 == 0 else 'Deu ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu! Parabéns!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu! Parabéns!')
            v += 1
        else:
            print('Você perdeu!')
            break
print(f'GAME OVER! Você venceu {v} vezes')