class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        #percorre a chave e valor dentro da classe.  
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}" #tem que usar o items para retornar a chave e valor, pois estamos acessando o dicinário de dados. 


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw): #metodo Key wards
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
    
    
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    pass

gato = Gato(nro_patas=4, cor_pelo='preto')
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo='vermelho', cor_bico='laranja')
print(ornitorrinco)