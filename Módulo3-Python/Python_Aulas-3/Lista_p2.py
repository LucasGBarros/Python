# Aula Teórica
print(f'{" Aula Teórica ":-^50}')

# ----------------------------------------------------------------------------------------------------------------------
# Adicionando elementos em uma lista.

# elemento 0 = Pedro
# elemento 1 = 25

dados = list()
dados.append('Pedro')
dados.append('25')

print(dados[0])     # Imprimindo o elemento 0, no caso, "Pedro".
print(dados[1])     # Imprimindo o elemento 1, no caso, "25".

# ----------------------------------------------------------------------------------------------------------------------
print('-'*50)

# Complementando a estrutura.

# Exemplo:

dados = list()
dados.append('Pedro')
dados.append('25')

pessoas = list()

pessoas.append(dados[:]) # Cópia de dados "[:]", fazendo a junção de "Pedro" e "25" em uma única estrutura.
                         # Sendo assim, colocando a lista de dados, dentro da estrutura de pessoas.
                         # Uma lista dentro de uma outra lista.

# Outro exemplo:

dados = list()

dados.append('Pedro')
dados.append('25')

dados.append('Maria')
dados.append('19')

dados.append('João')
dados.append('32')

pessoas = list()

pessoas.append(dados[:])

# print(pessoas[0][0]) # Buscando dentro da estrutura de dados, que está dentro da lista pessoas, o elemento 0 e onde está
                     # o 0 da estrutura, no caso "PEDRO".

# print(pessoas[1][1]) # buscando elemento 1 na estrutura 1 = "19"

# print(pessoas[2][0]) # = João

# print(pessoas[1]) # mostrando a estrutura inteira, no caso: ['Maria', 19].

print(f'{" Aula Prática ":-^50}')
print('-'*50)

test = list()

test.append('Lucas')
test.append(21)

galera = list()

galera.append(test[:]) # Fazendo ligação entre as estruturas, por isso deemos utilizar a cópia. [:]

test[0] = 'Maria'
test[1] = 22

galera.append(test[:]) # utilizando a cópia [:]

print(galera)

print('-'*50)

galera = [['João', 19], ['Ana', 33], ['Joaquin', 13], ['Maria', 45]]

print(galera[0])
print(galera[0][0])
print(galera[2][1])

for p in galera:

    print(p[0])
    print(p[1])
    print(f'{p[0]} tem {p[1]} anos de idade.')

print('-'*50)

galera = list()
dado = list()

for c in range(0,3):

    dado.append(str(input('Nome: ')))

    dado.append(int(input('Idade: ')))

    galera.append(dado[:])

    dado.clear()

print(galera)

totmai = totmen = 0

for p in galera:

    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')

        totmai += 1

    else:

        print(f'{p[0]} é menor de idade')

        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')