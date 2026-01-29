'''cid = str(input('Digite o nome de uma cidade: '))
print ('Santo' in cid)'''

cid = str(input('Digite o nome de uma cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')
