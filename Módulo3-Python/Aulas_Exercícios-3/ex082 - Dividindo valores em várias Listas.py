print('''Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares 
digitados respectivamente.

Ao final , mostre o conteúdo das três listas geradas.
''')

valores = []
pares = []
impares = []

while True:

    valores.append(int(input('Digite um número: ')))

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if resp in 'N':

        break

for i, v in enumerate(valores):

    if v % 2 == 0:

        pares.append(v)     # Acrescentando o valores da lista completa em pares.

    else:

        impares.append(v)   # Acrescentando os valores da lista completa em impares.

print(f'A lista completa é {valores}')

print(f'A lista de valores PARES são: {pares}')

print(f'A lista de valores IMPARES são: {impares}')
