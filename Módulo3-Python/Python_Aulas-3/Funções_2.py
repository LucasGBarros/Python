# ========== INTERACTIVE HELP ==========

help() # Utilizando ajuda interativa.
print(input.__doc__) # Utiizando infotmações do Input (Podendo ser qualquer atributo).


# ============ DOCSTRINGS ============

# Básicamente uma string de documentação, mostra o manual de qualquer comando

def contador(i,f,p):

    """
    -> Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: fim da contagem
    :param p: passo a passo da contagem
    :return: Sem retorno
    """

    c = i
    while c <= f:
        print(f'{c}', end='..')
        c+=p
    print('FIM!')

contador(2,10,2)
help(contador)

# ======= Parâmetros Opcionais =======

def somar(a,b, c=0): # Utilizando parâmetro opcionais como "=0"
    s = a + b +c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)

def somar(a=0, b=0, c=0): # Utilizando parâmetro opcionais como "=0"
    s = a + b +c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)
somar()

# ========== Escopo de Váriaveis ==========

def teste():

    x=8 # Seria uma variavel LOCAL
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n=2 # seria uma variavel GLOBAL
print(f'no programa principal, n vale {n}')
print(f'No programa principal, x vale {x}') # por isso a váriavel local, não funciona na variavel global.


# ================ Escopo Global =========================

# ================ Escopo Local =================


def teste(b):
    a=8         # criando uma variavel dentro do escopo local
    b+=4        # criando uma variavel dentro do escopo local
    c=2         # criando uma variavel dentro do escopo local

    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
# ===============================================

a=5
teste(a)
print(f'A fora vale {a}')
print(f'B fora vale {b}') # Não vai rodar este comando pois, ele está dentro do escopo local e não global
print(f'C fora vale {c}') # Não vai rodar este comando pois, ele está dentro do escopo local e não global
# ========================================================

# ------------------------------ OUTRO EXEMPLO ------------------------------

# ================ Escopo Global =========================

# ================ Escopo Local =================


def teste(b):

    global a # Utilizando o A global, dentro do escopo local, porém, o VALOR ALTERADO é GLOBAL e não local

    a=8         # criando uma variavel dentro do escopo local
    b+=4        # criando uma variavel dentro do escopo local
    c=2         # criando uma variavel dentro do escopo local

    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')
# ===============================================

a=5
teste(a)
print(f'A fora vale {a}')
print(f'B fora vale {b}') # Não vai rodar este comando pois, ele está dentro do escopo local e não global
print(f'C fora vale {c}') # Não vai rodar este comando pois, ele está dentro do escopo local e não global
# ========================================================


# =============== RETURN ===============

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = soma(5, 3, 2)
r2 = soma(8, 2)
r3 = soma(9, 1)

print(soma(5, 3, 2))
print(soma(8, 2))
print(soma(9, 1))

# Ou pode ser utiizado desta forma

print(f'A soma dos valores foram {r1}, {r2} e {r3}')
