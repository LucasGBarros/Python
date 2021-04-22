import datetime

print('''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas são maiores''')

from datetime import date

atual = date.today().year

totmaior = 0

totmenor = 0

for pess in range(1, 8):

        ano = int(input('Em que ano a {}º nasceu? '.format(pess)))

        idade = atual - ano

        if idade >= 21:

            totmaior += 1   # += representa como "MAIS" de uma pessoa maior

        else:

            totmenor += 1   # += representa como "MAIS" de uma pessoa MENOR

print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))

print('E tambem tivemos {} pessoas menores de idade.'.format(totmenor))