print('Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor')

# Utilizando o resultado como variável!!

n1 = int(input('Digite um número inteiro: '))

a = n1 - 1
s = n1 + 1

print('O numéro inteiro é: {}, seu antecessor é: {} e seu sucessor é: {}'.format(n1, a, s))

# Utilizando resultado como NÃO variável!!

n1 = int(input('Digite um número inteiro: '))

print('O número inteiro é: {}'.format(n1))

print('O seu antecessor é: {}'.format(n1-1))

print('O seu sucessor é: {}'.format(n1+1))