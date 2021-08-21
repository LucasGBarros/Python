print('''Melhore o jogo do DESAFIO ex028 onde o computador vai pensar em um número entre 0 e 10. Só que agora
o jogador vai TENTAR adivinhar até acertar, mostrando no final quantos palpites foram necesário para vencer.
''')

from random import choice

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = choice(lista)

aleatório = int(input('Adivinhe um número de 0 a 10 que o computador escolheu: '))

while aleatório != r:

    aleatório = int(input('Você não acertou. Tente novamente: '))

print('Parabéns, você acertou.')

print('O computador escolheu o número: {}'.format(r))

# Correção do execício.

from random import randint

comp = randint(0, 10)

print('Olá, sou seu computador! Acabei de pensar em um número de 0 a 10.')

print('Será que você consegue adivinhar qual foi? ')

acertou = False

tentativas = 0

while not acertou:

    jogador = int(input('Qual é seu palpite? '))

    tentativas += 1

    if jogador == comp:

        acertou = True

    else:

        if jogador < comp:

            print('Mais... Tente novamente.')

        elif jogador > comp:

            print('Menos... Tente novamente')

print('Parabéns!!! Você acertou com {} tentativas.'.format(tentativas))
