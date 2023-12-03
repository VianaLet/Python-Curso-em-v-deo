class Main:
    pass
print("Testando o projeto")

from Cliente import Cliente  # Estou importando a classe que criei mais cedo

from Conta import Conta
c1 = Cliente("João", "114444-2222")   # Declarando um novo objeto
conta = Conta(c1.nome, 6565, 0)
print(c1)   # Aqui será apresentado o ID do objeto
print(c1.nome, " e ", c1.telefone)   # Conteúdo do objeto "João e 114444-2222
print(conta.titular, "Número: ", conta.numero, "Seu Saldo: ", conta.saldo)