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



#Exemplo 4 usando from import math sqrt, floor

from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))
