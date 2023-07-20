c0 = int(input('Digite um número: '))

etapas = 0
while c0 != 1:
    c0 = c0 / 2 if c0 % 2 == 0 else 3 * c0 + 1
    print(int(c0))
    etapas += 1
print('etapas =', etapas)