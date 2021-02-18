dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))

diaria = 60 * dias
kms = 0.15 * km
total = diaria + kms
print('O total a pagar é de R${:.2f}.'.format(total))
