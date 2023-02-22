from sys import exit
from termcolor import colored
print(colored(f"{' LOJAS GUANABARA ':=^40}", 'cyan'))
preco = float(input(colored('Informe o valor das compras: R$ ', 'light_yellow')))
opcao = int(input(colored('''FORMAS DE PAGAMENTO: 
\033[7;36m[1]\033[m A vista dinheiro 
\033[7;36m[2]\033[m A vista no cartão 
\033[7;36m[3]\033[m 2x no cartão 
\033[7;36m[4]\033[m 3x ou mais no cartão
\033[36mEscolha a opção: ''', 'cyan')))
if opcao == 1:
    vlr_a_pagar = preco * 0.9 
    print(colored(f'O valor a pagar em dinheiro/cheque com 10% de desconto é de \033[33mR$ {vlr_a_pagar:.2f}', 'light_green'))
elif opcao == 2:
    vlr_a_pagar = preco * 0.95
    print(colored(f"O valor a pagar no cartão com 5% de desconto é de \033[33mR$ {vlr_a_pagar:.2f}", "light_green"))
elif opcao == 3:
    vlr_a_pagar = preco
    vlr_prestacao = vlr_a_pagar / 2
    print(colored(f'Sua compra de R$ {vlr_a_pagar:.2f} será parcelada em 2x de R$ {vlr_prestacao:.2f} sem juros.', 'light_green'))
elif opcao == 4:
    parcela = int(input(colored('Quantas parcelas? ', 'light_cyan')))
    vlr_a_pagar = preco * 1.20
    vlr_prestacao = vlr_a_pagar / parcela 
    print(colored(f'O Valor total a pagar é {vlr_a_pagar:.2f} já acrescidos os juros de 20%, ficará em {parcela}x de \033[33mR$ {vlr_prestacao:.2f} no cartão.', 'light_green'))
else:
    print(colored('Opçao inválida!', 'light_red'))
    exit()
