'''
O uso do bloco finally é útil para realizar ações de limpeza ou liberação de recursos,
como fechar arquivos, conexões de banco de dados ou desalocar memória. Isso garante que
essas ações sejam realizadas, independentemente de ocorrerem exceções ou não durante a
execução do bloco try.
'''

NAMES = ['rodrigo']

def write_file():
    arquivo = None
    try:
        arquivo = open("dados.txt", "w")
        arquivo.write(NAMES[2])
    except IndexError:
        print("Erro: NAMES contem apenas um nome")
    finally:
        if arquivo:
            arquivo.close()
            print("Arquivo fechado.")

write_file()
