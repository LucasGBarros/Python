print('''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:

- A média de idade do grupo.

- Qual é o nome do homem mais velho.

- Quantas mulheres tem menos de 20 anos.
''')

soma = 0

media = 0

maioridadehomem = 0

nomevelho = 0

totmulher20 = 0

for p in range(1, 5):

    print('----- {}º PESSOA -----'.format(p))

    nome = str(input('Qual é o seu nome? ')).strip()

    idade = int(input('Qual é a sua idade? '))

    sexo = str(input('Sexo [M/F]: ')).strip()

    soma += idade

    if p == 1 and sexo in 'Mm':

        maioridadehomem = idade

        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadehomem:

        maioridadehomem = idade

        nomevelho = nome

    if sexo in 'Ff' and idade < 20:

        totmulher20 += 1

media = soma / 4

print('A média de idade do grupo é de {:.1f} anos'.format(media))

print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))

print('Ao todo são {} Mulheres com menos de 20 anos'.format(totmulher20))