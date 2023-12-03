    # Classes - São um tipo abstrato de dados
class Cliente: #Aqui estamos criando uma classe chamada cliente
    def __init__(self, nome, fone):  # Estamos definindo um método construtor, no caso esse init()
                        # é um método especial que será chamado sempre que criarmos um objeto da classe
        self.nome = nome   # Definindo os atributos da classe
        self.telefone = fone

        pass  # Usamos a palavra reservada pass quando nenhuma estrutura será definida no corpo da classe
