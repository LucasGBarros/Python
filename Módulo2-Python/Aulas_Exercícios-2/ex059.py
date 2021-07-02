print('''Crie um programa que leia dois valores e mostre um menu na tela:

[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA

Seu programa deverá realizar a operação solicitada em cada caso.
''')

from time import sleep

print('{:=^40}'.format('MENU DE INTERAÇÃO'))

n1 = float(input('Primeiro Valor: '))
n2 = float(input('Segundo valor: '))

menu = 0

while menu != 5:

    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')

    menu = int(input('Qual é a sua opção? '))

    if menu == 1:

        soma = n1 + n2

        print('A soma entre {:.0f} e {:.0f} é de {:.0f}'.format(n1, n2, soma))

    elif menu == 2:

        mult = n1 * n2

        print('A multiplicação entre {:.0f} x {:.0f} é {:.0f}'.format(n1, n2, mult))

    elif menu == 3:

        if n1 > n2 or n2 > n1:

            maior = n1

        else:

            maior = n2

        print('O maior número é de {:.0f} e {:.0f} é {:.0f}'.format(n1, n2, maior))

    elif menu == 4:

        print('Digite os números novamente.')

        n1 = int(input('Primeiro valor: '))

        n2 = int(input('Segundo valor: '))

    elif menu == 5:

        sleep(1)

        print('Finalizando...')

    else:

        print('Opção inválida, tente novamente.')

print('='*40)

sleep(2)

print('Fim do Programa! Volte sempre!')
