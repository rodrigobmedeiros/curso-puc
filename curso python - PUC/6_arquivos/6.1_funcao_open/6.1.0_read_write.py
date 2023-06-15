'''
Em python podemos manipular arquivos facilmente, principalmente com operacoes de leitura e escrita. Para isso, utilizamos
principalmente a funcao open(), que eh uma built-in function (ja vimos anteriormente o que sao as built-in functions).
'''

# Como utilizar a funcao open?
# caminho do arquivo (path) + modo de abertura (leitura, escrita...)
# Tipos de modo de abertura
# MAIS USADOS #
# 'r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	create a new file and open it for writing
# 'a'	open for writing, appending to the end of the file if it exists

# BOM SABER QUE EXISTE #
# 'b'	binary mode
# 't'	text mode (default)
# '+'	open a disk file for updating (reading and writing)
# 'U'	universal newline mode (deprecated)

'''
Escrevendo um arquivo em modo de escrita ('w')
'''

base_path = "6_arquivos/6.1_funcao_open"

arquivo = open(f"{base_path}/src/arquivo.txt", "w")
arquivo.write("Hello World!\n")  
arquivo.close()

'''
Adicionar conteúdo a um arquivo existente sem sobrescrevê-lo
'''
arquivo = open(f"{base_path}/src/arquivo.txt", "a")
arquivo.write("Hello World! (2x)") 
arquivo.close()


'''
Abrir um arquivo em modo de leitura usando o modo "r"
Para ler o conteudo dos arquivos pode-se usar os seguintes métodos:
read(), readline() ou readlines()
'''
arquivo = open(f"{base_path}/src/arquivo.txt", "r")
print(arquivo.read())
arquivo.close()

arquivo = open(f"{base_path}/src/arquivo.txt", "r")
print()
print('Leitura linha a linha:')
for line in arquivo.readlines():
    print(line, end='')
arquivo.close()

'''
É Recomendado o uso do bloco with 
'''

with open(f"{base_path}/src/arquivo_2.txt", "w") as arquivo:
    arquivo.write("Exemplo de conteudo.\n")
    arquivo.write("Outra linha de texto.\n")
    arquivo.write("Mais uma linha.\n")
