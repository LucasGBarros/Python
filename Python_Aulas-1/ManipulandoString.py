frase = 'Curso em Video Python' # Considerando que na letra "C" começa com 0 e a última letra "N" é 20

# Operador: Fatiamento

print(frase[9]) #o número colocado, serve para identificar uma unica letra da frase que eu quero selecionar
                # O tipo de colchetes é um indentificador de uma estrutura de dados chamado LISTA

print(frase[9:13])  # O ultimo número serve para selecionar até aonde eu quero que a frase acabe
print(frase[9:21])  # O algoritimo ":" serve para dar a função de até aonde eu quero que o texto seja selecionado

print(frase[9:21:2]) # O último número do colchete, serve para pular as letras das palavras que eu desejo que pule.

print(frase[:5]) # Como não tem o ínicio do texto, então a função :5 vai me mostrar até o final do texto até 5

print(frase[15:]) # Como eu indiquei o ínicio, e não tem o final, então ele vai selecionar o ínicio do 15 até a ultima frase do texto

print(frase[9::3]) # Será selecionado o ínicio do texto e como não indica o final, ele ira usar todo textos cortando de 3 em 3

# Operação Analise

frase = 'Curso em Video Python'

print(len(frase)) # A função len, mostra o comprimento da frase, mostrando quandos caracteres possui na frase

print(frase.count('o')) # A função count Contabiliza quantas letras "o" tem minuscula na frase
print(frase.count('o', 0, 13)) # Com a função count ", 0, 13" ele vai buscar dentro desse paramentro a letra 'o' da frase

print(frase.find('deo')) # A função Find, vai procurar na frase, uma palavra desejada, no caso 'deo'

print(frase.find('Android')) # Como na frase não stá a palavra 'Android', ele retorna como -1 pois não foi encontrado

print('Curso' in frase) # Com a função "in" ele vai me indicar se existe algum valor e me retorna como true ou false

# Operação Transformação

frase = 'Curso em Video Python'

print(frase.replace('Python', 'Android')) # A função Replace troca a palavra desejada do texto

print(frase.upper()) # A função UPPER, tem como trocar as palavras que estiverem minuscula para maiuscula

print(frase.lower()) # A função LOWER, transforma todas as letras maiuscula em minuscula da frase

print(frase.capitalize()) # A função CAPITALIZE, deixa todas as palavras minuscula, somente a primeira letra do inicio da frase

print(frase.title()) # A função title, contabiliza quantas frase tem, e coloca em maiusculo todas as letras de frase.

frase1 = '   Aprenda Python  '

print(frase1.strip()) # A função STRIP remove o espaçamento do inicio e o final da frase, mantendo o espaço entre as frase.

print(frase1.rstrip()) # A função RSTRIP irá remover o espaçamento somente da direita (OBS: R de Right = Direita)

print(frase1.lstrip()) # A função LSTRIP irá remover o espaçamento somente da esquerda (OBS: L de left = esquerda)

# Operação Divisão

frase = 'Curso em Video Python'

print(frase.split()) # A função SPLIT, divide a frase e cada palavra recebe uma indexação nova e cada uma dessas palavras, é colocada dentro de uma "LISTA"
