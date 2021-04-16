print('Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.')

print('------TABUADA------')
# DECLARANDO VARIÁVEL
tabuada = int(input('Tabuada: '))

n1 = tabuada * 1
n2 = tabuada * 2
n3 = tabuada * 3
n4 = tabuada * 4
n5 = tabuada * 5
n6 = tabuada * 6
n7 = tabuada * 7
n8 = tabuada * 8
n9 = tabuada * 9
n10 = tabuada * 10

print('A tabuada de {} é: '.format(tabuada))
print('{} x  1 = {}'.format(tabuada, n1))
print('{} x  2 = {}'.format(tabuada, n2))
print('{} x  3 = {}'.format(tabuada, n3))
print('{} x  4 = {}'.format(tabuada, n4))
print('{} x  5 = {}'.format(tabuada, n5))
print('{} x  6 = {}'.format(tabuada, n6))
print('{} x  7 = {}'.format(tabuada, n7))
print('{} x  8 = {}'.format(tabuada, n8))
print('{} x  9 = {}'.format(tabuada, n9))
print('{} x 10 = {}'.format(tabuada, n10))


# Sem declaraçao de Variavel

num = int(input('A tabuada de: '))

print('-'*12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-'*12)