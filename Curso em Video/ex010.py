cart = float(input('Quanto de dinheiro você tem na sua carteira?: R$'))
dol =  cart / 5.30
print('Com R${:.2f} você pode comprar ${:.2f}'.format(cart, dol))