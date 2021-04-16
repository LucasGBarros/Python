print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.')

conv = float(input('Quantos R$ voce tem na sua carteira? '))

dollar = 5.69

print('Com R${:.2f}, dá para comprar US{:.2f} na casa de câmbio!'.format(conv, conv/dollar))
