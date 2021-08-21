print('''Refaça o Desafio ex009, mostrando a tabuada que o usuário escolher, só que agora utilizando laço FOR''')

n = int(input('Digite a tabuada que deseja: '))

print('{:=^40}'.format('TABUADA'))

for c in range(0, 10+1):

    print(n, 'x', c,'= {}'.format(n * c))

print('='*40)