print('''Crie um programa onde o usuário digita uma expressão qualquer que use parêntes. Seu aplicativo deverá analisar 
se a expressão passada está com os parênteses abertos ou fechados na ordem correta.''')

expr =  str(input('Digite sua expressão: '))

pilha = []

for simb in expr:

    if simb == '(':

        pilha.append('(')

    elif simb == ')':

        if len(pilha) > 0:

            pilha.pop()

        else:

            pilha.append(')')

            break

if len(pilha) == 0:

    print('Su a expressão está válida.')

else:

    print('Sua expressão está inválida.')