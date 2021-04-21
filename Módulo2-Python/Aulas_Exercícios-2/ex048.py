print('''Faça um programa que calcule a soma entre todos os números impares que são multiplos de 3 e que se encontram
no intervalo de 1 até 500.
''')

print('''Números ímpares MULTIPLOS de 3.
''')

s = 0

for c in range(1, 500, 2):

    if c % 3 == 1:

        s += c

print('Soma:', s)

print('''FIM''')