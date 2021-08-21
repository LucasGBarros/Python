print("""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salário superiores a R$ 1.250,00, calcule um aumento de 10%.

para os inferiores ou iguais, o aumento é de 15%""")

salario = float(input('Digite seu salário: R$ '))

if salario <= 1.250:

    salnov = salario + (salario * 15 / 100)

else:

    salnov = salario + (salario * 10 / 100)

print('Seu salário de R$ {:.2f} teve um aumento e agora você receberá R$ {:.2f}. Parabéns!!!'.format(salario, salnov))