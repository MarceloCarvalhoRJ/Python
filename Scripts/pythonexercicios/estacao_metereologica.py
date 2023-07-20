

temperatures_month = [[20.0 for i in range(24)] for j in range(31)]

print(temperatures_month)

total, cont_20 = 0.0, 0.0
highest = temperatures_month [0][0]

for day in temperatures_month:
    total += day[11]
    if day[11] == 20.0:
        cont_20 +=1
    for temp in day:
        if temp > highest:
            highest = temp

average = total / 31

print('')
print('A temperatura média do meio dia eh:', average)
print('')
print('A maior temperatura do mês foi:', highest)
print('')
print('Qtde de dias que a temperatura ao meio-dia foi de 20º:', cont_20)
