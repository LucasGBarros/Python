print('''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre
eles. [DESCONSIDERANDO O FLAG]
''')

num = 0

cont = 0

soma = 0

num = int(input('Digite um número [999 para parar]: '))

while num != 999:

    num = int(input('Digite um número [999 para parar]: '))

    soma += num

    cont += 1

print('Você digitou {} numeros! E a soma entre eles foi {}'.format(cont, soma))