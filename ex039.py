from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
sexo = str(input('Qual o seu gênero? '))
idade = atual-nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if sexo == 'Feminino':
    print('Você não precisa se alistar.')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!!')
elif idade < 18:
    saldo = 18 - idade
    print('Faltam {} anos para o seu alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será no ano de {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(idade))
    ano = atual - saldo
    print('Seu alistamento foi no ano de {}'.format(ano))
