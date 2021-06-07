print('''Crie um programa que tenha uma tula com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palvra, quais são as suas vogais.
''')

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python',
            'Curso', 'Gratis', 'Estudar','Praticar',
            'Trabalhar', 'Mercado', 'Programador', 'Futuro')

for p in palavras: # analisando cada elementos da tuplas.

    print(f'\nA palavra "{p.upper()}" temos a vogais: ', end='')

    for letra in p: # analise do elemento se está dentro da função, no caso, encontrar a vogal

        if letra.lower() in 'aeiou':

            print(letra, end=' ')