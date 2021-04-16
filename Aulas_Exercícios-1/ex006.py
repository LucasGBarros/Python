print('Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada')

# Utilizando 006 sem a Variável

# Função para calcular a raiz é "pow" ou seja -> "pow(n, (1/2))"

n = int(input('Digite um valor: '))

print('O dobro do valor é: {}'.format(n*2))

print('O triplo do valor é: {}'.format(n*3))

print('A raiz quadrada do valor é: {:.3}'.format(n**(1/2))) # Ou pow(n, (1/2))

# Utilizando 006 COM a variável

n = int(input('Digite um valor: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro do valor é: {} \n O triplo do valor é: {} \n A raiz quadrada do valor é: {:.2f}'.format(d, t, r))
