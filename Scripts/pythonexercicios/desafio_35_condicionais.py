from termcolor import colored
print(colored('-=-' * 10, 'light_yellow')) # colore a fonte
print(colored('   Analisador de Triangulos', 'blue'))
print(colored('-=-' * 10, 'light_yellow'))
a = float(input('Informe o segmento da 1ª reta: cm '))
b = float(input('Informe o segmento da 2ª reta: cm '))
c = float(input('Informe o segmento da 3ª reta: cm '))
if a < b + c and c < a + b and c < a + b:
    print(colored('Os segmentos de reta formam um triângulo', 'yellow'))
else:
    print('Os segmentos de reta \033[31mNÃO\033[0m formam um triângulo')
