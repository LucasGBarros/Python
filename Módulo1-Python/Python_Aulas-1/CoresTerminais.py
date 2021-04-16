# AULA TEÓRICA

"""ANSI = Escape Sequence

\033[style text back m

\033[0;33;44m == código de cores"""

"""stile
0 Sem estilo
1 em negrito
4 Sublinhado
7 inverter as cores

text
29 branco
30 preto
31 vermelho
32 verde
33 amarelo
34 azul
35 roxo
36 verde agua
37 cinza

back

40 branco
41 vermelho
42 verde
43 amarelo
44 azul
45 roxo
46 verde agua
47 cinza
"""

#teste = \033[0;30;41m
#teste = \033[4;33;46m
#teste = \033[1;35;43m
#teste = \033[30;42m
#teste = \033[m
#teste = \033[7;30m


# AULA PRATICA

print('\033[7;33;44mOlá mundo\033[m')

a = 5
b = 7
print('Os valores são \033[34m{}\033[m e \033[4;35m{}\033[m!!!'.format(a, b))

# Outro exemplo


nome = 'Lucas'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[33m', nome, '\033[31m'))

# Outro exemplo que será explicado mais para frente

nome = 'Lucas'

cores = {'Limpa' : '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;29m'}

print('Olá, Muito prazer em te conhecer {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['Limpa']))