print('''Aula Teórica
      ''')

# O dicionário, consegue denominar nomes a tuplas ou listas, por exemplo:

dados = list()
dados.append('PEDRO')
dados.append('25')
print(dados[0]) # Ao invés de ser [0], seria [NOME]
print(dados[1]) # Ao invés de ser [1], seria [IDADE]

# O dicionário poderá denominar o nome de cada FATIAMENTOS

print('-'*30)

# A identificação de Dicionarios para declarar váriavel é denominada por {CHAVES}

dados = {'nome': 'Pedro', 'idade': 25}

dados['sexo'] = 'M'

print(dados['nome'])

print(dados['idade'])

print(dados['sexo']) #Criando um novo elemento de SEXO

del dados['idade'] #Eliminando elemento no DICIONÁRIO

print('-' * 30)

filme = {'título': 'Star Wars',
         'ano': 1997,
         'diretor': 'George Lucas'
         }

print(filme.values()) # Mostrando somente as informações do Dicionário.
print(filme.keys()) # Mostrando os Nomes denomidados do Dicionário.
print(filme.items()) # Mosstrando o Nomes denomidados e as informações do Dicionário.

print('-'*30)

# Utilizando FOR para mostrar um texto de Dicionário

for k, v in filme.items():

    print(f'O {k} é {v}')

print('-' * 30)

# Podemos utilizar uma lista e dentro da listas CONTER os Dicionários. Exemplo:

locadora = list()

filme1 = {'Filme': 'Star Wars',
          'Ano': 1977,
          'Diretor': 'George Lucas'}

filme2 = {'Filme': 'Avengers',
          'Ano': 2012,
          'Diretor': 'Joss Whedon'}
filme3 = {'Filme': 'Matrix',
          'Ano': 1999,
          'Diretor': 'Wachowski'}

locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)

print(locadora[0]['Ano'])
print(locadora[1]['Filme'])
print(locadora[2]['Diretor'])

print('=' * 100)

print('''AULA PRÁTICA
''')

pessoas = {'Nome': 'Lucas', 'Sexo': 'M', 'Idade': 21}

print(pessoas['Nome'])

print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print('-'*30)

for k in pessoas.keys():

    print(k)

print('-'*30)

for k in pessoas.values():

    print(k)

print('-' * 30)

for k, v in pessoas.items():

    print(f'{k} = {v}')

print('-'*30)

pessoas = {'Nome': 'Lucas', 'Sexo': 'M', 'Idade': 21}

del pessoas['Sexo'] # Apagando declaração de Váriavel

for k, v in pessoas.items():

    print(f'{k} = {v}')

print('-'*30)

# TROCANDO NOME DECLARADO

pessoas = {'Nome': 'Lucas', 'Sexo': 'M', 'Idade': 21}

pessoas['Nome'] = 'Gabriel'

for k, v in pessoas.items():

    print(f'{k} = {v}')

# ADICIONANDO NOVO ELEMENTO

pessoas = {'Nome': 'Lucas', 'Sexo': 'M', 'Idade': 21}

pessoas['Peso'] = 75 # Não precisando utilizar o .APPEND

for k, v in pessoas.items():

    print(f'{k} = {v}')

print('-'*30)

# Adicionando um Dicionário em uma Lista

brasil = [] # Lista

estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
print(brasil[1]['Sigla'])

print('-'*30)

estado = dict()
brasil = list()

for c in range(0, 3):

    estado['uf'] = str(input('Unidade Fedreativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))

    brasil.append(estado.copy()) # Dentro do dicionário, não podemos utilizar o FATIAMENTO p/ cópia, por isso,
                                 # o Dicionário tem uma função/ método interno chamado COPY()

print(brasil)

for e in brasil:

    for k, v in e.items():

        print(f'O campo {k} tem valor {v}.')

for e in brasil:

    for v in e.values():

        print(v, end= ' ')

    print()