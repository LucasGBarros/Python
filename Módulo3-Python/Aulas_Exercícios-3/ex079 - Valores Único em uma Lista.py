print('''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
''')

num = []

while True:

    n = int(input('Digite um valor: '))

    if n not in num:

        num.append(n)

        print(f'O número {n} digitado, foi adicionado.')

    else:

        print('Este número está repetido, tente novamente.')

    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

    if r in 'N':

        break

num.sort()

print(f'Você digitou os valores: {num}')