'''Estrutura de Repetição WHILE = Interrompendo repetição'''

'''

Linguagem português:


Enquanto VERDADEIRO

    se BLOCO
        
        passo
        
    se MOEDA
        
        pega
        
    se TROFEU 
        
        pula
        
        INTERROMPA 

pega

'''

'''
# Linguagem Python TEÓRICA

bloco = passo = vazio = pula = moeda = pega = troféu = 0

while True:         # O TRUE, faz a função de repetiçção INFINITA

    if bloco:

        passo

    if vazio:

        pula

    if moeda:

        pega

    if troféu:      #Dentro desse "SE" a dunção Break irá dizer que é o fim do programa.

        pula

        break

pega'''

n = s = 0


while True: # TRUE repetição infinita

    n = int(input('Digite um número: '))

    if n == 999: # SE o FLAG 999 for utilizado, ele não será somado com as outras somas.

        break

    s += n

print('A soma vale {}'.format(s))

print(cont)