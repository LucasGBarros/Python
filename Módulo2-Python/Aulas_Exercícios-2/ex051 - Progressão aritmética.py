print('''Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA. No final, mostre os 10 primeiros termos
dessa progressão
''')

print('{:=^40}'.format('PROGRESSÃO ARITMÉTICA'))

p = float(input('Digite o primeiro termo: '))

r = float(input('Digite a razão: '))

a = p

print(p)

for c in range(0, 9):

    a = a + r

    print('{}'.format(a))

print('{:=^40}'.format('FIM'))