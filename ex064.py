n = cont = soma = 0
n = int(input('Digite um número [999 pra parar] '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 pra parar] '))
print(f'Você digitou {cont} números e a soma entre eles é {soma} ')
