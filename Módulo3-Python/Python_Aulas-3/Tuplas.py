# Fundamentos Tuplas

# ======================================================================================================================

print(f'{" Aula teórica ":=^40}')

# As TUPLAS são variáveis compostas e imútaveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis
# por chave individuais.

# Váriavel simples, só cabe um valor dentro do armazenamento.

# Váriavel compostas armazenam vários valores.

# Tipo de váriaveis compostas: Tuplas, Listas e Dicionário.


# Dentro da Tupla, eles são identificado por indices numéricos.

# Para TUPLAS, utilizamos "()" Parentêses, para listas utilizamos "[]" Colchetes e para dicionário utilizamos "{}" chaves

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

# As tuplas é utilizado no fatiamento dentro de uma "Lista"

print(lanche[2])

print(lanche[0:2])

print(lanche[1:])

print(lanche[-1])

print(len(lanche))

# Utilizando na estrutura de Repetição

for c in lanche:

    print(c)

# As tuplas SÃO IMUTÁVEIS, não podemos mudar uma tupla.

print(f'{" Fim aula teórica ":=^40}')

# ======================================================================================================================

# AULA PRÁTICA

print(f'{" Aula Prática ":=^40}')

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') # Váriavel Compostas "()" -> Tuplas

print(lanche[1])

print(lanche[3])

print(lanche[-2])

print(lanche[1:3])

print(lanche[2:])

print(lanche[:2])

print(lanche[-2])

print(lanche[-3:])

print(lanche)

# Tuplas IMUTÁVEIS

# lanche[1] = 'Refrigerante'

# print(lanche[1])

# Utilizando For

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

# Lendo quantos Elementos tem na tupla.

print(len(lanche))

for comida in lanche:

    print(f'Eu vou comer {comida}')

print('Comi muito.')



# Outra maneira de utilizar For

for cont in range(0, len(lanche)):

    print(f'Eu vou comer {lanche[cont]}') # Colocando lanche lendo o RANGE CONT

print('Comi muito')




# Outra maneira de utilizar For contando a posição

for cont in range(0, len(lanche)):

    print(f'Eu vou comer {lanche[cont]} na posição {cont}')



# outra maneira de contabilizar posição

for pos, comida in enumerate(lanche):

    print(f'Eu vou comer {comida} na posição {pos}')



# Mostrando a tupla em ORDEM


lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(sorted(lanche)) # e com isso ele tranforma em LISTA para organizar a TUPLA

# Criando outra Tupla

a = (2, 5, 4)
b = (5, 8, 1, 2)

c = a + b # Junção de TUPLA

print(c)

print(len(c))

print(c.count(5))

print(c.index(8)) # Index indica em que posição está o valor

pessoa = ('Lucas', 21, 'M', 99.88)

# del(pessoa) # "APAGANDO" uma váriavel

print(pessoa)

print(sorted(lanche))