print('''Crie um programa que mostra na tela todos os numeros pares que estão no intervalo entre 1 e 50.''')

print('Todos os números pares que estão dentro de 0 a 50.')

for c in range(0, 50):

    res = c % 2

    if res == 0:

        print(c)

print('FIM')