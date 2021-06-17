print('''Aprimore o desafio anterior, mostrando no final: 

A) A soma de todos os valores pares digitados.

B) A soma dos valores da 3 coluna.

C) O maior valor da segunda linha.
''')

print('=-'*30)

num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

par = maior = somcolu = 0

for l in range(0, 3):

    for c in range(0, 3):

        num[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('=-'*30)

for l in range(0, 3):

    for c in range(0, 3):

        print(f'[{num[l][c]:^5}]', end='')

        if num[l][c] % 2 == 0:

            par += num[l][c]

    print()

print('=-'*30)

print(f'A soma dos valores pares são: {par}.')

for l in range(0, 3):

    somcolu += num[l][2]

print(f'A soma dos valores da terceira coluna é de: {somcolu}.')

for c in range(0, 3):

    if c == 0:

        maior = num[1][c]

    elif num[1][c] > maior:

        maior = num[1][c]

print(f'O maior valor da segunda coluna é de: {maior}')

print('=-'*30)
