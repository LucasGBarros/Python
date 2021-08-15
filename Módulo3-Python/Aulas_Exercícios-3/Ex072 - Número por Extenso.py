print('''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem preenchida com uma contagem por 
extenso, de zero a vinte.

seu programa deverá ler um número pelo teclado (ente 0 e 20) e mostrá-lo por extenso.
''')

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'Cartoze', 'Quinze', 'Dezesseiz', 'Dezessete', 'Dezoito',
       'Dezenove', 'Vinte')

resp = 'S'

while resp in 'S':

    num = int(input('Digite um número entre 0 a 20: '))

    if num < 0 or num > 20:

        print('Tente novamente. ', end= '')

    else:

        print(f'Você digitou o número: {cont[num]}')

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':

        print('Fim do Programa!')

        break