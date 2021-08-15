print('''Faça um programa ue leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
''')
num = []

maior = menor = 0

for c in range(0, 5):

       num.append(int(input(f'Digite um número na posição {c}: '))) # Adicionando valores dentro da váriavel composta Lista.

       if c == 0:

              maior = menor = num[c]      # Definindo num[c] como o maior ou menor.

       else:

              if num[c] > maior:

                     maior = num[c]       # num[c] passa a ser o maior valor

              if num[c] < menor:

                     menor = num[c]       # num[c] passa a ser o menor valor

print(f'Os números digitados na lista foram: {num}')

print(f'O maior número digitado foi: {maior} nas posições ', end='')

for i, v in enumerate(num):        # i = indice / v = valor

       if v == maior:              # valor (v) receber maior número.

              print(f'{i}... ', end='') # indice (i) posição do valor maior

print()       # Quebrando " end'' "

print(f'O menor número digitado foi: {menor} nas posições ', end='')

for i, v in enumerate(num): # i = indice / v = valor

       if v == menor:       # valor (v) recebe menor valor

              print(f'{i}... ', end='') # indice (i) posição do valor menor

print()       # Quebrando " end='' "
