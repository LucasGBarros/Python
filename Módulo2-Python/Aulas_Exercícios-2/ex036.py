print("""Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar
o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que não pode exceder 30% do salário ou então o empréstimo será negado.
""")
print('\033[7:29:40m=-=\033[m'*15)

casa = float(input('Qual o valor da casa? R$ '))

salario = float(input('Quanto voce recebe por mês de salário? R$ '))

ano = int(input('Quantos anos voce pretende terminar de pagar? '))

prestação = casa / (ano * 12)

minimo = salario * 30 / 100

if prestação <= minimo:

    print('\033[30:29:42mParabéns, voce comprou uma propriedade nova de R$ {:.2f}!! A sua parcela é de {} anos de R$ {:.2f} por mês.\033[m'.format(casa, ano, prestação))

else:

    print('\033[1:29:41mPara pagar uma casa de R$ {:.2f}, em {} anos, sua prestação será de R$ {:.2f} por mês. Seu empréstimo foi negado! Você não poderá comprar está casa no momento.\033[m'.format(casa, ano, prestação))

print('\033[7:29:40m=-\033[m'*15)