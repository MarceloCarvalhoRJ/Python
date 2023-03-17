def find_average(numbers):
    return sum(numbers) / len(numbers)

numbers = []

while True:
    n = (float(input('Digite um numero (-1 para sair): ')))
    if n < 0 and len(numbers) == 0:
        print('Fim do programa')
        break
    if n >= 0:
        numbers.append(n) 
    else:
        print('-=' * 20)
        print(f'Voce digitou {len(numbers)} números com média {find_average(numbers):.2f}')
        print('-=' * 20)
        print('Fim do programa. Volte Sempre!')
        break

