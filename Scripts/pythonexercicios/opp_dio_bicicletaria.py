class Bicicleta: #cria a classe bicicleta
    #inicializa as caracteristicas (atributos) da classe, define o método construtor e insere os valores desejados.
    def __init__(self, cor, modelo, ano, valor, aro=700): # "self" eh uma ref. explícita p/o objeto. Representa a instância do objeto.
        self.cor = cor           #|       
        self.modelo = modelo     #|
        self.ano = ano           #|-> atributos da classe
        self.valor = valor       #|
    

    #metodos (funcoes dentro de uma classe) define o comportamento(ações) do objeto
    def buzinar(self): #obrigatorio a definicao de pelo menos um argumento dentro do método.
        print('Bibiiiiii.....')

    def parar(self):
        print('Parando a bike......Bike parada!')

    def correr(self):
        print('Pedale Rápido...vrunnnnn!')


    #exibe o nome da classe
    def __str__(self):
        #percorre a chave e valor dentro da classe.  
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}" #tem que usar o items para retornar a chave e valor, pois estamos acessando o dicinário de dados. 

bike_1 = Bicicleta('Preta', 'Estrada', 2015, 5000) #cria uma instancia de bicicleta
bike_2 = Bicicleta('Verde', 'BTT', 2010, 2000)

bike_1.buzinar()
bike_2.correr()  
bike_1.parar()  

#exibi os atributos da classe
print(f'A bike {bike_1.modelo} é da cor {bike_1.cor} do ano {bike_1.ano} e custa R$ {bike_1.valor},00')
Bicicleta.buzinar(bike_2) #essa chamada eh equivalente a bike_2.buzinar()
bike_2.buzinar()
print(bike_1)
print(bike_2)

