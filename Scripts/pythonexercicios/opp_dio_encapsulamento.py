#Encapsulamento - Acesso Publico e Privado.

class Conta:
    def __init__(self, nr_agencia, saldo=0):
        self.nr_agencia = nr_agencia

        # atributo saldo foi definido como privado, veja que inicia com '_'.
        self._saldo = saldo 
    
    def depositar(self, valor):
        #...
        self._saldo += valor

    def sacar(self, valor):
        #...
        self._saldo -= valor

    #maneira correta de acessar um atributo privado eh criando um método para acesso.
    def mostrar_saldo(self): 
        #...
        return self._saldo


conta = Conta('0001', 100)
conta.depositar(100)
conta.sacar(80)

#por convenção, não eh a maneira correta de acessar um atributo privado. Obs.: O Python não garante essa validação pelo interpretador.
print(conta._saldo) 

print(conta.nr_agencia)
print(conta.mostrar_saldo())