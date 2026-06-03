'''valores = []
for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))
maior = max(valores)
menor = min(valores)
posicao = valores.index(maior)
posicao2 = valores.index(menor)
print(f'O maior valor é {maior} e está na posição {posicao} e o menor valor é {menor}'
      f' e está na posição {posicao2}.')'''


listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i} ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i} ', end='')