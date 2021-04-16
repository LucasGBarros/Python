from math import trunc

print("""Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua posição inteira.

EX: DIGITE UM NÚMERO: 6.127
O número 6.127 tam a parte inteira de 6.""")

num = float(input('Digite um número: '))

p = trunc(num)

print('O número {:.3f} tem a parte inteira {}.'.format(num, trunc(num)))
