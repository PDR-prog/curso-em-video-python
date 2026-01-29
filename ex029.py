'''vel = float(input('Qual a velocidade atual do carro? '))
multa = (vel-80) * 7
if vel <= 80.0:
    print('Tenha um bom dia! Dirija com segurança')
else:
    print('MULTADO! Você ultrapassou o limite de velocidade que era de 80km/h!')
    print('Você terá que pagar uma multa no valor de R${:.2f}' .format(multa))
    print('Tenha um bom dia! Dirija com segurança')'''

vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80km/h.')
    multa = (vel-80) * 7
    print('Você terá que pagar uma multa no valor de R${:.2f}.' .format(multa))
print('Tenha um bom dia! Dirija com segurança')