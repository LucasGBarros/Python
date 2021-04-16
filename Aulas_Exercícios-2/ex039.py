print("""Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade.

- Se ele \033[:33mainda vai se alistar\033[m ao serviço militar.

- Se é a \033[:33mhora de se alistar\033[m.

- Se já \033[:33mpassou do tempo\033[m do alistamento.

Seu programa deverá mostrar o tempo que faltou ou que passou do prazo.

""")

from datetime import date

print("""Digite sua data de nascimento e direi o tempo e se deverá se alistar ou não.
""")

atual = date.today().year

print("""Informe seu sexo

[1] Masculino
[2] Feminino""")

sexo = int(input('Qual é a sua opção? '))

if sexo == 1:

    print('Vamos analisar seus dados.')

else:

    sexo = 2

    print('Você não é obrigada a se Alistar.')

    quit()

ano = int(input('Ano em que você nasceu: '))

idade = date.today().year - ano - 1

print('Analisando os dados . . .')

print('Você nasceu em {:.0f}, tem {} anos em {}.'.format(ano, idade, atual))

if idade < 18:

    saldo = 18 - idade

    print('Você ainda irá se alistar! Faltam exato {:.0f} anos para se alistar.'.format(saldo))

    anoalis = atual + saldo

    print('Seu alistamento será em {}.'.format(anoalis))

elif idade == 18:

    print('Já está na hora de se alistar!')

elif idade > 18:

    saldo = idade - 18

    print('Seu tempo de ALISTAMENTO já se passou {:.0f} anos, vá se alistar.'.format(saldo))

    anoalis = atual - saldo

    print('Voce deveria ter se alistado em {}'.format(anoalis))
