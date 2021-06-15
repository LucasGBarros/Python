print('''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:

- Quantos números foram digitados.

- A lista de valores, ordenada de forma decrescente.

- Se o valor 5 já foi digitado ou não na lista.
''')

print('-'*50)
print()

num = []

while True:

    num.append(int(input('Digite um valor: ')))

    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if r in 'N':

        break

print('-'*50)

print(f'Você digitou {len(num)} elementos.')        # Identificando quantos elementos está na lista.

num.sort(reverse=True)      # Método de inverter a ordem.

print(f'Os valores na ordem decrescente são: {num}')        # Valores invertidos.

if 5 in num:        # Indentificando se o número desejado está na lista.

    print('O valor 5 faz parte da lista!')

else:

    print('O valor 5 não faz parte da lista!')

print('-'*50)