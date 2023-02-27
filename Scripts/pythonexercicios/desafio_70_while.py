from letreiro import letreiro, letreiro_2
from termcolor import colored

letreiro ('LOJA SUPER BARATÃO', 'cyan', 'light_yellow')

total_compras = produtos_caro = produto_barato = menor = 0

while True: 
    nome_produto = input(colored('Nome do Produto: ', 'magenta'))
    preco = float(input(colored('Preço: R$ ', 'magenta')))
    total_compras += preco
    if preco >= 1000:
        produtos_caro += 1
    if menor is 0 or preco < menor: #"menor" só será atualizado se ainda não tiver um valor ou se o novo preço for menor do que o valor atual.
        menor = preco
        produto_barato = nome_produto
    while True:
        continua = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continua in 'SN':
            break
    if continua == 'S':
        print(colored('.' * 25, 'light_yellow'))
    else:
        print(colored(f"+{' FIM DO PROGRAMA ':=^35}+", 'light_yellow'))
        print(colored(f'O total de compras foi R$ {total_compras:.2f}', 'cyan'))
        print(colored(f'Temos {produtos_caro} produtos custando mais de R$ 1.000,00', 'cyan'))
        print(colored(f'O produto mais barato foi {produto_barato} que custa R$ {menor:.2f}', 'cyan'))
        letreiro_2('Volte Sempre!', 'yellow', 'blue')
        break
    
        