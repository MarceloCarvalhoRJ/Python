##Este código usa um loop while que continua executando enquanto a quantidade de casos de teste n é maior que zero.
N = int(input())
resultados = []

#Dentro do loop, ele lê os valores de A e B separados por espaço usando o método split() da string input()
while(N > 0):
    
    a, b = input().split()
#Em seguida, ele verifica se B corresponde aos últimos dígitos de A usando o método endswith() da string a.
    if a.endswith(b):
#adicionamos o resultado de cada iteração à lista usando o método append().
        resultados.append('encaixa') 
    else:
        resultados.append('não encaixa')
    N -= 1
#loop for para imprimir cada resultado armazenado na lista. Dessa forma, a saída será impressa de uma só vez, no final do programa.
for resultado in resultados:
    print(resultado)

'''Dado de entrada:
4
56234523485723854755454545478690 78690
5434554 543
1243 1243
54 64545454545454545454545454545454554
Saída esperada:
encaixa
nao encaixa
encaixa
nao encaixa'''
