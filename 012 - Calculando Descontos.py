produto = float(input('Digite o preço do produto para calcular o novo valor com 5% de desconto: '))

desconto = produto * 5 / 100
valor_com_desconto = produto * 95
print('Você ganhou R${} em descontos, o novo valor com desconto agora é: R${:.3f}'.format(desconto, valor_com_desconto))
