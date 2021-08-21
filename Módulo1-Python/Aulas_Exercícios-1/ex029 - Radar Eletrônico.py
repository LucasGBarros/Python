print("""Escreva um programa que leia a velocidade de um carro.
      Se ele ultrapassar de 80km/h, mostre uma mensagem dizendo que ele foi multado.
      A multa vai custar R$ 7,00 por cada km acima do limite.""")

vel = float(input('Qual foi a velocidade percorrida? '))

multa = (vel - 80) * 7

if vel >= 80:
    print('Voce foi multado, este é o valor da multa R${:.2f}'.format(multa))
else:
    print('Parabéns, pode prosseguir seu caminho.')