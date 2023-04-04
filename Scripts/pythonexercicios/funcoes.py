def titulo(msg):
    print('.' * (len(msg)))
    print(msg)
    print('.' * (len(msg)))

def potencia(a, b): # a to the power of b
    print(a ** b)

def average(*num): # empacotar parametros. aceita todos os valores infornados na chamada da funcao.
    print(sum(num) / len(num))

def dobra_valores(list):
   list = [num * 2 for num in list] #sintaxe de compreensão
   print(list)


titulo('Aprendendo Python')
titulo('I have been working hard on this!')

potencia(3, 3) # passando parametros para a funcao
average(10, 20, 30, 40, 50)

valores = [2, 4, 6, 8]
dobra_valores(valores)

def soma(a=0, b=0, c=0): #parametros opcionais. coloca as variaveis igual a zero, assim não dá erro se esquecer alguma variavel quando chamar no programa principal.
    s = a + b + c
    print(f'A soma dos valores {a}, {b}, e {c} é: {s}')

soma(2)
soma(2, 10)
soma(2, 10, 5)
print('.' * 40)

def fatorial(num=1):
    fat = 1 #precisa declarar o valor de 1 para assumir o primeiro valor em fat quando multiplicar por n.
    for n in range(num, 0, -1):
        fat *= n
    return fat

numero = int(input('Digite um número: '))
print(f'O fatorial de {numero} é: {fatorial(numero)}')