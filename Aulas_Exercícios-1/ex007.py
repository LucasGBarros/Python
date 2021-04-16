print('Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.')

n1 = float(input('Primeira Nota: '))

n2 = float(input('Segunda Nota: '))

m = (n1 + n2) / 2 # Para utilizar a média, sempre deverá estar dentro dos parentêses como ordem de precedências

print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, m))
# Todos os tipos de números que obtem uma média, a função poderá ser FLOAT