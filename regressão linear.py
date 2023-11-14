
distancia = [215, 480, 325, 550, 920, 670, 825, 1070, 1350, 1215]       # Lista que irá ficar no eixo x
tempo = [1, 1, 1.5, 2, 3, 3, 3.5, 4, 4.5, 5]                            # Lista que irá ficar no eixo y
tabela = []                                                     # Tabela vazia, posteriormente preenchida com pares x,y
quadrado_x_lista = []
quadrado_y_lista = []
xy_lista = []
somatoria_quadrado_y = 0
somatoria_quadrado_x = 0
somatoria_x = sum(distancia)
media_x = somatoria_x/len(distancia)
somatoria_y = sum(tempo)
media_y = somatoria_y/len(tempo)
somatoria_xy = 0

for i in range(len(distancia)):
    pares = [(distancia[i], tempo[i])]  # Aqui estou ordenando os pares das listas: distancia e tempo
    tabela = tabela + pares

for n in range(len(distancia)):
    xy_lista.append(distancia[n] * tempo[n])


for x in range(len(distancia)):                 # Preenchendo a lista de x²
    quadrado_x_lista.append(distancia[x]**2)

for y in range(len(tempo)):                     # Preenchendo a lista de y²
    quadrado_y_lista.append(tempo[y]**2)        # apesar de não precisar desse valor na fórmula foi válido o aprendizado

somatoria_xy = sum(xy_lista)
somatoria_quadrado_x = sum(quadrado_x_lista)    # Armazenando a somatória da lista de x²
somatoria_quadrado_y = sum(quadrado_y_lista)    # Armazenando a somatória da lista de y²
print(f'Tabela: {tabela}')                      # Mostrando no terminal as listas ordenadas
print("y²: ", quadrado_y_lista)
print("x²: ", quadrado_x_lista)
print("Σx: ", somatoria_x)
print("Σy: ", somatoria_y)
print("Σxy: ", somatoria_xy)
print("Σx²: ", somatoria_quadrado_x)        # apesar de não precisar desse valor na fórmula foi válido o aprendizado
print("Σy²: ", somatoria_quadrado_y)

a = (somatoria_xy - (somatoria_x * somatoria_y/len(distancia)))/ (somatoria_quadrado_x - (somatoria_x**2)/len(distancia))
print("Coeficiente a: ",a)
b = media_y - a * media_x
print("Coeficiente b: ", b)
print(f"Resultado: y = {round(a,4)}x + {round(b,4)}")
valor = float(input("Digite o valor que deseja prever o tempo de acordo com a relaão dessa tabela: "))
y = a * valor + b
print(f'O tempo em dias estimado para entrega é de: {round(y,1)}')

