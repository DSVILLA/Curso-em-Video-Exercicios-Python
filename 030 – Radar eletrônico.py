print('---- CHECK DE MULTAS ----')
velo = int(input('Digite a velocidade que você passou na via: '))
multa = (velo - 80) * 7.00
if velo <= 80:
    print('Você está dentro do limite da via!')

else:
    print('Você está acima do limite da via')
    print('Você tomou uma multa de {}, são 7 '
          'reais para cada 1km acima do permitido!'.format(multa))


