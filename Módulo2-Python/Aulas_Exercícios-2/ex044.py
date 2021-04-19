print("""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
- Á vista DINHEIRO/CHEQUE: 10% de desconto.
- Á vista no CARTÃO: 5% de desconto.
- Em até 2x no CARTÃO DE CRÉDITOS: Preço normal.
- 3x ou mais no CARTÃO DE CRÉDITOS: 20% de juros.
""")

print('{:=^40}'.format('MERCADO'))

preço = float(input('Qual o valor do produto? R$ '))

print('''FORMA DE PAGAMENTO
[1] DINHEIRO / CHEQUE
[2] Débito
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opção = int(input('Qual é a opção? '))

if opção == 1:

    total = preço - (preço * 10 / 100)

elif opção == 2:

    total = preço - (preço * 5 / 100)

elif opção == 3:

    total = preço

    parcela = total / 2

    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))

elif opção == 4:

    total = preço + (preço * 20 / 100)

    totalparc = int(input('Quantas Parcelas? '))

    parcela = total / totalparc

    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totalparc, parcela))

else:

    total = 0

    print('Opção inválida de pagamento. Tente novamente!')

print('Sua compra de R$ {:.2f}, vai custar R$ {:.2f} no final.'.format(preço, total))

print('{:=^40}'.format('VOLTE SEMPRE'))