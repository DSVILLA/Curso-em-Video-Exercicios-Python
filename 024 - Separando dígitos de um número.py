n1 = int(input('Digite um número de 1 a 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
n = n1 // 1000 % 10
print('Analisando o número {}'.format(n1))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(n))
