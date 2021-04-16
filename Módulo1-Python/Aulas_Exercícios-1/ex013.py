print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salpario, com 15% de aumento.')

salario = float(input('Qual o salário do funcionário? R$ '))

novo = salario + (salario * 15 / 100)

print('O salário do funcionário era de R${:.2f}, para 15% de aumento, foi reajustado para R${:.2f}'.format(salario, novo))