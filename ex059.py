from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
resp = 0
while resp != 5:
    print('''[ 1 ]Somar
[ 2 ]Multiplicar
[ 3 ]Maior
[ 4 ]Novos números
[ 5 ]Sair do programa''')
    resp = int(input('Escolha uma opção: '))
    if resp == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}.'.format(n1, n2, soma))
    elif resp == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é igual a {}.'.format(n1, n2, mult))
    elif resp == 3:
        if n1 == n2:
            print('Os dois valores são iguais')
        else:
            maior = max(n1, n2)
            print('O maior valor é {}.'.format(maior))
    elif resp == 4:
        print('Digite novos valores: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif resp == 5:
        print('Finalizando programa...')
        sleep(3)
        print('Programa finalizado!')
    else:
        print('Erro! Tente de novo')
    print('=-=' * 10)
