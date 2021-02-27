sal = float(input('Digite seu salário: '))
if sal <= 1.250:
    sal_novo = sal + ( sal * 15 / 100)
else:
    sal_novo = sal + ( sal * 15 / 100)
    print('Seu novo salário é de R${:.1f}'.format(sal_novo))
