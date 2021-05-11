print('{:=^40}'.format(' APÊNDICE 1 '))

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

    if menu == 1:

        print('''Ok, carregando informações...''')

        sleep(2)

        sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

        while sexo not in 'MmFf':
            sexo = str(input('Dados inválidos, digite novamente seu sexo: [M/F] '))

        print('Sexo {} registrado com sucesso.'.format(sexo.upper()))

        break


    elif menu == 2:

        print('Ok, carregando informações...')

        sleep(2)

        sexo = str(input('Informe seu Sexo: [M/F] ')).strip().upper()[0]

        while sexo not in 'MmFf':
            sexo = str(input('Dados inválidos, digite novamente seu sexo: [M/F]'))

        print('Sexo {} registrado com sucesso.'.format(sexo.upper()))

        break

    elif menu == 3:

        print('Ok, carregando informações...')

        sleep(2)

        sexo = str(input('Informe seu sexo: [M/N] ')).strip().upper()[0]

        while sexo not in 'MmFf':
            sexo = str(input('Dados inválidos, digite novamente seu sexo: [M/F]'))

        print('Sexo {} registrado com sucesso.'.format(sexo.upper()))

        break

    elif menu == 4:

        print('Ok, carregando informações...')

        sleep(2)

        sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

        while sexo not in 'MmFf':
            sexo = str(input('Dados inválidos, digite novamente seu sexo: [M/F] '))

        print('Sexo {} registrado com sucesso.'.format(sexo.upper()))

        break

    elif menu == 5:

        print('Ok, carregando informações...')

        sleep(2)

        sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]

        while sexo not in 'MmFf':
            sexo = str(input('Dados inválidos, digite novamente seu sexo: [M/F] '))

        print('Sexo {} registrado com sucesso.'.format(sexo.upper()))

        break

    elif menu == 6:

        print('Ok, carregando informações')

        sleep(2)

        sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

        while sexo not in 'MmFf':
            sexo = str(input('Dados inválidos, digite novamente seu sexo: [M/F] '))

        print('Sexo {} registrado com sucesso.'.format(sexo.upper()))

        break

    elif menu == 7:

        sleep(2)

        print('Finalizando...')

    else:

        print('Opção Inválida! Tente novamente.')

sleep(2)

print('{:=^40}'.format(' Fim do Formulário! '))

print('''
Estado Civil:

[1] Solteiro
[2] Casado
[3] Divorciado
[4] Viúva(o)
''')