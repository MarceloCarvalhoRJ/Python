# PRIMEIRA FUNCÃO
def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

print()
exibir_mensagem()
exibir_mensagem_2("Guilherme")
exibir_mensagem_3()
exibir_mensagem_3("Chappie")
print('.' * 40) 

# RETORNO DA FUNCÃO
def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)
print('.' * 40) 

# ARGUMENTOS NOMEADOS
def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # vantagem de informar o argumento com o valor é que o python sempre vai respeitar a sequencia em que elas foram informadas, mas cuidado pois se mudarem o nome do argumento na funcao vai retornar erro.
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # os ** informa para a funcao que se trata de um dicionario e ele vai interpretar cada chave como um argumento.
print('.' * 40)

#  «« EXIBIR POEMA »»
def exibir_poema(data_extenso, *args_tupla, **kwargs_chave_valor):
    """
    -> data_extenso vai pegar a primeira string informada na tupla.
    -> *args_tupla vai considerar todas as strings da tupla, separados por virgula por conta do '*' informado antes do arguemento.
    -> **kargs_chave_valor vai considerar todos os argumentos com chave e valor/dicionários.
    """
    texto = "\n".join(args_tupla)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs_chave_valor.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Sexta, 8 de Abril de 2023",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)
print('.' * 40)

# PARAMETROS SOMENTE POR POSIÇÃO

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    """
    Os argumentos antes da '/' so aceitam por posição(valores).  
    Os depois da '/' aceitam nomeados ou só por posição (as duas formas)
    """
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
print('.' * 40)

# PARAMETROS SOMENTE POR NOME:

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):   
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
print('.' * 40)

#OBJETOS DE PRIMEIRA CLASSE

def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
print('.' * 40)

# ESCOPO LOCAL E GLOBAL

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


print(salario_bonus(500))  # 2500
print('.' * 40)