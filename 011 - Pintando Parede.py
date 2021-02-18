larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite o comprimento da parede: '))

area = larg * alt
print('Sua parede tem a dimensão de {} X {} e sua área é de {:.2f}m'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(tinta))
