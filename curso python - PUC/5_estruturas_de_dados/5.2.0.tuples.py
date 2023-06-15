'''
As tuples assim como as listas sao containers que podem conter elementos de diferentes tipos. A principal diferenca, 
eh que a tuple eh um tipo de estrutura de dados imutavel, onde nao eh possivel alterar seus elementos em tempo de execucao.
'''

'''
1 - Criação de tuplas:
'''
x = (1, 2, 3)
print(x)
print(type(x))

y = tuple([1, 2, 3])
print(y)
print(type(y))

'''
2 - Acesso aos elementos:
'''
# Acesso atraves de indices assim como as listas
names = ('rodrigo', 'bernardo', 'medeiros')
print(names[0])
print(names[1:])

'''
3 - Imutabilidade:
'''
megasena = (12, 17, 21, 32, 40, 50)
# megasena[0] = 21 # Espero que de um erro


'''
4 - Uso de tuplas em atribuições múltiplas:
'''
point = (1, 3)
x, y = point 
print(x)
print(y)

# Falar sobre o desempacotamento em sub-containers

'''
5 - Verificar se um elemento está presente na tupla:
'''
numbers = (1, 3, 5, 7, 9)
print(1 in numbers)
# validacao valida para qualquer container (qualquer objeto que siga o protocolo de iterator/iterable em python)