print("""Faça um programa que tenha uma função chamada escreva() que receba um texto qualquer como parâmetro e
mostre uma mensagem com tamanho adaptável.

ex:

escreva('Olá Mundo!')

Saída:

~~~~~~~~~~~~~~~~~~~~
    Olá, mundo!
~~~~~~~~~~~~~~~~~~~~""")
print()


def escreva(msg):
    tam = len(msg)

    print('~' * tam)
    print(msg)
    print('~' * tam)


escreva('Curso Em Video')
escreva('Aulas de Python')
escreva('Lucas')
