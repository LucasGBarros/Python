print("""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.""")
print()


def voto(ano):
    from datetime import date

    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: Não Vota!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Opcional!'
    else:
        return f'Com {idade} anos: Obrigatório!'


nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
