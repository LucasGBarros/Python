print('''
Crie um programa que leia vários números inteiros pelo teclado. 

O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 

No final, mostre quantos números foram digitados e qual foi a soma entre eles. (DESCONSIDERANDO O FLAG).
''')

n = s = 0
cont = 0

while True:

    n = int(input('Digite um valor [999 Stop]: '))

    if n == 999:

        break

    cont += 1

    s += n

print(f'Foram {cont} para somar o valor de {s}.')