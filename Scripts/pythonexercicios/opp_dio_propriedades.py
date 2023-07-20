
class Pessoa:
    def __init__(self, nome, ano_de_nascimento):
        self.nome = nome
        self.data_de_nascimento = ano_de_nascimento

    #cria uma propriedade dentro da classe. simplifica, pois nao precisa inserir mais um atributo dentro do __init__
    #utilizar propriedades quando voce for usar esporadicamente um atributo.
    @property
    def idade(self):
        ano_atual = 2023
        return ano_atual - self.data_de_nascimento
    
pessoa_01 = Pessoa('Marcelo', 1972)
    
print(f'Nome: {pessoa_01.nome} \tIdade: {pessoa_01.idade}')