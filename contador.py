# > Exemplo número dois de while com um contador
contador = 0

while contador < 5:  # Enquanto for menor que 5 vai realizar o bloco de código identado abaixo
    print(contador)
    contador = contador + 1

print('Fim do programa')  # Finalização do bloco de código do while


# > Laço de repetição For - Ele permite a gente criar estruturas de loop de forma
# controlada, quando sabemos quantas vezes queremos repetir o código

for cont in range(5):  # O range vai definir a faixa de valor de 0 até < 5
    print(cont)

for i in range(1,10):  # O range vai de 1 até < 10
    print(i)

for a in range(5,8):  # aqui vamos começar do número 5 até <8
    print(a)

for n in range(1,12,3):  #Aqui adicionamos um outro parametro na range,
# ele significa de quanto em quanto iremos pular. No caso de 1 até <12 pulando de 3 em três
    print(n)
