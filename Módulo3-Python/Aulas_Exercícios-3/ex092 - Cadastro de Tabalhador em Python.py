print("""Crie um Programa que leia Nome, Ano de Nascimento e Carteira de Trabalho e cadastre-os (com idade) em um 
Dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.""")

from datetime import datetime

print()

dados = dict()

dados['Nome'] = str(input('Digite seu nome: '))

nasc = int(input('Ano de Nascimento: '))

dados['Idade'] = datetime.now().year - nasc

dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['CTPS'] != 0:

    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)

print('=-'*30)

for k, v in dados.items():

    print(f'{k} tem o valor de {v}')

print('=-'*30)