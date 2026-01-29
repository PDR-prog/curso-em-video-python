km = float(input('Quantos km o carro percorreu?'))
d = int(input('Por quantos dias o carro foi alugado?'))
preço = 60 * d + 0.15 * km
print('O preço a ser pago é de R${:.2f}.'.format(preço))