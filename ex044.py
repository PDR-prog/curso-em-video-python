preço = float(input('Qual o preço do produto? R$'))
print('''Escolha uma forma de pagamento:
[ 1 ] À vista dinheiro ou cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual a opção? '))
if opção == 1:
    total = preço - (preço*10/100)
    print('O valor a ser pago é R${:.2f}' .format(total))
elif opção == 2:
    total = preço - (preço*5/100)
    print('O valor a ser pago é de R${:.2f}'.format(total))
elif opção == 3:
    total = preço
    parcela = total/2
    print('O valor a ser pago é de 2 parcelas de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço*20/100)
    totparc= int(input('Quantas parcelas? '))
    parcela = total/totparc
    print('O total a ser pago é de {} parcelas de {:.2f}'.format(totparc,parcela))
else:
    print('OPÇÃO DE PAGAMENTO INVÁLIDA, TENTE NOVAMENTE!')
