gastTot = prodMil = prodBara = cont = 0
barato = ' '
while True:
    nome = str(input('NOME DO PRODUTO: '))
    preco = float(input('PREÇO: R$'))
    cont += 1
    gastTot += preco
    if preco > 1000:
        prodMil += 1
    if cont == 1:
        prodBara = preco
        barato = nome
    else:
        if preco < prodBara:
            prodBara = preco
            barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total gasto foi de R${gastTot:.2f}.')
print(f'Ao todo tem {prodMil} produtos que custaram mais de R$1000.')
print(f'O produto mais barato foi {barato} e custou {prodBara}')