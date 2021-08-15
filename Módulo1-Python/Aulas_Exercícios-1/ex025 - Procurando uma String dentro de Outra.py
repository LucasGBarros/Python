print('Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.')

nome = str(input('Qual o seu nome completo? ')).strip()

print('Seu nome tem Silva? {}'.format(nome[:5] == 'Silva'))

print('Seu nome tem Silva? {}'.format('Silva' in nome.upper()))
# Outra maneira de manipular String, porém, vai dar erro, caso alguém escreva "SilvA" pois não está denominado como upper ou lower como função.