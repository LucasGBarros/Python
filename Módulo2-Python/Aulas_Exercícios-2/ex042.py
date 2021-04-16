print("""Refaça o DESAFIO 035 dos triângulos acrecentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: Todos os lados Iguais.

- Isósceles: Dois lados Iguais.
 
 - Escaleno: Todos os lados diferentes. 
 """)

r1 = float(input('Primeiro segmento: '))

r2 = float(input('Segunda segmento: '))

r3 = float(input('Terceira segmento: '))

if r1 + r2 < r3 or r1 + r3 < r2 or r2 + r3 < r1:

    print('Os segmentos PODEM formar um triângulo ', end=' ')

    if r1 == r2 == r3:

        print('EQUILÁTERO!') # Um triângulo equilátero é todos os triângulos em que os três lados são iguais

    elif r1 != r2 != r3 != r1:

        print('ESCALENO!') # Um triângulo é escaleno quando as medidas dos lados são todas diferentes

    else:

        print('ISÓSCELES') # Um triângulo isósceles é um triângulo que possui dois lados de mesma medida

else:
    print('Os segmentos acima NÃO podem formar um triângulo.')


