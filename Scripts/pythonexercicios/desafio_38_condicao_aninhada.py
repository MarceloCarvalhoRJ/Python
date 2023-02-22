a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
if a > b:
    print(f'O número {a} é o maior!')
elif a < b:
    print(f'O numero {b} é o maior!')
else:
    print(f'Não existe número maior, {a} e {b} são iguais!')
