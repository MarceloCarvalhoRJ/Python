n = int(input('Digite um número: '))
primo = True
for i in range(2, n):
    if (n > 2) and (n % i == 0):
        primo = False
        break
if primo:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} NÃO é primo.')
    