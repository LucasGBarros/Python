print("""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
 podem ou não formar um triângulo""")

print('-=' * 20)

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

# Testando se é triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos da reta, PODEM formar um triângulo.')
else:
    print('Os segmentos da reta, NÃO podem formar um triângulo.')


"""if (r1 + r2 < r3) or (r1 + r3 < r2) or (r2 + r3 < r1):

    print('Não pode ser formado um triângulo')

elif (r1 == r2) and (r1 == r3):

    print('Equilátero = Todas as retas são iguais.') # Um triângulo equilátero é todos os triângulos em que os três lados são iguais

elif (r1 == r2) or ( r1 == r3) or (r2 == r3):

    print('Isóceles = As duas retas recebem a mesma medidas.') # Um triângulo isósceles é um triângulo que possui dois lados de mesma medida

else:

    print('Escaleno = As duas retas dos lados são diferentes.') # Um triângulo é escaleno quando as medidas dos lados são todas diferentes"""

print('-=' * 20)