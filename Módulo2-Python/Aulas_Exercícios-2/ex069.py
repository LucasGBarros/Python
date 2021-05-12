print('''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar.

No final, mostre:

- Quantas pessoas tem mais de 18 anos.
- Quantos Homens foram cadastrados.
- Quantas mulheres tem menos de 20 anos
''')

total18 = totalHomem = mulher20 = 0

while True:

    print(f'{" Cadastre uma Pessoa ":=^40}')

    idade = int(input('IDADE: '))

    sexo = ' '

    while sexo not in 'MmFf':

        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade > 18:

        total18 += 1

    if sexo == 'M':

        totalHomem += 1

    if idade < 20:

        mulher20 += 1

    resp = ' '

    print('='*40)

    while resp not in 'SN':

        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':

        break

print(f'Total de pessoas com mais de 18 anos: {total18}.')

print(f'Total de {totalHomem} homens cadastrados.')

print(f'Total de {mulher20} menores de 20 anos.')

print(f'{" Fim do programa ":=^40}')