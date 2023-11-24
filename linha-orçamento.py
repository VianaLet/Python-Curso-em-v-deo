produto_x = input("Qual é o produto x?")
px = int(input(f"Informe o preço do(a) {produto_x}: "))
produto_y = input("Qual é o produto y?")
py = int(input(f"Informe o preço do(a) {produto_y}: "))
i = 1
qtd_x = 1
qtd_y = [0]
totalx = px*qtd_x
totaly = px*qtd_y

print(totalx)
while (totalx <= 100):
    qtd_x = i
    print(qtd_x)
    print(totalx)
    i = i + 1
if (totalx == 100):
    print(totalx)