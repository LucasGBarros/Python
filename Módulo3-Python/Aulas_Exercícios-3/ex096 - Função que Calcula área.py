print("""Faça um programa que tenha uma função chamada área(), que receba as dimenções de um terreno retangular
{largura e comprimento} e mostre a área do terreno.""")
print()


def área(larg, compr):

    a = larg * compr

    print(f'A dimensão da área de {larg}x{compr} é de {a}m².')

print('-'*40)
print(f'{" Controle de Terreno ":=^40}')
print('-'*40)

l = float(input('Largura (m): '))

c = float(input('Comprimento (m): '))

print()

print('-'*40)

área(l, c)