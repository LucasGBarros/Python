# Condições são operadores que tem dois lados de possibilidades, "se ou senao", utilizado para a resposta que o programa vai mostrar.

# Comando sequenciais são ordens de cima para baixo de execução, chamado de estrutura sequencial


# Ex:

# Lembrando que "()" sempre representará como métodos

#O programa abaixo tem dois fluxos, representado como fluxo verde (Fluxo verdadeiro) e fluxo vermelho (Fluxo falso)
# Representando como dois caminhos diferentes

"""Carro.siga()

se carro.esquerda(): # A palavra "se" é representado com if
    carro.siga()
    carro.direita()
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga

senao: # "senao" é representada como else:
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()"""

# EX:

#tempo = int(input('Quantos anos tem seu carro? '))

#if tempo <=3:
#    print('Seu carro está novo')

#else:
#    print('Carro velho')
#print('--FIM--')

# ou utilizando o mesmo método simplificado

#tempo = int(input('Quantos anos tem seu carro? '))

#print('Carro novo' if tempo <=3 else 'Carro velho')

#print('--FIM--')

nome = str(input('Qual o seu nome? '))

if nome == 'Lucas':
    print('Seu nome é lindo!')
else:
    print('Seu nome é tão normal')
print('Bom dia {}!'.format(nome))

# Outro Exemplo:

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Sua média é {}!'.format(m))
if m >= 6:
    print('Parabéns você passou!!!')
else:
    print('Estude mais!!!')

# Ou

print('Parabéns você passou!!!' if m >=6 else 'Estude mais!!!')