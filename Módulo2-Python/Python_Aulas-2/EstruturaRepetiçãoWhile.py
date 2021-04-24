# AULA TEÓRICA WHILE

'''

- A estrutura de repetição FOR, ela precisa de um limite de um ponto até outro ponto.

- Com a repetição While, nós não sabemos até quanto é o limite que precisamos saber por isso é utilizado a
estrutura While

- A estrutura de repetição WHILE, serve para repetir o laço ENQUANTO não chegar no objetivo.

- A estrutura While é representada como estrutura de repetição de teste LÓGICO, já a estrutura de repetição FOR,
é representada como Estrutura de repetição com VARIAVEL DE CONTROLE.


# EX WHILE teórico:

    ENQUANTO não (MAÇA) # Não representa como CONDIÇÃO

            passo

        pega

# Ex de como utilizar (teórico):


while not maça:        # not representa Condição.
    
    passo              # Dentro da estrutura While, será utilizada as funçoes desejada

pega                   # Fora da estrutura While, ultimo comando da função



- A diferença da estrutura é de que, quando sabemos o limite da repetição, é mais pratico utilizar o for, caso contrario, utilizamos While.

REPRESENTAÇÃO PORTUGUES (PORTUGOL):


enquanto não maçã
    
    se bloco
    
        passo
    
    se não bloco
        
        pula

    se moeda
        
        pegue

pega



REPRESENTAÇÃO PYTHON

while not maça:

    if bloco:

        passe

    if nãobloco:

        pule

    if moeda:

        pega

pega
'''

# AULA PRÁTICA WHILE

'''for c in range(1, 10):
    print(c)
print('fim')'''

c = 1

while c < 10:

    print(c)
    c = c + 1

print('FIM')

'''Com a repetição for, podemos colocar o limite de resultados que queremos, com a repetição for, podemos colocar o 
limite que queremos, por mais que não sabemos o final do resultado.

Ex:'''

# Repetição for.

for c in range(1, 5):

    n = int(input('Digite um valor: '))

print('FIM')

# Repetição While:

n = 1

while n != 0: # Condição de parada

    n = int(input('Digite um valor: '))

print('Fim')

# Outro exemplo de como utilizar o While.

r = 'S'

while r == 'S':

    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar: [S/N] ')).upper()

print('FIM')

''' Com a função while eu não preciso determinar um limite, até o limite que voce quer.'''

# Ex:

n = 1

par = impar = 0

while n != 0:

    n = int(input('Digite um valor: '))

    if n != 0:

        if n % 2 ==0:

            par += 1

        else:

            impar += 1

print('você digitou {} números pares e {} impares'.format(par, impar))