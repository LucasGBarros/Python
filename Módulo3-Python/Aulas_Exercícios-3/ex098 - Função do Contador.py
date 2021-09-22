print("""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: Início, Fim e Passo e
realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

A) De 1 até 10, de 1 em 1.
B) De 10 até 0, de 2 em 2.
C) Uma contagem Personalizada.""")
print()

from time import sleep


def mostraLinha():
    print('-' * 35)


def contador(i, f, p):
    print('-' * 35)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if p < 0:
        p *= -1

    if p == 0:
        p = 1

    if i < f:
        cont = i

        while cont <= f:
            print(f'{cont} ', end='')  # Caso não estivesse mostrando no RUN, colocar desta forma: end='', flush=True
            sleep(0.5)

            cont += p

        print('FIM')

    else:
        cont = i

        while cont >= f:
            print(f'{cont} ', end='')  # Caso não estivesse mostrando no RUN, colocar desta forma: end='', flush=True
            sleep(0.5)

            cont -= p

        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)

mostraLinha()
print('Agora é a sua vez!')

ini = int(input('Início:  '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))

contador(ini, fim, pas)
