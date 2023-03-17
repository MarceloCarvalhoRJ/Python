def past(h, m, s):    
    if 0 < h > 23 or 0 < m > 59 or 0 < s > 59:
        return 1 
    else:
        result = ((h * 3600) + (m * 60) + s) * 1000
        return result   
while True:
    hour = int(input('Digite a Hora: '))
    min = int(input('Digite os minutos: '))
    sec = int(input('Digite os segundos: '))
    if past(hour, min, sec) == 1:   
        print('Invalid Value!')
    else:
        print(f'A hora {hour}:{min}:{sec} em milesegundos é {past(hour, min, sec)} ')
        break



'''
h = 0
m = 1
s = 1

result = 61000
Restrições de entrada:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59'''