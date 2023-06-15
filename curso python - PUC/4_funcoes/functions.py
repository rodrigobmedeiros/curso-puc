# Definicao:

# Funcoes sao blocos de codigo responsaveis por determinada funcionalidade especifica. Tem intima relacao com as funcoes matematicas,
# onde basicamente temos um input de dados, a transformacao dos dados e o retorno dos dados transformados.

# VANTAGENS:
# 1. Reuso
# 2. Evitar repeticao de codigo
# 3. Base de codigo mais organizada
# 4. Mais facil de implementar testes unitarios
# 5. Mais facil manutencao da base de codigo
# 6. Manter codigo isolado e desacoplado - QUANTO MAIS ISOLADO MELHOR

# Estrutura
# Exemplo com cartorio (copia autenticada)

# def my_function(parameter_1, parameter_2):

#     # Transformacao dos dados
#     # Calculos com os parametros
#     # Neste exemplo simplesmente agrupando os parametros recebidos em uma lista

#     return [parameter_1, parameter_2]

# Uma funcao pode ter 0 -> N parametros com N sem limite superior

# BOA PRATICA: que a funcao tenha um numero reduzido de parametros (ate 3 parametros)


# Definicao de parametros default
def my_function(parameter_1, parameter_2='valor_default'):

    return [parameter_1, parameter_2]

# EXEMPLO:

# Crie uma funcao capaz de converter um valor de centimetro para metro e metro para centimetro.
def convert_cm_m(value, from_unit, to_unit):

    if from_unit == 'm':
        if to_unit == 'cm':
            return value * 100, 'cm'
        
    return value / 100, 'm' # Retorno de uma tuple

print(convert_cm_m(1, 'm', 'cm'))
print(convert_cm_m(100, 'cm', 'm'))

# O que pode ser melhorado nessa funcao?

# EXERCICIOS:

# Crie uma funcao que recebe uma temperatura em celsius e retorne a temperatura em Fahrenheit
# Eq: Tf = 32 + 9 * Tc /5

def c_to_f(tc):
    # Escreva seu codigo aqui
    ...

print(c_to_f(5)) # 41 °F
print(c_to_f(0)) # 32 °F
print(212 == c_to_f(100)) # 100 °F

# Crie uma funcao que receba um nome e print na tela a mensagem "Hello, nome"
def greeting(name):

    ...

# DISCUSSAO FINAL
# - Nome das funcoes
# - Nome dos parametros
# - Indicacao de leitura da PEP-8

# Falar rapidamente sobre funcoes anonimas

