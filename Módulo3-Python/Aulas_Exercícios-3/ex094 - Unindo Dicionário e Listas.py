print("""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
Dicionário e todos os dicionários em uma lista. no final, mostre: 

A) Quantas pessoas cadastradas.

B) A média de idade.

C) Uma lista com mulheres.

D) Uma lista com idade acima da média.""")
print()
print('~'*40)
print()

galera = list()

pessoa = dict()

soma = média = 0

while True:

    pessoa.clear() # A cada Laço, lerá um novo jogador.

    pessoa['nome'] = str(input('Nome: '))

    while True:

        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]

        if pessoa['sexo'] in 'MF':

            break

        print('ERRO! Por favor, digite apenas "M" ou "F".')

    pessoa['idade'] = int(input('Idade: '))

    soma += pessoa['idade']

    galera.append(pessoa.copy())

    while True:

        resp = str(input('Quer continuar? [S/N] ')).upper()[0]

        if resp in 'SN':

            break

        print('ERRO! Responda apenas "S" ou "N".')

    if resp == 'N':

        break

print()
print('~'*40)
print()

print(f'Ao todo temos {len(galera)} pessoas cadastrada')

média = soma / len(galera)

print(f'A média de idade é de {média:5.2f} anos.')

print('As mulheres cadastradas foram: ', end='')

for p in galera:

    if p['sexo'] in 'Ff':

        print(f'{p["nome"]}', end=' ')

print()

print('Pessoas que estão acima da média: ')

for p in galera:

    if p['idade'] >= média:

        print('    ')

        for k, v in p.items():

            print(f'{k} = {v} ', end='')

        print()

print()
print(f'{" Encerrado ":~^40}')