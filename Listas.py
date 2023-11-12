# > Listas   Criando listas no python
notas = [7.9, 9.7, 8.2]

lista = []  # Aqui é uma lista vazia
listav = list()  # Também estamos criando uma lista vazia
listas = [26, 'Wallisson', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação

print(listas[0])
print(listas[1])
print(listas[2])
print(listas[3])
print(listas[-1])  # Esse -1 é para pegar o último elemento de uma lista

# Slices(fatiamento)
lista = [10, 50, 30, 40, 25, 60, 5]
print(lista[0:3])  # Aqui ele vai pegar do índice 0 até o < que 3
print(lista[3:6])
print(lista[3:])  # Quando não definimos o final, ele irá até o final da lista de do índice 3 até o 6
print(lista[2:6:2])  # Aqui vamos selecionar do íncide 2 até o indice < 6 e pulando de 2 em 2

for elemento in lista:  # Estou pedindo para cada elemento da lista ele pecorrer e imprimir
    print(elemento)

print('Comprimento da lista', len(lista))  # o len vai me dizer a quantidade de elementos dentro da lista

for i in range(len(lista)):  # Aqui ele vai pegar e imprimir cada ele mento na posição do índice
    print(lista[i])