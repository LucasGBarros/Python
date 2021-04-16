# A função "IMPORT" é de importar arquivos/funções para serem utilizados, uma vez importado os dados, já pode ser utilizado.
# A função IMPORT traz todas as informações de dados de funções sem excessões.

# A função "FROM" ela denomina qual tipo de função você quer utilizar,
# sendo assim, ao invés de importar todas as funções, vocÊ utiliza apenas o necessário.

#EX: Função IMPORT

#import math (trouxe todas as funções do MATH).

#EX: Função FROM

#from match import sqrt (Chamando a função e denominando qual função que irá ser utilizado).

import math                             # Função IMPORT
num = int(input('Digite um valor: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é de {:.2f}'.format(num, raiz))

from math import sqrt, floor            # Função FROM
num = int(input('Digite um valor: '))
raiz = sqrt(num)
print('A raiz de {} é de {:.2f}'.format(num, floor(raiz)))