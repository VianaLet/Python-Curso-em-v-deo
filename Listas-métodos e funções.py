# > MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

# append - adicionar um elemento ao final da lista
print('Antes do append: ', lista)

lista.append(3)
print('Depois do append: ', lista)

# insert - adiciona um elemento na posição que eu quiser escolher lista.insert(índice, elemento)
print('Antes do insert: ', lista)

lista.insert(2, 10)

print('Depois do insert: ', lista)

# extend - Ele vai unir duas listas.
lista2 = [1, 2, 3]
print('Lista1:', lista, '\nLista2', lista2)
lista.extend(lista2)  # Aqui ele está pegando a lista dois e colocando no final da lista1
print('Lista unida: ', lista)

# pop - para remover um elemento

lista.pop()  #Quando não passamos nenhum valor ele vai remover o último elemento
print('Lista após o pop: ', lista)

lista.pop(0)  # Aqui vamos remover o elemento localizado no índex 0
print('Lista após o pop: ', lista)

# remove  -vai remove o elemento escolhido
lista.remove(3)  # vai remover o primeiro elemento '3' que ele encontrar
print('Depois do remove: ', lista)

# count - vai contar a quantidade que um elemento x aparece na lista
print('Quantidade de 2 na lista: ', lista.count(2))

# index - Ele me diz o índice de determinado elemento
print('Índice do elemento 12: ', lista.index(12))

# sort - para ordenar a lista

lista.sort()  #Vai ordenar minha lista no valor crescente
print('Lista ordenada-crescente: ', lista)

lista.sort(reverse=True)  # Vai ordenar minha lista no valor decrescente
print('Lista ordenada-Decrescente: ', lista)

# Funções para listas

# len - saber quantos elementos tem na lista, ele conta o tamanho da lista
print(len(lista))

# sum - Vai somar todos os elementos dentro da lista
print(sum(lista))

# max - vai me retornar o maior elemento da lista
print('Maior elemento da lista: ', max(lista))

#min - vai me retornar o menor elemento da lista
print('Menor elemento da lista: ', min(lista))