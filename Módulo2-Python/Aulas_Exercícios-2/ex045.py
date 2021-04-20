print('Crie um programa que faça o computador jogar Jokenpô com você.')

from random import randint

itens = ('PEDRA', 'PAPEL', 'TESOURA')

computador = randint(0, 2)

print('''Suas Jogadas:

[0] PEDRA
[1] PAPEL
[2] TESOURA
''')

jogador = int(input('Qual é a sua jogada? '))

print('=-'*25)

print('O Computador escolheu {}.'.format(itens[computador]))

print('O Jogador jogou {}.'.format(itens[jogador]))


print('=-'*25)

if computador == 0: # Computador jogou Pedra.

    if jogador == 0:

        print('EMPATE')

    elif jogador == 1:

        print('Jogador Venceu')

    elif jogador == 2:

        print('Computador Venceu')

    else:

        print('Jogada Inválida.')

elif computador == 1:  # Computador jogou Papel.

    if jogador == 0:

        print('Computador Venceu.')

    elif jogador == 1:

        print('Empate.')

    elif jogador == 2:

        print('Jogador venceu.')

    else:

        print('Jogada Inválida')

elif computador == 2:   # Computador jogou Tesoura.

    if jogador == 0:

        print('Jogador Venceu.')

    elif jogador == 1:

        print('Computador venceu.')

    elif jogador == 2:

        print('Empate.')

    else:

        print('Jogada Inválida.')

print('=-'*25)