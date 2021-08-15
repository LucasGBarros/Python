print('''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem
de colocação. depois mostre:
      
- Apenas os 5 primeiros colocados.

- Os últimos 4 colocados da tabela.

- Uma lista dos times em ordem alfabética.

- Em que posição na tabela está o time da Chapecoense.
''')

times = ('Atlético-GO', 'Bahia', 'Bragantino', 'Fortaleza', 'Fluminense',
         'Athletico-PR', 'Flamengo', 'Ceára SC', 'Santos', 'Sport Recife',
         'Juventude', 'Cuiaba', 'Internacional', 'América-MG', 'Corinthians',
         'São Paulo', 'Grêmio', 'Atlético-MG', 'Palmeiras', 'Chapecoense')

print('~'*25)

print(f'Lista do times do Brasileirão: {times}')

print('~'*25)

print(f'Os 5 primeiros times são: {times[0:5]}')

print('~'*25)

print(f'Os 4 últimos times são: {times[-4:]}')

print('~'*25)

print(f'Times em ordem alfabética: {sorted(times)}')

print('~'*25)

print(f'A chapecoense está na posição: {times.index("Chapecoense")+1}ª')

print('~'*25)
