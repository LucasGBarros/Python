print('''Crie um programa que leia varios números inteiros pelo teclado. 
No final mostre a média entre todos os valors e qual foi o maior e o menor valores lidos. 
O programa deve perguntar se ele quer ou não continuar a digitar os valores.
''')

resposta = 'S'

soma = quant = med = maior = menor = 0

while resposta in 'Ss':

    num = int(input('Digite um número: '))

    soma += num

    quant += 1

    if quant == 1:

        maior = menor = num

    else:
        if num > maior:

            maior = num

        if num < menor:

            menor = num

    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

med = soma / quant

print('Você digitou {} números e a média foi {}.'.format(quant, med))

print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))