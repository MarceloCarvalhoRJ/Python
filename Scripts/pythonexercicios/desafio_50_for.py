soma = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'A quantidade de numeros pares é {cont} e a soma é {soma}')  