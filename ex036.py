casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o salário do comprador? R$'))
anos = float(input('Em quantos anos a casa vai ser financiada? '))
prestação = casa / (anos * 12)
mínimo = salário * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}' .format(casa,anos,prestação))
if prestação <= mínimo:
    print('Empréstimo CONCEDIDO')
else:
    print('Empréstimo NEGADO')
