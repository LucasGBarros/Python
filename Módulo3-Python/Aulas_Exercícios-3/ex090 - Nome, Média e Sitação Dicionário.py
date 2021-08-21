print("""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final
mostre o conteúdo da estrutura na tela.""")
print()

print(f'{" Média Escolar ":=^40}')
print()

dados = {'Nome': '', 'Média': '', 'Sitação': ''}

dados['Nome'] = str(input('Digite seu nome: '))
dados['Média'] = float(input('Qual sua média: '))

if dados['Média'] >= 6:

    dados['Sitação'] = 'Aprovado'

elif dados['Média'] <= 6 and dados['Média'] >= 5:

    dados['Sitação'] = 'Recuperação'

else:

    dados['Sitação'] = 'Reprovado'

for k, v in dados.items():

    print(f'{k} é igual a {v}.')

print()
print('='*40)