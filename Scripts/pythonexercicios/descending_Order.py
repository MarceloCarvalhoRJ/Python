
def descending_order(num):
    return int(''.join(sorted(str(num), reverse = True)))
# transforma em string para fazer o ordenamento e depois retorna como inteiro.
num = 37639
#print(descending_order(num))
'''lista = []
x =  list()
di = dir(x)
for i in di:
    di = i.replace('__', '')
    lista.append(di.replace('__', ''))
print(lista)'''

numeros = []
while True:
    num = input('Digite um numero (done /sair): ').lower()
    if num == 'done': break
    numero = float(num)
    numeros.append(numero)
average = sum(numeros) / len(numeros)
print(f'Average of the {numeros} is equal a {average}')
