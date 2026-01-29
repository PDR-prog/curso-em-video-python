n1=int(input('\033[1;4mDigite um valor:'))
n2: int=int(input('Digite outro valor:\033[m'))
s=n1+n2
print('A soma entre \033[32m{}\033[m e \033[33m{}\033[m vale, \033[034m{}' .format(n1,n2,s))
