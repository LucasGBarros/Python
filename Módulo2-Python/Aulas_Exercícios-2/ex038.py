print("""Escreva um programa que leia \033[1:34m dois números \033[m inteiros e compare-os, mostrando na tela
uma mensagem.

- O \033[1:33mprimeiro valor\033[m é \033[1:34mmaior\033[m

- O \033[1:33m segundo valor\033[m é \033[1:34mmaior\033[m

- \033[1:33mNão existe\033[m valor maior, os dois são \033[1:34iguais\033[m
""")

print("""Digite qualquer número, que direi qual numero é maior ou se são iguais!!
""")

n1 = float(input('PRIMEIRO número: '))

n2 = float(input('SEGUNDO valor: '))

if n1 > n2:

    print('O \033[1:33mPrimero número\033[m {:.0f} que você colocou é \033[1:34mmaior\033[m que o segundo número que você colocou!'.format(n1))

elif n2 > n1:

    print('O \033[1:33mSegundo número\033[m {:.0f} que você colocou é \033[1:34mmaior\033[m que o primeiro número que voce colocou!'.format(n2))

else:

    n1 = n2

    print('\033[1:33mNão existe\033[m um valor maior. Os dois números são \033[1:34mIGUAIS\033[m!!')