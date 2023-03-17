def make_negative(number):
    return -abs(number) #transforma o numero em inteiro absoluto 'abs(number)' em negativo.
    #abs(number)
    #return number * -1
n = int(input('Digite um numero positivo: '))
print(f'O negativo é {make_negative(n)}')
