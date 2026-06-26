viagem = float(input('Qual é a distancia da sua viagem: '))
print('Você está preste a começar uma viagem de {:.2f}Km'.format(viagem))
if viagem > 200:
    dis = viagem * 0.45
    print('E o preço da sua viagem sera de R${:.2f}'.format(dis))
else:
    Nor = viagem * 0.50
    print('E o preço da sua viagem será de R${:.2f}'.format(Nor))