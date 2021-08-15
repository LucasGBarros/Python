print('''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O Programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.
''')

from random import randint
from time import sleep

lista = list()

jogos = list()

print('-='*20)

print(f"{' MEGA SENA ':^40}")

print('-='*20)

quant = int(input('Quantos Jogos você quer jogar? '))

tot = 1

while tot <= quant:

    cont = 0

    while True:

        num = randint(1, 60)

        if num not in lista:

            lista.append(num)

            cont += 1

        if cont >= 6:

            break

    lista.sort()

    jogos.append(lista[:])

    lista.clear()

    tot += 1

print('=' * 10, f"SORTEANDO {quant} JOGOS", '=' * 11)
for i, l in enumerate(jogos):

    print(f'Jogos {i+1}: {l}')

    sleep(1.5)

print(f'{" BOA SORTE ":=^40}')