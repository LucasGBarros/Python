print("""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

- Média abaixo de \033[:33m5.0\033[m: \033[:34mREPROVADO\033[m.

- Média entre \033[:33m5.0\033[m e \033[:33m6.9\033[m: \033[:34mRECUPERAÇÃO\033[m.

- Média \033[:33m7.0\033[m ou superior: \033[:34mAPROVADO\033[m
""")

print('=' * 25, 'NOTA','=' * 25)

n1 = float(input('Qual a sua primeira nota? '))

n2 = float(input('Qual a sua segunda nota? '))

n3 = float(input('Qual a sua terceira nota? '))

n4 = float(input('Qual a sua quarta nota? '))

média = (n1 * n2 + n3 + n4) / 4

if média <= 5.0:

    print('Sua média foi de {}.'.format(média))
    print('Você está \033[:31mREPROVADO\033[m. Estude mais!!!')

elif 5.1 <= média <= 6.9:

    print('Sua média foi de {}.'.format(média))
    print('Você está de \033[:33mRECUPERAÇÃO\033[m. Estude para a próxima prova')

else:

    print('Sua média foi de {}.'.format(média))
    print('Voce está \033[:32mAPROVADO\033[m')

print('='*25)