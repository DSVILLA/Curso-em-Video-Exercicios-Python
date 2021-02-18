from math import hypot
print('==== SOMA DA HIPOTENUSA ====')

co = float(input('Digite o Cateto oposto: '))
ca = float(input('Digite o Cateto adjacente: '))
hi = hypot(co, ca)

print('O comprimento da Hipotenusa é: {:.2f}'.format(hypot(hi)))
