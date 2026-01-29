rs = float(input('Quantos reais você tem na carteira? R$'))
do= rs / 5.52
eu= rs / 6.47
print('Com R${:.2f} você poderá comprar\n US${:.2f} e\n €{:.2f}' .format(rs,do,eu))
