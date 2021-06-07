print('''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.

No final, mostre uma listagem de preços organizando os dados em forma TABULAR.
''')


print('-'*50)

print(f'{"Listagem de Preço":^50}')

print('-'*50)

listagem = ('Pão', 2.50,
            'Arroz', 11.89,
            'Feijão', 10.40,
            'Queijo', 8,
            'Mortadela', 2.50)

for pos in range(0, len(listagem)):

    if pos % 2 == 0:

        print(f'{listagem[pos]:.<40}', end=' ') # Utilizando elemento par para identificar produto da lista.

    else:

        print(f'R${listagem[pos]:7.2f}') # Utilizando ímpar para identificar preço da lista.

print('-'*50)