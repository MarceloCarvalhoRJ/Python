from random import choice
from sys import exit
from time import sleep
from termcolor import colored
from letreiro import letreiro

def display_board(board):
 # A função aceita um parâmetro contendo o status atual da placa
 # e o imprime no console.
    print( f'''
        +-------+-------+-------+
        |       |       |       |
        |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
        |       |       |       |
        +-------+-------+-------+
        |       |       |       |
        |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
        |       |       |       |
        +-------+-------+-------+
        |       |       |       |
        |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
        |       |       |       |
        +-------+-------+-------+''')



def enter_move(board):
 # A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada, 
 # verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.
    print()
    your_move = int(input('Digite seu movimento: '))
    number_list.remove(your_move)
    sleep(1)
    for r in range(3):
        for c in range(3):
            if your_move == board[r][c]:
                board[r][c] = colored('0', 'green')
    display_board(board)
    victory_for(board)
    sleep(1)



def draw_move(board):
 # A função desenha o movimento do computador e atualiza o tabuleiro.         

    computer_move = choice(number_list)
    print(f'Meu movimento...{computer_move}')
    sleep(1)
    number_list.remove(computer_move) 
    for r in range(3):
        for c in range(3):
            if computer_move == board[r][c]:
                board[r][c] = colored('X', 'red')           
        
    display_board(board)
    
  

def victory_for(board):
        # A função analisa o estado da placa a fim de verificar se 
        # o jogador usando 'O's ou 'X's ganhou o jogo
    if ((board[0][0] == colored('0', 'green') and board[0][1] == colored('0', 'green') and board[0][2] == colored('0', 'green')) or (board[1][0] == colored('0', 'green') and board[1][1] == colored('0', 'green') and board[1][2] == colored('0', 'green')) or (board[2][0] == colored('0', 'green') and board[2][1] == colored('0', 'green') and board[2][2] == colored('0', 'green'))) or ((board[0][0] == colored('0', 'green') and board[1][0] == colored('0', 'green') and board[2][0] == colored('0', 'green')) or (board[0][1] == colored('0', 'green') and board[1][1] == colored('0', 'green') and board[2][1] == colored('0', 'green')) or (board[0][2] == colored('0', 'green') and board[1][2] == colored('0', 'green') and board[2][2] == colored('0', 'green'))) or ((board[0][0] == colored('0', 'green') and board[1][1] == colored('0', 'green') and board[2][2] == colored('0', 'green')) or (board[0][2] == colored('0', 'green') and board[1][1] == colored('0', 'green') and board[2][0] == colored('0', 'green'))): 
        print('Voce Ganhou!')
        sleep(1)
        play_again()
        
    elif ((board[0][0] == colored('X', 'red') and board[0][1] == colored('X', 'red') and board[0][2] == colored('X', 'red')) or (board[1][0] == colored('X', 'red') and board[1][1] == colored('X', 'red') and board[1][2] == colored('X', 'red')) or 
    (board[2][0] == colored('X', 'red') and board[2][1] == colored('X', 'red') and board[2][2] == colored('X', 'red'))) or ((board[0][0] == colored('X', 'red') and board[1][0] == colored('X', 'red') and board[2][0] == colored('X', 'red')) or 
    (board[0][1] == colored('X', 'red') and board[1][1] == colored('X', 'red') and board[2][1] == colored('X', 'red')) or (board[0][2] == colored('X', 'red') and board[1][2] == colored('X', 'red') and board[2][2] == colored('X', 'red'))) or ((board[0][0] == colored('X', 'red') and board[1][1] == colored('X', 'red') and board[2][2] == colored('X', 'red')) or 
    (board[0][2] == colored('X', 'red') and board[1][1] == colored('X', 'red') and board[2][0] == colored('X', 'red'))): 
        print('O Computador Ganhou!')
        sleep(1)
        play_again()
        
    elif number_list == []:
        print('O Jogo Empatou.')
        sleep(1)
        play_again()
        
    

def play_again():
    global answer
    print()
    while True:
        answer_play = input('Quer jogar novamente [S/N]? ').upper()
        if 'N' in answer_play:
            exit()
        elif 'S' in answer_play:
            answer = 1
            return 
                
                    
             
while True:
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    computer_move, your_move = 0, 0

    answer = 0

    letreiro('Jogo da Velha', 'yellow', 'cyan')

    print(colored('        Vamos começar o jogo!', 'magenta'))
    print()
    while True:
        
        if answer == 1:
           break

        draw_move(board)
        victory_for(board)
        sleep(1)
        
        enter_move(board)
        victory_for(board)
        sleep(1)

       
        
        
    