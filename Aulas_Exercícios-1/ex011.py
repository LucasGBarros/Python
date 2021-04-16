print("""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
       e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma
       área de 2m².""")

alt = float(input('Qual a Altura da sua parede? '))

larg = float(input('Qual a largura de sua parede? '))

print('Considerando que a dimensão da sua parede é de {:.2f}x{:.2f}.\nSua parede tem {:.2f}m²\nA quantidade de tinta para ser utilizada é de: {:.4f}l.'.format(alt, larg, alt*larg, (alt*larg)/2))

larg = float(input('Qual a Largura de sua parede: '))

alt = float(input('Qual a Altura de sua parede? '))

área = larg * alt

print('A sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m²'.format(larg, alt, área))

tinta = área / 2

print('Para pintar essa parede, você precisará de {:.1f}l de tinta.'.format(tinta))


