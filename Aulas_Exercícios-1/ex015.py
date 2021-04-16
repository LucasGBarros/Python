print("""Escreva um programa que pergunte a quantidade de km percorridos por um carro e a quantidade
        de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
        por dia e R$0,15 por km rodado.""")

dias = float(input('Quantos dias alugado? '))

km = float(input('Quantos Km rodado? '))

dias = dias * 60

km = km * 0.15

pago = dias + km

print('O valor total a pagar é de: {:.2f}'.format(pago))

# Correção

dias = int(input('Quantos dias alugado? '))

km = float(input('Quantos Km rodados? '))

pago = (dias * 60) + (km * 0.15)

print('O valor a ser pago é de {:.2f} Reais'.format(pago))