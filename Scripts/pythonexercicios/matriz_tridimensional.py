false = False

rooms = [[[false for i in range(20)] for j in range(15)] for c in range(3)]

occupied = 0

#ocupar o quarto 15 em todos os 15 andares nos 3 edificios 
for build in rooms:
    for floor in build:
        floor[14] = True

#Agora você pode reservar um quarto para dois noivos: no segundo edifício, no décimo andar, quarto 14:
rooms[1][9][13] = True

#liberar a segunda sala no quinto andar, localizada no primeiro edifício:
rooms[0][4][1] = False

#Verifique se há vagas no 15º andar do terceiro edifício:
vocancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vocancy += 1


for build in rooms:
    for floor in build:
        for room in floor:
            if room == True:
                occupied += 1

print(rooms)
print()
print(f'existente {occupied} quartos ocupados no momento.')
print()
print(f'Existem {vocancy} quartos livres no 15º andar do 3º edificio.')