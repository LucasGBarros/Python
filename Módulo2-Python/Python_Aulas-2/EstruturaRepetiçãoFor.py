# AULA TEÓRICA


# Toda vez quando programamos uma estrutura de repetição, estamos na verdade, criando um algoritmo, um passo a passo
# do processo de programação.

#EX:

#Quando criamos um Laço, é pq criamos uma funçao de repetição, chamada "FOR" E "IN".
#Dentro dessa função, programamos o que desejamos repetir quantas vezes quisermos.

#Para definir um limite, numeramos o objeto, seja ele STR/INT/FLOAT... Nós começamos pelo numero "0" e [...].

#E com o limite definido, dentro do nossa função de laço, conseguimos estabelecer ações que quiser.

#Chamamos toda a função de "Laço de Repetição" ou de "ITERAÇÃO".

# Exemplo de Laço de Repetição:

'''
Laço C no intervalo(1, 10):

    passo   # passo == Identação para executar o que está dentro do laço de Repetição.

pega    # Pega sem Identação, para executar a ultima função do comando.


Como escrever em PYTHON:

for C in range(1, 10):

    passo

pega

OUTRO EXEMPLO:

for c in range(0 , 3):

    passo

    pula  # São dois comandos dentro da Repetição que se repetem e que podemos criar um laço.

passo

pega


OUTRO EXEMPLO

for c in range(0, 10):

    if moeda:

        pega

    passo

    pula

passo

pega
'''

# AULA PRÁTICA

for c in range(0, 6):
    print('Oi')
    print('FIM')

for c in range(6, 0, -1):
    print(c)

print('FIM')

for c in range(0, 7, 2):

    print(c)

print('Fim')


n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)

print('FIM')


n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)

print('FIM')


i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):

    print(c)

print('FIM')

s = 0

for c in range(0, 4):

    n = int(input('Digite um valor: '))
    s = s + n

print('O somatório de todos os valores foi {}'.format(s))


print('fim')