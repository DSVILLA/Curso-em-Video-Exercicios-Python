a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

#verificando o menor número

menor = a
if b <a and c < b:
    menor = b
if c < a and c < b:
    menor = c

#verificando maior número

maior =a
if b > a and c > b:
    maior = b
if c > a and c > b:
    maior = c

print('O menor número foi {}:'.format(menor))
print('O maior número foi {}:'.format(maior))
