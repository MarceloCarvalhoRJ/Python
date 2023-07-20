class Cachorro:
    def __init__(self, nome, cor, acordado=True):  #construtor
        print("inicilizando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado


    def __del__(self): #destrutor. Eh raro a sua utlização, pois o python tem um coletor de lixo automatico.
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

del c #força a remocão da instancia, senão acontecerá apenas no final.

print('Ola Mundo!')
print('Ola Mundo!')

#criar_cachorro()  

