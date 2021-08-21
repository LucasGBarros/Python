print('''Desenvolva um programa que leia SEIS NUMEROS INTEIROS e mostre a soma apenas daqueles que forem pares. Se o valor
for ímpar, desconsidere-o''')

s = 0

con = 0

for c in range(1, 7):

    n = int(input('Digite o {}º número: '.format(c)))

    if n % 2 == 0:

        s += n
        con += 1

print('{} números são pares e a soma deles é: {}'.format(con, s))