print("""Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artificio, indo de 10 a 0,
com uma pausa de 1 segundo entre eles.""")

import emoji

from time import sleep

print('Vai começar a contagem regressiva...')

for c in range(10, 0, -1):

    sleep(1)

    print('Contagem regressiva... ', c)

print(emoji.emojize(':fireworks:' * 10))
