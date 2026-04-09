soma = quant =  0
while True:
    num = int(input('Digite um número(999 para parar): '))
    if num == 999:
        break
    soma += num
    quant += 1
print(f'Foram digitados {quant} números e a soma entre eles é {soma}.')
