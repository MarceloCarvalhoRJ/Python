def cor_fundo(c):
    cor = (
    '\033[m',         # 0 - sem cores 
    '\033[0;30;41m',  # 1 - Branco em Vermelho
    '\033[0;30;42m',  # 2 - Branco em Verde
    '\033[0;30;43m',  # 3 - Branco em Amarelo
    '\033[0;30;44m',  # 4 - Branco em Azul
    '\033[0;30;45m',  # 5 - Branco em Roxo
    '\033[0;30;46m',  # 6 - Branco em Ciano
    '\033[7;30m',     # 7 - Branco 
    )
    return cor[c]

print(f'Hello, {cor_fundo(5)}World!{cor_fundo(0)}')