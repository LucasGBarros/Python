print('Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou Ímpar.')

n = int(input('Digite um valor: '))

res = n % 2 # Todos os numero par, o resultado dará 0 e todos números impar, dará 1.

if res == 0:

    print('O número {} que você escolheu é PAR'.format(n))

else:

    print('O número {} que voce escolheu é ÍMPAR'.format(n))