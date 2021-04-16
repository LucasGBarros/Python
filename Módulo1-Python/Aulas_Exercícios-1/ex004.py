print("""Faça um programa que leia algo pelo teclado e mostre na tela o seu ripo primitivo e todas as informações
      possíveis na tela.""")

a = input('Digite algo: ')

print('O tipo de primitivo desse valor é ', type(a))

print('Só tem espaço? ', a.isspace())

print('É um número? ', a.isnumeric())

print('É alfabético? ', a.isalpha())

print('É minúsculo? ', a.islower())

print('É Maiúsculo? ', a.isupper())

print('É alfanumérico? ', a.isalnum())

print('É capitalizada? ', a.istitle())