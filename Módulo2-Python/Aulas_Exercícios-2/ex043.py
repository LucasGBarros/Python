print("""Desenvolva uma lógica que leia o peso e a aultura de uma pessoa, calcule seu IMC e ostre seu sttatus,
de acordo com a tabela abaixo:

- Abaixo de 18.5: abaixo do peso.

- Entre 18.5 e 25: peso ideal.

- 25 até 30: Sobrepeso.

- 30 até 40: Obesidade.

- Acima de 40: Obesidade Mórbida.""")


print('='*50)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite a sua Altura: '))

imc = peso / (altura * altura) # Ou "imc = peso (altura ** 2)

if imc <= 18.5:

    print('Seu índice de massa corporal é de {:.1f}. Você está abaixo do peso.'.format(imc))

elif (imc >= 18.5) and (imc <= 25): # Ou podendo ser "18.5 <= imc < 25"

    print('Seu índice de massa corporal é de {:.1f}. Peso ideal para o seu corpo. Parabéns!!'.format(imc))

elif (imc >= 25) and (imc <= 30): # Ou podendo ser  "25 <= imc < 30"

    print('Seu índice de massa corporal é de {:.1f}. Você está Sobrepeso'.format(imc))

elif (imc >= 30) and (imc <= 40): # Ou podendo ser "30 <= imc <40

    print('Seu índice de massa corporal é de {:.1f}. Você está na Obesidade.'.format(imc))

else:

    print('Seu índice de massa corporal é de {:.1f}. Você está na Obesidade Mórbida.'.format(imc))

print('='*50)

