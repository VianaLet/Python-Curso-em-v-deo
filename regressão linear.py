
distancia = [215, 480, 325, 550, 920, 670, 825, 1070, 1350, 1215]
tempo = [1, 1, 1.5, 2, 3, 3, 3.5, 4, 4.5, 5]
tabela = []
quadrado_x_lista = []
quadrado_y_lista = []
somatoria_quadrado_y = 0
somatoria_quadrado_x = 0
for i in range(len(distancia)):
    pares = [(distancia[i], tempo[i])]  # Aqui estou ordenando os pares das listas: distancia e tempo
    tabela = tabela + pares

for x in range(len(distancia)):                 # Preenchendo a lista de x²
    quadrado_x_lista.append(distancia[x]**2)

for y in range(len(tempo)):                     # Preenchendo a lista de y²
    quadrado_y_lista.append(tempo[y]**2)

somatoria_quadrado_x = sum(quadrado_x_lista)    # Armazenando a somatória da lista de x²
somatoria_quadrado_y = sum(quadrado_y_lista)    # Armazenando a somatória da lista de y²
print(f'Tabela: {tabela}')               #Mostrando no terminal as listas ordenadas
print("y²: ", quadrado_y_lista)
print("x²: ", quadrado_x_lista)
print("Σx²: ", somatoria_quadrado_x)
print("Σy²: ", somatoria_quadrado_y)
