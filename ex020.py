from random import sample
num1= input('Primeiro aluno: ')
num2 = input('Segundo aluno: ')
num3 = input('Terceiro aluno: ')
num4 = input('Quarto aluno: ')
lista = [num1,num2,num3,num4]
ordem = sample(lista, 4)
print('a ordem de apresentação será', ordem)

'''from random import shuffle
num1= input('Primeiro aluno: ')
num2 = input('Segundo aluno: ')
num3 = input('Terceiro aluno: ')
num4 = input('Quarto aluno: ')
lista = [num1,num2,num3,num4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)'''