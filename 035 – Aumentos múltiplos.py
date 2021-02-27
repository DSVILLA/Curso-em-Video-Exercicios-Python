sal = float(input('Digite seu salário: '))
if sal > 1.250:
    sal_10 = sal * 0.10
    print('Seu novo salário é de R${:.1f}'.format(sal_10+sal))

else:
    sal_15 = sal * 0.15
    print('Seu novo salário é de R${:.1f}'.format(sal_15+sal))
