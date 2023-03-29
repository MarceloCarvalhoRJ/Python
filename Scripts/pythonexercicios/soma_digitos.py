numero = int(input('Digite um número: '))

soma = 0
while True:
    # obter o último dígito do número
    ultimo_digito = numero % 10

    # remover o último dígito do número
    numero //= 10

    # adicionar o último dígito à soma
    soma += ultimo_digito

    # verificar se todos os dígitos foram obtidos
    if numero == 0:
        break

print(f"Soma dos dígitos: {soma}")


'''
numero = input('Digite um nº: ')
digitos = ''.join(numero)
soma = sum(int(dig) for dig in digitos)
print(soma)
'''
