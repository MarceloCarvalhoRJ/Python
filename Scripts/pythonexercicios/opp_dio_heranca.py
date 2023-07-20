class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
 
    def ligar_motor(self):
        print("Ligando o motor")

    #exibe o nome da classe
    def __str__(self):
        #percorre a chave e valor dentro da classe.  
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}" #tem que usar o items para retornar a chave e valor, pois estamos acessando o dicinário de dados. 


class Motocilceta(Veiculo):
    pass
    

class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        self.carregado = carregado
        super().__init__(cor, placa, numero_rodas)

    def esta_carregado(self):
        print(f'{"sim" if self.carregado else "nao"}, estou carregado!')


moto = Motocilceta('preta', 'abc-1234', 2)
carro = Carro('Branco', 'xde-0098', 4)
caminhao = Caminhao('roxo', 'gfd-8712', 8, False)

#caminhao.ligar_motor()
#caminhao.esta_carregado()
print(moto)
print(carro)
print(caminhao)