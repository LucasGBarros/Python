print('''Faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lido''')

maior = 0

menor = 0

for p in range(1, 6):

    peso = float(input('Peso da {}º pessoa: '.format(p)))

    if p == 1:

        maior = peso

        menor = peso

    else:

        if peso > maior:

            maior = peso

        if peso < menor:

            menor = peso

print('O peso maior foi de {}Kg!'.format(maior))

print('O peso menor foi de {}Kg.'.format(menor))