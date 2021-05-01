print('''Faça um programa que leia um número qualquer e mostre o seu fatorial.

EX: 

5! = 5x 4 x 3 x 2 x 1 = 120
''')

# Usando função métodos.

from math import factorial

n = int(input('Digite um número para calcular seu fatorial: '))

fatorial = factorial(n)

print('O fatorial de {}! é de {}.'.format(n, fatorial))

# Usando função While

n = int(input('Digite um número para saber seu fatorial: '))

c = n

f = 1

print('Caculando {}! = '.format(n), end='')

while c > 0:

    print('{}'.format(c), end='')

    print(' x ' if c > 1 else ' = ', end='')

    f *= c

    c -= 1

print('{}'.format(f))

# Utilizando função for

n = int(input('Digite um número para saber seu fatorial: '))

c = 0

f = 1

for c in range(1, n):

    f *= n
    n -= 1

print('Seu fatorial é de {}'.format(f))