print(f'{" APÊNDICE 1 ":=^40}')

print('''
PREENCHA O FORMULÁRIO
''')

from time import sleep

menu = 0

nome = str(input('Nome: '))

while True:

    while menu != 6:

        print('''
Olá {}, tudo bem?
    
Em qual quadro se encaixa a sua idade?
    
[1] 18 - 20 ANOS;
[2] 21 - 30 ANOS;
[3] 31 - 40 ANOS;
[4] 41 - 50 ANOS;
[5] 51 - 60 ANOS;
[6] 61 ou mais;
    '''.format(nome.strip().title()))

        menu = int(input('Digite a sua opção: '))

        if menu == 1 or menu == 2 or menu == 3 or menu == 4 or menu == 5 or menu == 6:  # Informando Quadro de Sexo

            sleep(1)

            print('''Ok, carregando informações...''')

            sleep(2)

            sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]  # Utilizando métodos de String e
            # Fatiamento.

            while sexo not in 'MmFf':

                sexo = str(input('Dados inválidos, digite novamente seu sexo: [M/F] '))  # Informando sexo correto

            sleep(1)

            print(f'Sexo {sexo.upper()} registrado com sucesso.')

            break

        elif menu != 6:  # Tentando novamente

            print('Opção inválida! Tente novamente!')

    sleep(1)

    menu = 0

    while menu != 4:

        sleep(1)

        print(f'{" Estado Civil ":=^40}')

        sleep(1)

        print('''
Informe seu Estado Civil
        
[1] Solteiro.
[2] Casado.
[3] Divorciado.
[4] Viúvo.
        ''')

        menu = int(input('Qual a sua opção? '))

        if menu == 1:

            sleep(1)

            print('Carregando dados...')

            sleep(1)

            menu = 'Solteiro'

            print(f'Seu Estado Civil {menu} foi registrado com sucesso.')

            break

        elif menu == 2:

            sleep(1)

            print('Carregando dados...')

            sleep(1)

            menu = 'Casado'

            print(f'Seu estado Civil {menu} foi regstrado com sucesso.')

            break

        elif menu == 3:

            sleep(1)

            print('Carregando dados...')

            sleep(1)

            menu = 'Divorciado'

            print(f'Seu Estado Civil {menu} foi registrado com sucesso.')

            break

        elif menu == 4:

            sleep(1)

            print('Carregando dados...')

            sleep(1)

            menu = 'Viúvo'

            print(f'Seu Estado Civil {menu} foi registrado com sucesso.')

            break

        if menu != 4:
            sleep(1)

            print(f'{" Estado Civil ":=^40}')

            sleep(1)

            print("""
Informe seu Estado Civil
                    
[1] Solteiro.
[2] Casado.
[3] Divorciado.
[4] Viúvo.
    """)

        menu = int(input('Qual a sua opção? '))

    break
