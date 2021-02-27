print('--- Custo da Viagem ---')
a = int(input('Digite a quantidade de KM que você vai pecorrer: '))

if a <= 200:
    valor1 = 0.50 * a
    print('Sua passagem custará: R${}'.format(valor1))

else:
    valor2 = 0.45 * a
    print('Sua passagem custará: R${}'.format(valor2))
