# =============== AULA TEÓRICA ===================

# As funções em todas as linguagem de programaçao, elas estão vinculadas a uma palavra chamada ROTINA.
# As dunções é algo que se faz constantemente, uma rotina do que eu quero que mostre na tela.
# Assim podemos criar uma função na tela e como chamado no python, função ou DEF, que é definição de função.

# Exemplo de Função:

print('---------------------------------')
print('        SISTEMA DE ALUNOS        ')
print('---------------------------------')
print('---------------------------------')
print('     CADASTRO DE FUUNIONÁRIO     ')
print('---------------------------------')
print('---------------------------------')
print('         ERRO DO SISTEMA         ')
print('---------------------------------')

print()
print(f'{" Exemplo de como utilizar o DEF ":=^40}')
print()


def mostraLinha():  # TODAS AS FUNÇÕES DE PYTHON ELAS SÃO IDENTIFICADAS POR PARENTESES NO FINAL DO NOME.

    print('-' * 35)


mostraLinha()
print('        SISTEMA DE ALUNOS        ')
mostraLinha()

mostraLinha()
print('     CADASTRO DE FUNCIONÁRIO     ')
mostraLinha()

mostraLinha()
print('         ERRO DO SISTEMA         ')
mostraLinha()

print()
print('=' * 40)
print()


# Utilizando Paramentros

def menssagem(msg):  # toda vez que eu utilizar o comando "menssagem()", eu vou poder alterar o valor dentro dos
    # parenteses

    print('-' * 30)

    print(msg)

    print('-' * 30)


menssagem('   SISTEMA DE ALUNO   ')  # Menssagem que eu quero colocar dentro dos parametros "# (msg)"

menssagem(' PYTHON É MUITO BOM   ')

menssagem(' OI ')

# -------------------------------------------------------------------------------------------------------------

print()
print(f'{" AULA PRÁTICA ":=^50}')
print()

a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

print()
print('-' * 30)
print()


# -------------------------------------------------------------------------------------------------------------


def soma(a, b):
    s = a + b

    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(4, 1)

print()
print('-' * 40)
print()


# -------------------------------------------------------------------------------------------------------------


def soma(a, b):
    print(f'A = {a} e B = {b}')

    s = a + b

    print(f'A soma entre {a} e {b} é de {s}')
    print()


soma(b=5, a=9) or soma(a=5, b=9)
soma(7, 2)

print()
print('-' * 40)
print()


# -------------------------------------------------------------------------------------------------------------

# Função CONTADOR

# A linguagem python, tem conceitos de empacotar parametros, onde nao tem em outras linguagem de programação.

# Exemplo de Empacotamento


def contador(*num):
    print(num)


contador(8, 9, 5, 2)
contador(2, 6)
contador(5, 7, 6, 7, 4, 5)

print()
print('-' * 40)
print()


# -------------------------------------------------------------------------------------------------------------


def contador(*num):
    for valor in num:
        print(f'{valor}  ', end='')
    print('Fim')


contador(8, 9, 5, 2)
contador(2, 6)
contador(5, 7, 6, 7, 4, 5)

print()
print('-' * 40)
print()


# -------------------------------------------------------------------------------------------------------------


def contador(*num):
    tam = len(num)

    print(f' Recebi os  valores {num} e são ao todos {tam} números')


contador(8, 9, 5, 2)
contador(2, 6)
contador(5, 7, 6, 7, 4, 5)

print()
print('-' * 40)
print()

# -------------------------------------------------------------------------------------------------------------

# Dobrando valor de LISTA utilizando DEF


def dobra(lst):
    pos = 0

    while pos < len(lst):

        lst[pos] *= 2

        pos += 1


valores = [6, 3, 9, 1, 0, 2]

dobra(valores)
print(valores)

print()
print('-' * 40)
print()

# -------------------------------------------------------------------------------------------------------------


def soma(* valores):

    s = 0

    for num in valores:

        s += num

    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)

print()
print('-' * 40)
print()