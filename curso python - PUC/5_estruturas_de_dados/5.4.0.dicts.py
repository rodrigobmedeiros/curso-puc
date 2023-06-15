'''
Dicionario eh uma estrutura de dados que armazena uma colecao de elementos no formato chave-valor.

Ex: {
    nome: 'rodrigo', 
    idade: 37
}

A principal vantagem dos dicionarios eh acessar diretamente um determinado valor sem necessidade de uma busca extensiva.
'''

'''
1 - Criação de dicionários:
'''
user = { "nome": "rodrigo", "email": 'rodrimedeiros' }
address = { "rua": "leopoldo miguez", "numero": 29, "CEP": "22060-021"}

count_letters = dict.fromkeys(['a', 'b', 'c'], 0)
print(count_letters)

user_rodrigo = dict([("nome", "rodrigo"), ("idade", 37)])
print(user_rodrigo)

'''
2 - Exemplos de situacoes para utilizar dicionarios
'''
# Arquivos de configuracao
# Tomada de decisao
# Agrupamento de informacoes 

'''
3 - Acesso aos valores por chave:
'''
trocador_de_calor = { "tipo": "casco-tubo", "T entrada [ºC]": 100, "T saida [ºC]": 200, "P operacao [bar]": 1 }
print(trocador_de_calor["tipo"])
print(trocador_de_calor["T entrada [ºC]"])
print(trocador_de_calor["T saida [ºC]"])
print(trocador_de_calor["P operacao [bar]"])
# trocador_de_calor["status"] # Caso a chave nao exista um erro eh disparado (KeyError)

# Como evitar esse problema?

'''
4 - Chaves devem ser imutaveis:
'''
# mostrar exemplos com chaves imutaveis

'''
5 - Redefinicao dos valores:
'''
print(trocador_de_calor)
trocador_de_calor["T entrada [ºC]"] = 150
print(trocador_de_calor)

'''
Iteração sobre chaves e valores:

Você pode iterar sobre as chaves ou os valores de um dicionário usando os métodos keys(), values() ou items().

for chave in dicionario.keys():
    print(chave)

for valor in dicionario.values():
    print(valor)

for chave, valor in dicionario.items():
    print(chave, valor)
'''

