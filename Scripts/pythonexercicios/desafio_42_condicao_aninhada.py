from termcolor import colored

print(colored('-=-' * 10, 'light_yellow')) # colore a fonte
print(colored('   Analisador de Triangulos', 'blue'))
print(colored('-=-' * 10, 'light_yellow'))
a = float(input('Informe o segmento da 1ª reta: cm '))
b = float(input('Informe o segmento da 2ª reta: cm '))
c = float(input('Informe o segmento da 3ª reta: cm '))
if a < b + c and b < a + c and c < a + b:
    print(colored('Os segmentos de reta formam um triângulo.', 'yellow'))
    if a == b and b == c: # o python aceita tb aceita: a == b == c
        print(colored('Ele é do tipo Equilátero', 'green'))   
    elif a != b != c != a:
        print(colored('Ele é do tipo Escaleno', 'green'))
    else:
        print(colored('Ele é do tipo Isósceles', 'green'))
else:
    print('Os segmentos de reta \033[31mNÃO\033[0m formam um triângulo')