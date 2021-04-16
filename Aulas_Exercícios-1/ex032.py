from datetime import date

print('Faça um programa que leia um ano qualquer e mostre se que ele é bissexto.')

ano = int(input('Digite um ano e direi se ele é Bissexto: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

    print('O ano {} informado é Bissexto.'.format(ano))

else:

    print('O ano {} informado não é bissexto.'.format(ano))