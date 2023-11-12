# Aqui vamos fazer um programinha que recebe de entrada as notas do aluno
# E mostra na saída a média dessas notas
soma = 0
for i in range(1, 4):  # No caso vamos solicitar 3 notas, o laço vai repetir tres vezes
    nota = float(input(f'Digite a sua {i}ª nota: '))
    soma = soma + nota

media = soma / i
print(f'Sua média é {media}')
print(i)
