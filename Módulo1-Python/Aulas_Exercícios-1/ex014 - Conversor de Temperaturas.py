print('Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.')

# Celcius

celcius = float(input('Informe a temperatura em ºC: '))

fahrenheit = ((9 * celcius) / 5 ) + 32

print('A temperatura de {:.1f}ºC é de {:.1f}ºF!'.format(celcius, fahrenheit))
