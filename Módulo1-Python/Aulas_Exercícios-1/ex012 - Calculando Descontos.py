print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')

p = float(input('Qual o preço do produto? R$ '))

novo = p - (p * 5 / 100)

print('O produto que custava {:.2f}, com 5% de desconto está por {:.2f}.'.format(p, novo))