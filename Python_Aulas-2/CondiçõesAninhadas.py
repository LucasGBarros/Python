# Condições Aninhadas: servem para criar uma estrutura dentro da estrutura. Exemplo:

#  Lado esquerdo

"""
carro.siga()

IF  carro.esquerda():        # LEMBRANDO QUE TODAS AS  "()" REPRESENTA UM MÉTODO

    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()

ELIF  carro.direita():          # FUNÇÃO "SENÃO SE"

    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()

ELSE:

    carro.siga()

carro.pare()
"""

nome = str(input('Qual é o seu nome? '))

if nome == 'Lucas':

    print('Que nome bonito!')

elif nome == 'Pedro' or nome == 'Maria' or nome == 'Renato':

    print('Seu nome é bem popular no Brasil')

elif nome in 'Ana Cláudia Jéssica Juliana':

    print('Belo nome feminino')

else:

    print('Seu nome é bem normal.')

print('Tenha um bom dia {}!'.format(nome))