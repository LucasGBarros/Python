print('''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 

A) Quantas pessoas foram cadastradas.

B) Uma listagem com as pessoas mais pesadas.

C) Uma listagem com pessoas mais leves.
''')
print('-'*50)
print()
print(f'{" Cadastro ":-^50}')

temp = list()

princ = list()

maior = menor = 0

while True:

    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:

        maior = menor = temp[1]

    else:

        if temp[1] > maior:

            maior = temp[1]

        if temp[1] < menor:

            menor = temp[1]

    princ.append(temp[:]) # Adicionando os dados adquiridos na estrutura "PESSOAS"

    temp.clear()

    print('-'*50)

    r = str(input('Deseja continuar? [S/N] ')).upper().strip()

    print('-'*50)

    if r in 'N':

        break

print(f'Foram cadastradas {len(princ)} pessoas')


print(f'Listagem de pesos maiores: {maior}Kg. Peso de ', end='')

for p in princ:

    if p[1] == maior:

        print(f'[{p[0].title()}] ', end='')

print()

print(f'Listagem de peso menores {menor}Kg. Peso de ', end='')

for p in princ:

    if p[1] == menor:

        print(f'[{p[0].title()}] ', end='')
print()