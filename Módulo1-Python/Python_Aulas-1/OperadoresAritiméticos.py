#ORDEM DE PRECEDÊNCIA

# () -> Primeiro sempre calcular Parentêses!;

# (**) -> Após de parentêses, calcular Potências!;

# (* ou / ou // ou %) -> Calcular o que vier primeiro!;

# (+ ou -) -> Soma ou subtração binárias!;

# (==) -> Igual à;

# (=) -> Recebe.

n1 = int(input('Um valor: '))

n2 = int(input('Outro valor: '))

s = n1 + n2 #Soma

m = n1 * n2 #Multiplicação

d = n1 / n2 #Divisão

di = n1 // n2 #Divisão Inteira

e = n1 ** n2 #Exponenciação ou Potência

print('A soma é {} \n O produto é {} \n A divisão é {:.2f}'.format(s, m, d), end=' ')

print('\n A divisão inteira é {} \n Potencia {}'.format(di, e))