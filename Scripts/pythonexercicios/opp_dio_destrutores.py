class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("inicilizando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado


    def __del__(self):
        print('Removendo a instância da classe.')

    def latir(self):
        print('Latindo...au au au')
    
def criar_cachorro():
    c = Cachorro('Zeus', 'Branco e Preto', False)
    print(c.nome)

c = Cachorro('Conan', 'Preto e Laranja')
c.latir() 

print('Ola Mundo!')
print('Ola Mundo!')
print('Ola Mundo!')
print('Ola Mundo!')

#criar_cachorro()  

