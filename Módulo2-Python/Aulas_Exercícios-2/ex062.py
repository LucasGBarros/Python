print('''Melhore o DESAFIO ex061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
''')

print(f'{"PROGRESSÃO ARITMÉTICA":=^40}')

p = int(input('Digite o primeiro termo: '))

r = int(input('Digite a razão da PA: '))

termo = p

cont = 1

total = 0

mais = 10

while mais != 0:

    total = total + mais

    while cont <= total:

        print('{} -> '.format(termo), end='')

        termo += r

        cont += 1

    print('PAUSA')

    mais = int(input('Quanto termos voce quer mostrar mais? '))

print('PROGRESSÃO FINALIZADA. {} termos foram mostrados.'.format(total))
