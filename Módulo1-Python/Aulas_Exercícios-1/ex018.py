import math

print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.')

ang = float(input('Digite um angulo: '))
print('Seno: {:.2f}'.format(math.sin(math.radians(ang))))
print('Cosseno: {:.2f}'.format(math.cos(math.radians(ang))))
print('Tangente: {:.2f}'.format(math.tan(math.radians(ang))))