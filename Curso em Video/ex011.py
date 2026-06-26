larg = float(input('Qual é a largura da parede?: '))
alt = float(input('Qual é a altura da parede?: '))
area = larg * alt
print('Sua parede tem as dimensão de {}X{} e sua area é de {:.3f}m² .'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(area / 2))