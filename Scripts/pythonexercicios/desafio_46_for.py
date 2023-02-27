from time import sleep
from emoji import emojize
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emojize(':fireworks::collision::sparkler::party_popper::sparkles::party_popper::confetti_ball:' * 5 + '\n') * 5) # usando emoji de fogos de artificio e explosao, imprimindo 5x em 5 linhas. 
