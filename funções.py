# > Funções
# 1. O que são funções e por que utilizá-las?
# É um código que podemos usar diversas vezes, reaproveitando, que vai nos retornar um valor

"""
print()  # - imprime uma mensagem no console
input()  # - Retorna um dado informado pelo usuário(entrada padrão)
len()    # - Recebe uma lista e retorna o tamanho dessa lista
max()    # - Retorna o maior valor de uma lista
"""

#2. criação de funções

# Função inicial
def saudacao():
    print('Seja bem-vindo(a)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao()  # Aqui eu estou chamando a função que criei para ela ser usada

# Função com parâmetros
def saudacao(nome, curso):  # Aqui quando definimos coisas no parentese é como se criássemos variáveis
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao(input('Digite seu nome: '), input('Digite seu curso: '))