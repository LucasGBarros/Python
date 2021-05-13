print('''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

- Qual é o total gasto na compra.
- Quantos produtos custam mais de R$ 1000,00.
- Qual é o nome do produto mais barato.
''')
print('-' * 25)

print(f'{" LOJA ":=^25}')

print('-' * 25)

totalProd = caro = menor = cont = 0

barato = ''

while True:

    nome = str(input('Nome do Produto: '))

    preço = float(input(f'Valor do Produto: R$ '))

    cont += 1

    totalProd += preço

    if preço > 1000:

        caro += 1

    if cont == 1:

        menor = preço

    else:

        if preço < menor:

            menor = preço

            barato = nome

    resp = ' '

    while resp not in 'SN':

        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':

        break

print(f'{" Fim do Programa ":=^25}')

print(f'Total da compra: R$ {totalProd:.2f}.')

print(f'{caro} produtos foram acima do valor de R$ 1.000,00.')

print(f'Produto mais barato foi {barato} no valor de R$ {menor:.2f}.')
