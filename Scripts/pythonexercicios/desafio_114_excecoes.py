import requests
from termcolor import colored
from urllib.request import urlopen
from urllib.error import URLError

url = 'http://pudim.com.br/'
try:
    site = urlopen(url)
    print(colored('Consegui acessar o site Pudim com sucesso!', 'light_yellow'))
except URLError:
    print(colored('O site Pudim não está acessível no momento.', 'light_red'))
    
#solucao usando a biblioteca requests
'''try:
    response = requests.get(url)
    if response.status_code == 200:
        print(colored('Consegui acessar o site Pudim com sucesso!', 'light_yellow'))
except:
    print(colored('O site Pudim não está acessível no momento.', 'light_red'))'''
