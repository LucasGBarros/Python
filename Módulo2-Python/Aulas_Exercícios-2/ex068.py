print('''
Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.
''')

from random import randint

print(f'{" PAR OU IMPAR ":=^40}')

v = 0

while True:

    jogador = int(input('Digite um valor: '))

    computador = randint(0, 11)

    total = jogador + computador

    tipo = ' '

    while tipo not in 'PpIi':

        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]

    print('-='*20)

    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end=' ')

    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')

    if tipo == 'P':

        if total % 2 == 0:

            print('Você VENCEU!')

            v += 1

        else:

            print('Você PERDEU!')

            break

    if tipo == 'I':

        if total % 2 == 1:

            print('Você VENCEU!')

            v += 1

        else:

            print('Você PERDEU!')

            break

    print('Vamos jogar novamente...')

print(f'GAME OVER! Você venceu {v} vezes.')

print('-='*20)