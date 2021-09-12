print("""Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de vizualização de
detalhes do aproveiramento de cada jogador.""")
print()

time = list()

dados = dict()

partida = list()

print(f'{" Estátisticas de Jogadores ":=^40}')

while True:

    dados.clear() # A cada Laço, lerá um novo jogador.

    dados['nome'] = str(input('Nome do Jogador: ')).title()

    tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    partida.clear()

    for c in range(0, tot):

        partida.append(int(input(f'Quantos gols feito na {c}ª partida? ')))

    dados['gols'] = partida[:]

    dados['total'] = sum(partida)

    time.append(dados.copy())

    while True:

        resp = str(input('Deseja continuar? [S/N] ')).upper()[0]

        if resp in "SN":

            break

    if resp == 'N':

        break

print('='*40)

print('cód ', end='')

for i in dados.keys():

    print(f'{i:<15}', end='')

print()
print('='*40)

for k, v in enumerate(time):

    print(f'{k:>3} ', end='')

    for d in v.values():

        print(f'{str(d):<15}', end='')

    print()

print()
print('='*40)

while True:

    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))

    if busca == 999:

        break

    if busca>= len(time):

        print(f'ERRO! Não existe jogador com Código {busca}!')

    else:

        print(f' -- Levantamento do jogador {time[busca]["nome"]}')

        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')

        print('='*40)

print(f'{" VOLTE SEMPRE ":=^40}')
