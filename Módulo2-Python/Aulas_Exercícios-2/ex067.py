print('''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.

O programa será interrompido quando o número for negativo.
''')

print(f'{" TABUADA ":=^25}')

while True:

    n = int(input('Tabuada de: '))

    print('~' * 25)

    if n < 0:

        break

    for c in range(1, 11):

        print(f'{n} x {c} = {n * c}')

    print('~' * 25)

print('Tabuada encerrada.')