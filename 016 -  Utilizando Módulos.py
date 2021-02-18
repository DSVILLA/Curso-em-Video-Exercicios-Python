#Exemplo 1 usando import math

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))


#Exemplo 2 usando math.ceil

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))


#Exemplo 3 usando math.floor

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))


#Exemplo 4 usando from import math sqrt

from math import sqrt

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))



#Exemplo 5 usando from import math sqrt, floor

from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))



#Exemplo 6 usando import random para que a máquina me de números aleatorios.


import random
num = random.random()
print(num)



#Exemplo 6.1


import random
num = random.randint(1, 100)
print(num)


#Exemplo 7 Importando bibliotecas (Emoji)


import emoji
print(emoji.emojize("Olá Mundo :sunglasses:", use_aliases=True))
