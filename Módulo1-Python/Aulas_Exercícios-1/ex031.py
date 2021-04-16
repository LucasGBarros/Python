print("""Desenvolva um programa que pergunte a distância de uma viagem em km. 
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km 
e R$ 0,45 para viagens mais longas.""")

viagem = float(input('Qual a distância em Km de sua viagem? '))

if viagem <= 200:
    preço = viagem * 0.50

    print('A passagem até 200Km custa R$ 0.50. Logo o valor da viagem é: R$ {:.2f}'.format(preço))
else:
    preço = viagem * 0.45

    print('A viagem mais longa custa R$0.40. Logo o valor da viagem é de: R$ {:.2f}'.format(preço))