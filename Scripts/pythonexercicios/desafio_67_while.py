from termcolor import colored
from time import sleep
from letreiro import letreiro, letreiro_2

letreiro('CALCULADORA DE TABUADA', 'blue', 'magenta')
while True:
    num = int(input(colored('Quer ver a tabuada de qual valor: ', 'yellow')))
    if num < 0:
        print(colored('\nPrograma de tabuada encerrado.\n', 'red'))
        break
    print('-' * 30)
    for i in range(1, 11):
        resultado = num * i
        print(f"{num} x {i:2} = {colored(str(resultado), 'cyan')}")
        sleep(.1)
    print('-' * 30)
    sleep(.5)

letreiro_2('Obrigado e volte sempre!', 'magenta', 'blue')       