print("""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:

- Á vista DINHEIRO/CHEQUE: 10% de desconto.

- Á vista no CARTÃO: 5% de desconto.

- Em até 2x no CARTÃO DE CRÉDITOS: Preço normal.

- 3x ou mais no CARTÃO DE CRÉDITOS: 20% de juros.
""")

print('{:=^40}'.format('MERCADO'))

produto = float(input('Qual o valor do produto? '))

print("""O valor do produto é R$ {:.2f}, qual vai ser a a forma de pagamento?

[1] DINHEIRO / CHEQUE
[2] Débito
[3] 2x no cartão
[4] 3x ou mais no cartão
""".format(produto))

opcões = int(input('Digite a Opção que deseja: '))

if opcões == 1:

    desc = produto - (produto * 10 / 100)

    print('Pagando á VISTA, você ganha 10% de desconto. O valor do produto a ser pago agora é R$ {:.2f}'.format(desc))

elif opcões == 2:

    desc = produto - (produto * 5 / 100)

    print('Pagando no DÉBITO, você ganha 5% de desconto. O valor do produto a ser pago agora é R$ {:.2f}'.format(desc))

elif opcões == 3:

    parcela = produto / 2

    print('Sua compra será parcelada em 2x de R$ {}.'.format(parcela))

elif opcões == 4:

    parcelas = int(input('Quantas parcelas: '))

    juros = produto + (produto * 20 / 100)

    div = juros / parcelas

    print('Sua compra será parcelada em {:.0f}x de R$ {:.2f} COM JUROS.'.format(parcelas, div))

print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(produto,juros))

print('{:=^40}'.format('VOLTE SEMPRE'))