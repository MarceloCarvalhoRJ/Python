n = int(input('Digite um numero: '))
print(f'A tabuada de {n} é:')
for c in range(1, 11):
    print(f'{n} x {c:2} = {(n * c):2}')
