produto = float(input('Digite o preço do produto e conheça as formas de pagamentos a vista e parcelado: '))

preco_vista = produto - (produto * 10 /100)
preco_parcelado = produto + (produto * 8 / 100)
print('A vista o pagamento será R${} com 10% de desconto'.format(preco_vista))
print('Parcelado o pagamento sofrerá um aumento de 8%, sendo o novo valor de: R${}'.format(preco_parcelado))
