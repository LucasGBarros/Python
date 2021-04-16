from random import choice

print("""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo o computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.""")

lista = [0, 1, 2, 3, 4, 5]
r = choice(lista)

ale = int(input('Acerte um número de 0 a 5: '))

print('O número é {}!'.format(r))

if r == ale:
    print('Parabéns voce acertou!')
else:
    print('Você perdeu!')