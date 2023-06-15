# Crie uma funcao que retorne um dicionario contendo quantas vezes cada numero aparece em uma lista
def count_numbers(numbers):

    ...

numbers = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]
print(count_numbers(numbers))


# Palavra mais frequente: Crie uma funcao que recebe uma lista de palavras e retorne a palavra mais frequente
def most_frequent_word(words):

    ...


names = ['rodrigo', 'rodrigo', 'rodrigo', 'renata', 'rafael', 'andre', 'matias']
print(most_frequent_word(names))

# Comentar que o sorted atua diretamente nas chaves de um dicionario
# Como alterar o comportamento da funcao sorted?
# Como obter o par chave valor?

# Crie uma funcao que calcule o salario total de funcionarios de diferentes funcoes:
# A funcao vai receber dois parametros: O salario base e o cargo do funcionario
# A funcao deve retornar o salario total = salario base + bonus
# BONUS DE CADA CARGO
# - vendedor: 1200
# - analista: 1500
# - engenheiro: 2000
# - gerente: 2500
def calc_total_salary(base_salary, position):
    ...

print(calc_total_salary(2000, 'vendedor')) # resultado: 3200
print(calc_total_salary(3000, 'analista')) # resultado: 4500
print(calc_total_salary(5000, 'engenheiro')) # resultado: 7000
print(calc_total_salary(7000, 'gerente')) # resultado: 9500