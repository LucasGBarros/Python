print("""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.""")
print()

dados = dict()
partidas = list()

print(f'{" Estátistica de Jogador ":=^40}')

dados['Nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))

for c in range(0, tot):

    partidas.append(int(input(f'Quantos gols feito na {c+1}º partida? ')))

dados['Gols'] = partidas[:] # A função [:] serve para incluir uma lista dentro do Dicionário

dados['Total'] = sum(partidas)

print('='*40)

for k, v in dados.items():

    print(f'O campo {k} tem o valor de {v}')

print('='*40)

print(f'O jogador {dados["Nome"]} jogou {len(dados["Gols"])} partidas.')

for i, v in enumerate(dados["Gols"]):

    print(f'Na partida {i+1} fez {v} gols.')

print(f'Foi um total de {dados["Total"]} gols.')

print('='*40)