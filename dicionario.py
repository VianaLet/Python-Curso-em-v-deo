# > DICIONÁRIOS

# Criando dicionários
dicionario = {}  # criando um dicionário vazio
dicionario = dict()  # também vazio

dicionario = {'nome': 'Letícia', 'Idade': 26, 'altura':1.77 }  # No dicionário a gente dá uma label (o nome da chave) e em seguida o valor {'label':'valor', 'labe2':'valor2'}

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionário

dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 2  # Aqui como a label altura já existe ele vai sobrescrever o valor que continha antes
print(dicionario)

# Iterando sobre um dicionário
for chave in dicionario:
  print(chave)    #  Aqui ele vai percorrer pelas chaves do dicionário, no caso nome, Idade, altura, programador

for chave in dicionario:
  print(chave, dicionari[chave])  # Aqui vamos puxar o valor que tem nas chaves

# Testando a existência de uma chave
print('peso' in dicionario) # Com esse comando ele vai me mostrar se tem essa chave no dicionário
print('altura' in dicionario)
