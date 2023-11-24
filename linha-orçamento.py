produto_x = input("Qual é o produto x? ")
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
for i in range (maxqtd_x):
    for j in range (maxqtd_x):
        qtd_x = i
        qtd_y = j
        total = px*qtd_x + py*qtd_y
        if (total == 100):
            lista_qtd_x.append(qtd_x)
            lista_qtd_y.append(qtd_y)
            print(f"Preço {produto_x}: {px} Quantidade: {lista_qtd_x}")
            print(f"Preço {produto_y}: {py} Quantidade: {lista_qtd_y}\n  Total: {total}")