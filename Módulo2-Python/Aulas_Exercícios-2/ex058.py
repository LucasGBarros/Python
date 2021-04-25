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

print('Você tentou {}x para acertar.'.format(aleatório))

print('O computador escolheu o número: {}'.format(r))

