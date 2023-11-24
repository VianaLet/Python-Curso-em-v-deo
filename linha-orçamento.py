produto_x = input("Qual é o produto x? ")  # Só para estética mesmo, o usuário saber de qual produto estamos nos referindo
px = float(input(f"Informe o preço do(a) {produto_x}: "))
produto_y = input("Qual é o produto y? ")
py = float(input(f"Informe o preço do(a) {produto_y}: "))
renda= float(input("Qual sua renda? "))
maxqtd_x = int(renda/px)
maxqtd_y = int(renda/py)
lista_qtd_x = []
lista_qtd_y = []
total = 0
print(maxqtd_x, maxqtd_y)
for i in range (maxqtd_x + 1):
    for j in range (maxqtd_x+ 1):    # Aqui vamos fazer os calculos com todos os números até 
        qtd_x = i                 # Chegar na máxima de x e y, calculamos anteriormente para
        qtd_y = j                      # Não precisar colocar o for com números imensos  
        total = px*qtd_x + py*qtd_y
        if (total == renda):            # Selecionando o limite, que é a renda do consumidor
            lista_qtd_x.append(qtd_x)   # Estamos fazendo uma seleção dessas quantidades à serem
            lista_qtd_y.append(qtd_y)   # inseridas nas listas, para então podermos vizualizá-las
            print(f"Preço {produto_x}: {px} Quantidade: {lista_qtd_x}")
            print(f"Preço {produto_y}: {py} Quantidade: {lista_qtd_y}\n  Total: {total}")
"""
O que irá aparecer no console:
Preço Arroz: 2.0 Quantidade: [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
Preço Feijão: 5.0 Quantidade: [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
Total: 100.0
"""