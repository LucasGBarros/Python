print(f'{" APÊNDICE 1 ":=^40}')

print('''
PREENCHA O FORMULÁRIO
''')

menu = familia = 0


while True:

    nome = str(input('Nome: '))

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

            sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]  # Utilizando métodos de String e
            # Fatiamento.

            while sexo not in 'MmFf':

                sexo = str(input('Dados inválidos, digite novamente seu sexo: [M/F] '))  # Informando sexo correto

                print(f'Sexo {sexo.upper()} registrado com sucesso.')

            break

        elif menu != 6:  # Tentando novamente

            print('Opção inválida! Tente novamente!')

    menu = 0

    while menu != 4:

        print(f'{" Estado Civil ":=^40}')

        print('''
Informe seu Estado Civil
        
[1] Solteiro.
[2] Casado.
[3] Divorciado.
[4] Viúvo.
        ''')

        menu = int(input('Qual a sua opção? '))

        if menu == 1:

            menu = 'Solteiro'

            print(f'Seu Estado Civil {menu} foi registrado com sucesso.')

            break

        elif menu == 2:

            menu = 'Casado'

            print(f'Seu estado Civil {menu} foi regstrado com sucesso.')

            break

        elif menu == 3:

            menu = 'Divorciado'

            print(f'Seu Estado Civil {menu} foi registrado com sucesso.')

            break

        elif menu == 4:

            menu = 'Viúvo'

            print(f'Seu Estado Civil {menu} foi registrado com sucesso.')

            break

        if menu != 4:

            print(f'{" Estado Civil ":=^40}')

            print("""
Informe seu Estado Civil
                    
[1] Solteiro.
[2] Casado.
[3] Divorciado.
[4] Viúvo.
    """)

        menu = int(input('Qual a sua opção? '))

    familia = 0

    while familia != 4:

        print('''Quantas pessoas moram com você? 
    
[1] Moro Sozinho(a).
[2] Uma a Três.
[3] Quatro a Sete.
[4] Oito ou Mais
''')

        familia = int(input('Qual sua opção? '))

        if familia == 1:

            menu = 'Moro Sozinho'

        elif familia == 2:

            menu = 'Uma a Três'

        elif familia == 3:

            menu = 'Quatro a Sete'

        elif familia == 4:

            menu = 'Oito ou Mais'

        break