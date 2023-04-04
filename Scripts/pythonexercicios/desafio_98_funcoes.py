import os
#limpa a tela do terminal
os.system('cls' if os.name == 'nt' else 'clear')

from time import sleep

def contador(num1, num2, passo):
    print('-=' * 20)
    print(f'Contagem de {num1} até {num2} de {passo} em {passo}') #retorna um valor absoluto
    passo = passo if passo != 0 else 1 #sintaxe de conpreensa, se passo = 0 para nao dar erro transformamos em 1.
    sleep(1)
    if num1 > num2:
        while num1 >= num2:
            print(num1, end = ' ', flush=True)
            sleep(.3)
            num1 -= passo
    else: 
        while num1 <= num2:
            print(num1, end = ' ', flush=True)
            sleep(.3)
            num1 += passo
    print('FIM!')
   

contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = abs(int(input('Passo: ')))
contador(inicio, fim, passo)
print()