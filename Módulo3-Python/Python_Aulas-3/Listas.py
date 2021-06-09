"""Aula Teórica"""

# listas []

lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim'] # As listas SÃO mutáveis e podem ser mutáveis, ou seja, podemos trocar valores.

lanche[3] = 'Picolé' # Trocando valores.


# Como as listas são mutáveis, podemos adicionar mais itens/ valores para alteração de dados.

# ----------------------------------------------------------------------------------------------------------------------

'''Declaração de Lista'''

# ----------------------------------------------------------------------------------------------------------------------

"""Método Append()"""
# Adicionando item novos na lista:


lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']

lanche.append('Cookie') # cookie adicionado como novo elemento da lista.

'''Lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Cookie']''' # Cookie adicionado.

# ----------------------------------------------------------------------------------------------------------------------

"""Método insert()"""
# Adicionando novo elemento em posiçao desejada.


lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Cookie']

lanche.insert(0,'Hotdog') # Inserindo a posição do HOTDOG na posição antes do HAMBURGUER.

''' lanche = ['Hotdog', 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Cookie']'''



# ----------------------------------------------------------------------------------------------------------------------

'''Método del.xxx[3]'''
# Apagando elemento da Lista.

lanche = ['Hotdog', 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Cookie']

del lanche[3]
#  OU
lanche.pop(3) # Geralmente o método pop é utilizado para eliminar o último elemento, mas podemos utilizar da mesma forma.
# Podendo utilizar duas maneiras de deletar um elemento da lista.

# ----------------------------------------------------------------------------------------------------------------------

# Método Remove

"""lanche.remove('Pizza')""" # eliminando o valor que deseja eliminar. Os demais elementos irão se reposicionar.

# Caso tentamos remover algum item na lista, poderiámos resolver da seguinte maneira:

"""if 'Cookie' in lanche:"""

"""lanche.remove('Pizza')"""

# ----------------------------------------------------------------------------------------------------------------------

# Utilizando lista com range()

valores = list(range(4, 11))

# representando como:

# Valores
"""4 5 6 7 8 9 10       # Dentro do elemento.
   0 1 2 3 4 5  6"""    # Ordenação da Lista.


# Utilizando elementos fora de ordem:

valores = [8, 2, 5, 4, 9, 3, 0]

# Valores
"""8 2 5 4 9 3 0        # Dentro do elemento.
   0 1 2 3 4 5 6 """    # Ordenação da Lista.


# Ordernando valores/ elementos da lista.

valores = [8, 2, 5, 4, 9, 3, 0]

valores.sort() # Feito a ordenação do valores [8, 2, 5, 4, 9, 3, 0].

# invertendo a ordem dos valores/ elementos.

valores = [8, 2, 5, 4, 9, 3, 0]

valores.sort(reverse = True) # Ordem de valores invertida.

len(valores) # Lendo valores/ elementos


# ----------------------------------------------------------------------------------------------------------------------

"""Aula Prática"""

num = [2, 5, 9, 1]

num[2] = 3

num.append(7) # Adicionando "7" na lista.

num.sort() # Colocando em ordem

num.sort(reverse = True) # Colocando ordem invertida

num.insert(2, 0) # Inserindo o valor no meio dos valores.

num.pop() # Eliminando o último valor.

num.pop(2) # Eliminando valor desejado.

num.remove(2)

if 4 in num:

    num.remove(4)
else:

    print('Não achei o numero 4')

print(num)

print(f'Essa lista tem {len(num)} elementos')

# ----------------------------------------------------------------------------------------------------------------------

valores = []

valores.append(5)

valores.append(9)

valores.append(4)

"""for v in valores:

    print(f'{v}...', end='')""" # adicionando append no print

for c, v in enumerate(valores): # c = indice / v = valor

    print(f'na posiçao {c} encontrei o valor {v}!') # indice (c) posição do valor (v) e recebe o valor (v)

print('Cheguei ao final da lista.')

print('-'*50)

for cont in range(0,5):

    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):

    print(f'Na posição {c} encontrei o valor {v}!')

print('Cheguei ao final da lista')

# ----------------------------------------------------------------------------------------------------------------------

# Ligação de lista PYTHON

a = [2, 3, 4, 7]
b = a

b = a[:] # Fazendo cópia da lista!!

b[2] = 8 # Alterando o unico valor que se iguala na mesma junção, irá trocar de duas lista.

print(f'Lista A: {a}')

print(f'Lista B: {b}')