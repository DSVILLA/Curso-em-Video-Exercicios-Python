frase = str(input('Digite seu nome e sobrenome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maisculo é: {}'.format(frase.upper()))
print('Seu nome em minusculo é: {}'.format(frase.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(frase) - frase.count(' ')))

#print('Seu primeiro nome tem {} letras.'.format(frase.find(' ')))
separa = frase.split()
print('Seu primeiro nome é {}, e ele tem {} letras.'.format(separa[0], len(separa[0])))

