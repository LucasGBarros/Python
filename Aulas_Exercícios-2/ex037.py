print("""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a 
\033[:34mbase de uma conversão\033[m.

- \033[:34m1\033[m para \033[:33mbinário\033[m.
- \033[:34m2\033[m para \033[:33moctal\033[m.
- \033[:34m3\033[m para \033[:33mhexadecimal\033[m.
""")

print('='*100)

num = int(input('Digite um número inteiro: '))

print("""Escolha uma base de conversão sobre o número inteiro que você digitou.

[1] \033[:34mBinário\033[m.

[2] \033[:34mOctal\033[m.

[3] \033[:34mHexadecimal\033[m.""")

opcões = int(input("""Qual a opção que voce deseja? """))

if opcões == 1:

    print('O valor inteiro {} que você escolheu, convertido para \033[:34mBINÁRIO\033[m fica: {}'.format(num, bin(num)[2:]))

elif opcões == 2:

    print('O valor inteiro {} que você escolheu, convertido para \033[:34mOCTAL\033[m fica: {}'.format(num, oct(num)[2:]))

elif opcões == 3:

    print('O valor inteiro {} que você escolheu, convertido para \033[:34mHEXADECIMAL\033[m fica: {}'.format(num, hex(num)[2:]))

else:

    print('Opção inválida, tente novamente!')

print('='*100)