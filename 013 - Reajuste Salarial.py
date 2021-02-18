salario = float(input('Digite seu salário e veja seu novo salário com 15% de aumento: '))

salario_com_aumento = salario * 15
salario_novo = salario + salario_com_aumento

print('Você ganhou um aumento de RS{}, e seu novo salário agora é: RS{}'.format(salario_com_aumento, salario_novo))
