print('-/-' * 20)
print(' Analisador de Triângulos')
print('-/-' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Estes segmentos podem formar um triângulo!')
else:
    print('Estes segmentos não formam um triângulo!')
