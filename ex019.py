from random import choice
num1= input('Primeiro aluno: ')
num2 = input('Segundo aluno: ')
num3 = input('Terceiro aluno: ')
num4 = input('Quarto aluno: ')
lista = [num1,num2,num3,num4]
sorteado = choice(lista)
print('O aluno escolhido foi {}' .format(sorteado))
