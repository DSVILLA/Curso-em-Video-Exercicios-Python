print('======= CONVERSOR DE MOEDAS (USD/BRL) =======')
brl = float(input('Quantos reais deseja investir? : '))
conv = brl / 5.41
print('Com R$ {:.2f}, você pode comprar {:.2f}USD'.format(brl, conv))
print('A cotação atual do dollar está em R$ 5,41 para cada (1 USD) \nAcompanhe em tempo real em: https://dolarhoje.com/')
