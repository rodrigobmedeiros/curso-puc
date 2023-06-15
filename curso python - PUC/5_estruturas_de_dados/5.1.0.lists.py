# Listas - definicao
# Basicamente sao containers, uma colecao de objetos python, os objetos podem ser de diferentes tipos sem restricao.

# Como as listas sao armazenadas na memoria?
# Como descobrir a dimensao de uma lista (quantos elementos a lista contem)?
# Como acessar cada valor atraves dos indices?
# Como modificar elementos em uma lista? -> Lista eh mutavel!
# Como inserir elementos em uma lista?
# Como remover elementos em uma lista?

# Exemplos
numbers = [1, 2, 3, 4, 5] # Lista de numeros
names = ["Alice", "Bob", "Charlie"] # Lista de strings
mixed = [10, "abc", True, 3.14] # Lista com elementos de diferentes tipos

countries = ['Argentina', 'Brasil', 'Canada', 'Dinamarca', 'EUA', 'França', 'Guiné-Bissau']

'''
1 - Acessar elementos da lista através de índices:
'''
print(countries[0])
print(countries[1])
print(countries[-1])


'''
2 - Modificar elementos da lista:
'''
# Alteracao do valor em tempo de execucao


'''
3 - Remover elementos da lista:
'''
# Uso do pop() ou remove() e del

'''
4 - Como descobrir a dimensao de uma lista 
'''

'''
5 - Como iterar por uma lista
'''
# Forma pythonica e nao-pythonica - uso do range e do enumerate


'''
6 - Exemplos de slice - Explorando a notacao de colchetes
'''
# lista[ini:fim:step]

lista = [1, 2, 3, 4, 5]
# print(lista[:2]) # Espero [1, 2]
# print(lista[2:]) # Espero [3, 4, 5]
# print(lista[1:4:2]) # Espero [2, 4]
# print(lista[::-1]) # Espero [5, 4, 3, 2, 1]

'''
7  - Adidionar elementos a uma lista
append()
soma simples
'''

'''
8 - Entendendo como a lista eh armazenada e referenciada na memoria
'''
x = [1, 2, 3, 4, 5]
y = x

x[2] = 500

print(x)
print(y)

# Como resolver esse problema?

