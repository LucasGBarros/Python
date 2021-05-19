print(f'{" APÊNDICE 1 ":=^40}')

print('''
PREENCHA O FORMULÁRIO
''')

from time import sleep

menu = 0

nome = str(input('Nome: '))

while menu != 7:

    print('''
Olá {}, tudo bem?

Em qual quadro se encaixa a sua idade?

[1] 18 - 20 ANOS;
[2] 21 - 30 ANOS;
[3] 31 - 40 ANOS;
[4] 41 - 50 ANOS;
[5] 51 - 60 ANOS;
[6] 61 ou mais;
[7] FECHAR PROGRAMA!
'''.format(nome.strip().title()))

    menu = int(input('Digite a sua opção: '))

    if menu == 1 or menu == 2 or menu == 3 or menu == 4 or menu == 5 or menu == 6:      # Informando Quadro de Sexo

        print('''Ok, carregando informações...''')

        sleep(2)

        sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

        while sexo not in 'MmFf':

            sexo = str(input('Dados inválidos, digite novamente seu sexo: [M/F] '))

        print(f'Sexo {sexo.upper()} registrado com sucesso.')

        break

    if menu != 7:

        print('Opção inválida! Tente novamente!')


sleep(1.5)

print('Finalizando...')

sleep(2)

print('Formulário Encerrado!')
