from random import randint
from time import sleep
computador = randint(0, 5)
print('-/-' * 20)
print('TENTE ADIVINHAR O NÚMERO ESCOLHIDO DE 0 a 5!')
print('-/-' * 20)
print('PROCESSANDO...')
sleep(4)

a = int(input('Qual número escolhido? '))

if a == computador:
    print('Você acertou o número!')
else:
    print('Não é este número, tente de novo!')

