print("""A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acord com a idade: 

- Até \033[33m9 anos\033[m: \033[34mMIRIM\033[m.

- Até \033[33m14 anos\033[m: \033[34mINFANTIL\033[m

- Até \033[33m19 anos\033[m: \033[34mJUNIOR\033[m

- Até \033[33m20 anos\033[m: \033[34mSÊNIOR\033[m

- Acima: \033[34mMASTER\033[m

""")

from datetime import date

print('==' * 25, 'DESAFIO 41' , '==' * 25)

print("""Olá, tudo bem? 

Para saber sua categoria, digite seu ano de nascimento.
""")

ano = int(input('Em que ano você nasceu? '))

idade = date.today().year - ano -1


if idade <= 9:

    print('Você tem {} anos, logo sua categoria é \033[34mMIRIM\033[m.'.format(idade))

elif 9 <= idade <= 14:

    print('Você tem {} anos, logo sua categoria é \033[34mINFANTIL\033[m.'.format(idade))

elif 14 <= idade <= 19:

    print('Você tem {} anos, logo sua categoria é \033[34mJUNIOR\033[m.'.format(idade))

elif 19 <= idade <= 20:

    print('Você tem {} anos, logo sua categoria é \033[34mSÊNIOR.\033[m.'.format(idade))

else:

    print('Você tem {} anos, logo sua categoria é \033[34mMASTER\033[m.'.format(idade))

print('==' * 56)