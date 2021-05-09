print('''Refaça o desafio ex051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da 
progressão usando a estrutura WHILE.
''')

print(f'{"PROGRESSÃO ARITMÉTICA":=^40}')

p = int(input('Digite o primeiro termo: '))

r = int(input('Digite a razão da PA: '))

termo = p

cont = 1

while cont <= 10:

    print('{} -> '.format(termo), end='')

    termo += r

    cont += 1

print('FIM')
