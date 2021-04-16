import trigonometry
from math import hypot

print("""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.""")

co = float(input('Digite o valor de Cateto Oposto: '))

ca = float(input('Digite o valor de Cateto Adjacente: '))

hi = hypot(co, ca)

print('O valor da Hipotenusa é de {:.2f}'.format(hi))
