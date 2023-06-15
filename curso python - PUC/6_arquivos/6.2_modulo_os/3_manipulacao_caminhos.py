'''
O módulo os.path em Python fornece várias funções úteis para manipulação 
de caminhos e nomes de arquivos. Essas funções ajudam a lidar com caminhos 
de forma portátil, independentemente do sistema operacional.
'''

'''
1 - Juntar partes de um caminho
'''
import os

directory = "/caminho/para/o/diretorio"
file_name = "arquivo.txt"
path = os.path.join(directory, file_name)
print(path)


'''
2 - Obter o nome do diretório de um caminho
'''

path = "6_arquivos/2_modulo_os/3_manipulacao_caminhos.py"
directory_name = os.path.dirname(path)
print(directory_name)

'''
3 - Obter o nome do arquivo de um caminho:
'''

path = "6_arquivos/2_modulo_os/3_manipulacao_caminhos.py"
file_name = os.path.basename(path)
print(file_name)


'''
4 - Verificar se um caminho é absoluto
'''
path = ""
if os.path.isabs(path):
    print("O caminho é absoluto.")
else:
    print("O caminho não é absoluto.")

'''
5 - Obter o caminho do modulo atual com a variavel __file__
'''

path = os.path.abspath(__file__)
print(path)