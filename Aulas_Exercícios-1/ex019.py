import random
from random import choice

print("""Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome escolhido.""")

print('-'*20)

a1 = input('Primeiro Aluno: ')

a2 = input('Segundo Aluno: ')

a3 = input('Terceiro Aluno: ')

a4 = input('Quarto Aluno: ')

lista = [a1, a2, a3, a4]    #  Correção da questão: O elemento [] é utilizado como lista
r = random.choice(lista)    #  Correção da questão

print('O aluno Sorteado é: {}'.format(r))

print('-'*20)